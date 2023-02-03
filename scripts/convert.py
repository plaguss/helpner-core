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
    for i, eg in enumerate(srsly.read_jsonl(input_path)):

        doc = nlp(eg["message"])

        try:
            doc.ents = [
                doc.char_span(start, end, label=label)
                for label, start, end in eg["annotations"]
            ]
        except Exception as e:
            # There is a bug in cli-help-maker?
            # Some messages failed with the following error:
            # File "/home/agustin/github_repos/helpner-core/scripts/convert.py", line 39, in main
            #     raise e from Exception
            # File "/home/agustin/github_repos/helpner-core/scripts/convert.py", line 27, in main
            #     doc.ents = [
            #     ^^^^^^^^
            # File "spacy/tokens/doc.pyx", line 758, in spacy.tokens.doc.Doc.ents.__set__
            # File "spacy/tokens/doc.pyx", line 1974, in spacy.tokens.doc.get_entity_info
            # TypeError: object of type 'NoneType' has no len()
            print(f"Couldn't process message: {i}")
            continue

        doc_bin.add(doc)

    doc_bin.to_disk(output_path)
    print(f"Processed {len(doc_bin)} documents: {output_path.name}")


if __name__ == "__main__":
    typer.run(main)
