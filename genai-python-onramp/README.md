# Python for GenAI Fast-Track

Welcome to the **Python for GenAI Fast-Track** course! This course is designed for developers with experience in object-oriented programming who want to quickly learn Python for Generative AI applications. The course is delivered entirely through Jupyter notebooks and is designed to be self-paced.

## Learning Goals

-   **Master Python Fundamentals:** Get up to speed with modern Python syntax and features relevant to GenAI.
-   **Hands-on Data Wrangling:** Learn to use Pandas for practical data manipulation and cleaning.
-   **Build Production-Ready Services:** Understand how to structure a Python project, write tests, and build a simple API with FastAPI.

## How to Use This Repository

You can either clone this repository or fork it to your own GitHub account.

### Cloning

```bash
git clone https://github.com/<<USERNAME>>/genai-python-onramp.git
cd genai-python-onramp
```

### Forking

Forking is recommended if you want to save your progress in the notebooks to your own repository.

## Setup for Local Development

You have several options for setting up your local environment. Choose the one you are most comfortable with.

### With pip/venv

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
pip install -r requirements.txt
```

### With Poetry

```bash
poetry install
poetry shell
```

### With uv

```bash
# Install uv
pip install uv

# Create and activate the virtual environment
uv venv
source .venv/bin/activate # On Windows, use `.venv\Scripts\activate`

# Install dependencies
uv pip install -r requirements.txt
```

### With Conda

```bash
# Create and activate the environment
conda create --name genai-python-onramp python=3.9
conda activate genai-python-onramp

# Install dependencies
conda install --file requirements.txt
```

## Environment Command Comparison

| Action                      | `pip/venv`                                      | `poetry`                      | `uv`                                | `conda`                                                   |
| --------------------------- | ----------------------------------------------- | ----------------------------- | ----------------------------------- | --------------------------------------------------------- |
| **Create Environment**      | `python -m venv .venv`                          | `poetry install`              | `uv venv`                           | `conda create -n myenv python=3.9`                        |
| **Activate Environment**    | `source .venv/bin/activate`                     | `poetry shell`                | `source .venv/bin/activate`         | `conda activate myenv`                                    |
| **Install Dependencies**    | `pip install -r requirements.txt`               | `poetry install`              | `uv pip install -r requirements.txt`  | `conda install --file requirements.txt`                   |
| **Add a Package**           | `pip install <pkg>`                             | `poetry add <pkg>`            | `uv pip install <pkg>`              | `conda install <pkg>`                                     |
| **Deactivate Environment**  | `deactivate`                                    | `exit`                        | `deactivate`                        | `conda deactivate`                                        |
| **List Environments**       | (Not directly supported)                        | `poetry env list`             | (Not directly supported)            | `conda env list`                                          |
| **Delete Environment**      | `rm -rf .venv`                                  | `poetry env remove <python>`  | `rm -rf .venv`                      | `conda env remove -n myenv`                               |

## Course Notebooks

Each notebook includes an "Open in Colab" badge at the top. **Note:** You will need to replace `<<USERNAME>>` with your GitHub username for the Colab links to work correctly if you have forked the repository.

### Module 1: Python Refresher for OOP Devs

-   [1.1 Virtual Envs & Poetry/Pip](notebooks/1_python_refresher/1_virtual_envs.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<<USERNAME>>/genai-python-onramp/blob/main/notebooks/1_python_refresher/1_virtual_envs.ipynb)
-   [1.2 Types, Dataclasses, Typing, Pydantic](notebooks/1_python_refresher/2_types_and_dataclasses.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<<USERNAME>>/genai-python-onramp/blob/main/notebooks/1_python_refresher/2_types_and_dataclasses.ipynb)
-   [1.3 Async Basics with httpx/requests](notebooks/1_python_refresher/3_async_httpx.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<<USERNAME>>/genai-python-onramp/blob/main/notebooks/1_python_refresher/3_async_httpx.ipynb)
-   [1.4 Files, JSON, YAML, dotenv, Logging](notebooks/1_python_refresher/4_files_json_yaml.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<<USERNAME>>/genai-python-onramp/blob/main/notebooks/1_python_refresher/4_files_json_yaml.ipynb)
-   [Mini-Lab: Call a public API, parse JSON, and log results](notebooks/1_python_refresher/5_mini_lab_api_json.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<<USERNAME>>/genai-python-onramp/blob/main/notebooks/1_python_refresher/5_mini_lab_api_json.ipynb)

### Module 2: Practical Data Wrangling

-   [2.1 Pandas 101](notebooks/2_data_wrangling/1_pandas_basics.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<<USERNAME>>/genai-python-onramp/blob/main/notebooks/2_data_wrangling/1_pandas_basics.ipynb)
-   [2.2 CSV, Parquet, Basic Plotting](notebooks/2_data_wrangling/2_csv_parquet_plotting.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<<USERNAME>>/genai-python-onramp/blob/main/notebooks/2_data_wrangling/2_csv_parquet_plotting.ipynb)
-   [Mini-Lab: Clean a messy CSV](notebooks/2_data_wrangling/3_mini_lab_clean_csv.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<<USERNAME>>/genai-python-onramp/blob/main/notebooks/2_data_wrangling/3_mini_lab_clean_csv.ipynb)

### Module 3: Project Scaffolding

-   [3.1 VS Code Setup, Repo Hygiene](notebooks/3_project_scaffolding/1_vscode_repo_hygiene.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<<USERNAME>>/genai-python-onramp/blob/main/notebooks/3_project_scaffolding/1_vscode_repo_hygiene.ipynb)
-   [3.2 Pre-commit Hooks & Pytest](notebooks/3_project_scaffolding/2_testing_pytest.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<<USERNAME>>/genai-python-onramp/blob/main/notebooks/3_project_scaffolding/2_testing_pytest.ipynb)
-   [Mini-Project: Build a starter FastAPI service](notebooks/3_project_scaffolding/3_mini_project_fastapi.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<<USERNAME>>/genai-python-onramp/blob/main/notebooks/3_project_scaffolding/3_mini_project_fastapi.ipynb)

## Starter FastAPI Project

This repository includes a starter FastAPI project in the `starter_fastapi` directory. See the [mini-project notebook](notebooks/3_project_scaffolding/3_mini_project_fastapi.ipynb) for a guided walkthrough.
