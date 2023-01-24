"""Script to transform the a dataset in jsonl to a DocBin.

Copied from the spacy tutorials:
https://spacy.io/usage/training#training-data
https://github.com/explosion/projects/blob/v3/tutorials/ner_fashion_brands/scripts/preprocess.py
"""

from pathlib import Path

import spacy
import srsly
import typer
from spacy.tokens import DocBin


def main(
    input_path: Path = typer.Argument(..., exists=True, dir_okay=False),
    output_path: Path = typer.Argument(..., dir_okay=False),
):
    nlp = spacy.blank("en")
    doc_bin = DocBin()
    for eg in srsly.read_jsonl(input_path):

        doc = nlp(eg["message"])

        doc.ents = [
            doc.char_span(start, end, label=label)
            for label, start, end in eg["annotations"]
        ]
        doc_bin.add(doc)

    doc_bin.to_disk(output_path)
    print(f"Processed {len(doc_bin)} documents: {output_path.name}")


if __name__ == "__main__":
    typer.run(main)
