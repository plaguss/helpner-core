"""Script to generate the README for the project. 

Calls the autogenerator from spacy and adds some extra info.
"""

import subprocess
import sys
from pathlib import Path
import srsly

import typer
from wasabi import MarkdownRenderer
root = Path(__file__).parent.parent.resolve()

def get_readme(path: Path) -> str:
    """Grabs the generated readme content as a string. """
    with open(path, "r") as f:
        return f.read()


def get_metrics(path: Path = root / "training" / "metrics.json") -> dict[str, int]:
    """Get the metrics data from the last trained model. 
    Assumes the file will be on the path defined by spacy.
    """
    return srsly.read_json(path)


def add_training_metrics(readme: str) -> str:
    md = MarkdownRenderer()
    md.add(md.title(md.title(2, "Model accuracy")))

def add_versioning(readme: str) -> str:
    """Adds the explanation of how the model is versioned. """
    # Add how the model is versioned (following spacy-models)
    md = MarkdownRenderer()
    md.add(md.title(2, "Model versioning"))
    md.add("This is a paragraph")

    return readme + "\n" + md.text


def main(
    readme_name: str = typer.Argument(
        "README.md", exists=True, dir_okay=False, help="Path to a README.md file"
    )
):
    readme_path = root / "README.md"
    # Call spacy
    subprocess.run(
        [sys.executable, "-m", "spacy", "project", "document", "--output", str(readme_path)],
        check=True
    )
    readme = get_readme(readme_path)



if __name__ == "__main__":
    typer.run(main)
