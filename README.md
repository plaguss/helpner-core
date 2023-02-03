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
| speed | 3228586.60 |

### NER (per type)

|  | P | R | F |
| --- | --- | --- | --- |
| CMD | 98.25 | 99.96 | 99.10 |
| ARG | 94.79 | 89.97 | 92.32 |
| OPT | 98.88 | 98.96 | 98.92 |
## Model versioning

The naming conventions and versioning scheme follows the conventions used in [spacy-models](https://github.com/explosion/spacy-models) (in spirit), but so much simplified.

See for the [model-versioning](https://github.com/explosion/spacy-models#model-versioning) section, replace `spaCy` with `helpner`, and that's the idea.
## Downloading a model

The trained models are uploaded as [release assets](https://github.com/plaguss/helpner-core/releases) in GitHub, so they can be installed via pip,         and loaded in spacy via `spacy.load`.
## Descriptive statistics of the last dataset used for training.

A total of 1000 help messages were used.
|                                   |      mean |       std |          min |       25% |       50% |        75% |        max |
|:----------------------------------|----------:|----------:|-------------:|----------:|----------:|-----------:|-----------:|
| indent_spaces                     |  3.012    |  1.00043  |  2           |  2        |  4        |   4        |   4        |
| total_width                       | 89.344    | 16.2353   | 70           | 78        | 80        | 100        | 120        |
| prob_name_capitalized             |  0.503812 |  0.287329 |  0.00189856  |  0.254035 |  0.523925 |   0.74786  |   0.998479 |
| description_before                |  0.472    |  0.499465 |  0           |  0        |  0        |   1        |   1        |
| description_after                 |  0.498    |  0.500246 |  0           |  0        |  0        |   1        |   1        |
| program_description_prob          |  0.490548 |  0.28722  |  0.00167024  |  0.242151 |  0.477199 |   0.74083  |   0.99586  |
| usage_section                     |  0.516    |  0.499994 |  0           |  0        |  1        |   1        |   1        |
| usage_pattern_capitalized         |  0.484    |  0.499994 |  0           |  0        |  0        |   1        |   1        |
| commands_section                  |  0.815    |  0.388492 |  0           |  1        |  1        |   1        |   1        |
| commands_header                   |  1        |  0        |  1           |  1        |  1        |   1        |   1        |
| commands_capitalized              |  0.49958  |  0.284029 |  0.0022922   |  0.25243  |  0.501338 |   0.737582 |   0.999426 |
| commands_documented_prob          |  0.505911 |  0.283441 |  0.00123438  |  0.27576  |  0.509805 |   0.742631 |   0.99995  |
| arguments_section                 |  0.492    |  0.500186 |  0           |  0        |  0        |   1        |   1        |
| arguments_header                  |  1        |  0        |  1           |  1        |  1        |   1        |   1        |
| argument_repeated                 |  0.497881 |  0.285127 |  0.00101773  |  0.270007 |  0.488525 |   0.746068 |   0.999867 |
| argument_documented_prob          |  0.486583 |  0.289539 |  0.000206963 |  0.228881 |  0.472501 |   0.738158 |   0.998935 |
| arguments_pattern_capitalized     |  0.512    |  0.500106 |  0           |  0        |  1        |   1        |   1        |
| argument_capitalized_prob         |  0.492618 |  0.287912 |  0.0060436   |  0.246821 |  0.489228 |   0.747413 |   0.999545 |
| argument_optional_prob            |  0.505243 |  0.295162 |  7.63351e-05 |  0.235492 |  0.507031 |   0.770653 |   0.999283 |
| argument_any_number_prob          |  0.503465 |  0.295311 |  0.000182664 |  0.247908 |  0.511808 |   0.770671 |   0.999878 |
| argument_nested_prob              |  0.5016   |  0.290744 |  0.00096628  |  0.244742 |  0.51879  |   0.751403 |   0.998248 |
| options_section                   |  0.506    |  0.500214 |  0           |  0        |  1        |   1        |   1        |
| options_header                    |  1        |  0        |  1           |  1        |  1        |   1        |   1        |
| option_documented_prob            |  0.507132 |  0.291259 |  0.000381441 |  0.251737 |  0.517262 |   0.761607 |   0.999397 |
| options_pattern_capitalized       |  0.484    |  0.499994 |  0           |  0        |  0        |   1        |   1        |
| options_shortcut                  |  0.510277 |  0.286645 |  0.00107218  |  0.272586 |  0.521389 |   0.750301 |   0.998364 |
| options_shortcut_capitalized_prob |  0.499165 |  0.289056 |  0.000546323 |  0.253128 |  0.495272 |   0.760074 |   0.999867 |
| options_shortcut_all_caps         |  0.524    |  0.499674 |  0           |  0        |  1        |   1        |   1        |
| exclusive_group_optional_prob     |  0.50469  |  0.290709 |  0.00185361  |  0.254987 |  0.514023 |   0.755868 |   0.995541 |
| options_mutually_exclusive_prob   |  0.209    |  0.406798 |  0           |  0        |  0        |   0        |   1        |
| option_set_size                   |  1.977    |  1.42496  |  0           |  1        |  2        |   3        |   4        |
| option_set_size_prob              |  0.506309 |  0.28327  |  0.000160774 |  0.26604  |  0.504979 |   0.742098 |   0.99916  |
| number_of_commands                |  4.52     |  3.4571   |  1           |  2        |  4        |   6        |  15        |
| number_of_arguments               |  4.63     |  3.74688  |  1           |  2        |  3        |   7        |  15        |
| number_of_options                 |  4.543    |  3.72505  |  1           |  1        |  3        |   7        |  15        |
| exclusive_programs                |  1.573    |  1.00682  |  1           |  1        |  1        |   2        |   8        |
