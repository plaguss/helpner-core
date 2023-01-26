<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Detecting Commands, Arguments and Options in CLI Help messages (Named Entity Recognition)

This project deals with the backbone model that powers [helpner](https://github.com/plaguss/helpner).

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `create-dataset` | Create a dataset using [cli-help-maker](https://github.com/plaguss/cli-help-maker) |
| `split` | Split the .jsonl dataset file contents in train/dev |
| `convert` | Convert .jsonl files to .spacy format |
| `train` | Train a named entity recognition model on cli help messages |
| `evaluate` | Evaluate the model and export metrics |
| `package` | Package the trained model so it can be installed |
| `release` | WIP: Upload the packaged model to github releases |
| `readme` | Auto-generate README via spacy. |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `split` &rarr; `convert` &rarr; `train` &rarr; `evaluate` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets/dataset.jsonl` | Local | JSONL-formatted training data obtained from [`cli-help-maker`](https://github.com/plaguss/cli-help-maker) |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
## Model metrics

The following metrics are obtained from the `spacy benchmark accuracy` command:

### Accuracy

| Type | Score |
| --- | --- |
| token_acc | 100.00 |
| token_p | 100.00 |
| token_r | 100.00 |
| token_f | 100.00 |
| speed | 3324722.16 |

### NER (per type)

|  | P | R | F |
| --- | --- | --- | --- |
| CMD | 100.00 | 94.06 | 96.94 |
| ARG | 100.00 | 100.00 | 100.00 |
| OPT | 100.00 | 100.00 | 100.00 |
## Model versioning

The naming conventions and versioning scheme follows the conventions used in [spacy-models](https://github.com/explosion/spacy-models) (in spirit), but so much simplified.

See for the [model-versioning](https://github.com/explosion/spacy-models#model-versioning) section, replace `spaCy` with `helpner`, and that's the idea.
## Downloading a model

The trained models are uploaded as [release assets](https://github.com/plaguss/helpner-core/releases) in GitHub, so they can be installed via pip,         and loaded in spacy via `spacy.load`.