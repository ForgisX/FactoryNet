# Base Repository

This is a base repository for Xelerit projects.

## Getting Started

### Prerequisites

- [uv](https://github.com/astral-sh/uv)

### Installation

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  Create a virtual environment and install dependencies:
    ```bash
    uv venv
    uv pip install -r requirements.txt
    ```

## Documentation

To view the documentation, run:

```bash
mkdocs serve
```

Then open your browser to `http://127.0.0.1:8000`. 

## Code Style and Pre-commit Hooks

This repository uses [pre-commit](https://pre-commit.com/) to enforce code style with Black, isort, and flake8.



### Setup pre-commit

1. Install pre-commit and style tools:
    ```bash
    uv pip install -r requirements.txt
    ```
2. Install the pre-commit hooks:
    ```bash
    pre-commit install
    ```

### Usage
- Hooks will run automatically on `git commit`.
- To run checks manually on all files:
    ```bash
    pre-commit run --all-files
    ``` 

For more details on code style and pre-commit hooks, see the [documentation](docs/index.md). 


### Dataset Structure 

The dataset contain 6 different fields:

1. **id**: unique identifier of a timeseries

2. **timestamps**: timestamp of each ts point 

3. **values**: timeseries datapoint

4. **domain**: if it's real or syntethic

5. **subtype**: tag that give informations on the type of timeseries 

        -industrial
        -step
        -sine
        -random_walk
        -stock

6. **statistics**: a dictionary of timeseries's statistics

        -max
        -min
        -mean
        -std