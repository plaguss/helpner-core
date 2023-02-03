"""Script to generate the README for the project. 

Calls the autogenerator from spacy and adds some extra info.
"""

import subprocess
import sys
from pathlib import Path
import textwrap
import pandas as pd

import srsly
import typer
from wasabi import MarkdownRenderer

root = Path(__file__).parent.parent.resolve()

MetricsType = dict[str, float | dict[str, dict[str, float]]]


def get_readme(path: Path) -> str:
    """Grabs the generated readme content as a string."""
    with open(path, "r") as f:
        return f.read()


def get_metrics(path: Path = root / "training" / "metrics.json") -> MetricsType:
    """Get the metrics data from the last trained model.
    Assumes the file will be on the path defined by spacy.
    """
    return srsly.read_json(path)


def get_arguments(path: Path = root / "training" / "metrics.json") -> MetricsType:
    """Get the metrics data from the last trained model.
    Assumes the file will be on the path defined by spacy.
    """
    return srsly.read_json(path)


def add_training_metrics(readme: str, content: MetricsType) -> str:
    """Adds the training metrics as tables."""
    md = MarkdownRenderer()
    md.add(md.title(2, "Model metrics"))
    md.add("The following metrics are obtained from the `spacy benchmark accuracy` command:")
    md.add(md.title(3, "Accuracy"))
    accuracy_metrics = [
        (m, f"{content[m]*100:.2f}")
        for m in ("token_acc", "token_p", "token_r", "token_f", "speed")
    ]
    table = md.table(accuracy_metrics, ["Type", "Score"])
    md.add(table)

    md.add(md.title(3, "NER (per type)"))
    ner_metrics = []
    for r in ("CMD", "ARG", "OPT"):
        row = [r]
        for c in ("p", "r", "f"):
            row.append(f"{content['ents_per_type'][r][c]*100:.2f}")
        ner_metrics.append(row)

    table = md.table(ner_metrics, ["", "P", "R", "F"])
    md.add(table)

    return readme + "\n" + md.text


def add_versioning(readme: str) -> str:
    """Adds the explanation of how the model is versioned."""
    # Add how the model is versioned (following spacy-models)
    md = MarkdownRenderer()
    md.add(md.title(2, "Model versioning"))
    link = md.link("spacy-models", "https://github.com/explosion/spacy-models")
    text = textwrap.dedent(
        "The naming conventions and versioning scheme follows the conventions used in "
        f"{link} (in spirit), but so much simplified.",
    )
    md.add(text)
    link = md.link("model-versioning", "https://github.com/explosion/spacy-models#model-versioning")
    md.add(f"See for the {link} section, replace `spaCy` with `helpner`, and that's the idea.")

    return readme + "\n" + md.text


def add_downloading(readme: str) -> str:
    """Adds the explanation of how the model is downloaded. """
    # Install via pip
    # Done in helpner
    md = MarkdownRenderer()
    md.add(md.title(2, "Downloading a model"))
    # spaCy: https://github.com/explosion/spacy-models#downloading-models
    link = md.link("release assets", "https://github.com/plaguss/helpner-core/releases")
    text = textwrap.dedent(
        f"The trained models are uploaded as {link} in GitHub, so they can be installed via pip, \
        and loaded in spacy via `spacy.load`."
    )
    md.add(text)

    return readme + "\n" + md.text


def add_arguments_jsonl(readme: str) -> str:
    """Reads the arguments.jsonl generated from the program,
    computes the descriptive statistics and writes the content to 
    the README file.
    """
    project_yml = srsly.read_yaml(root / "project.yml")
    path = project_yml["commands"][0]["outputs"][1]
    path = path.replace("${vars.version}", project_yml["vars"]["version"])
    df = pd.read_json(root / path, lines=True)
    size = len(df)
    df = df.describe().T.drop("count", axis=1)
    resume_arguments = df.to_markdown()

    md = MarkdownRenderer()
    md.add(md.title(2, "Descriptive statistics of the last dataset used for training."))
    md.add(f"A total of {size} help messages were used.")

    return readme + "\n" + md.text + "\n" + resume_arguments + "\n"


def write_readme(content: str, filename: str) -> None:
    with open(filename, "w") as f:
        f.write(content)


def main(
    readme_name: str = typer.Argument(
        "README.md", exists=True, dir_okay=False, help="Path to a README.md file"
    )
):
    readme_path = root / readme_name
    # Call spacy
    subprocess.run(
        [
            sys.executable,
            "-m",
            "spacy",
            "project",
            "document",
            "--output",
            str(readme_path),
        ],
        check=True,
    )
    readme = get_readme(readme_path)
    metrics = get_metrics()
    readme = add_training_metrics(readme, metrics)
    readme = add_versioning(readme)
    readme = add_downloading(readme)
    readme = add_arguments_jsonl(readme)
    write_readme(readme, str(readme_path))


if __name__ == "__main__":
    typer.run(main)
