<div align="center">

# python-t-test

[![PyPI version](https://img.shields.io/pypi/v/your-package)](link-to-pypi-page)
[![codecov](https://codecov.io/github/ashkonf/python-t-test/graph/badge.svg?token=7Y596J8IYZ)](https://codecov.io/github/ashkonf/python-t-test)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Pytest](https://img.shields.io/badge/pytest-✓-brightgreen)](https://docs.pytest.org)
[![Pyright](https://img.shields.io/badge/pyright-✓-green)](https://github.com/microsoft/pyright)
[![Ruff](https://img.shields.io/badge/ruff-✓-blue?logo=ruff)](https://github.com/astral-sh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Build Status](https://img.shields.io/github/actions/workflow/status/ashkonf/python-t-test/ci.yml?branch=main)](https://github.com/ashkonf/python-t-test/actions/workflows/ci.yml?query=branch%3Amain)

A simple Python implementation of standard statistical t-test and confidence interval estimation.

</div>

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Linting and Type Checking](#linting-and-type-checking)
- [Example](#example)

## Installation

This project requires Python 3.8 or newer and uses [uv](https://docs.astral.sh/uv/) for dependency management.
Install dependencies with:

```
uv sync
```

## Usage

The module exports two public functions:

- `perform_t_test(points1, points2, two_sided=True) -> float`
- `calculate_confidence_interval(points, confidence_threshold=0.95) -> Tuple[float, float]`

## Running Tests

Run tests with full coverage using:

```
uv run --extra dev pytest --cov
```

## Linting and Type Checking

- Format code: `uv run --extra dev ruff format`
- Lint code: `uv run --extra dev ruff check`
- Type check: `uv run --extra dev pyright`

## Example

```python
import random
from ttest import calculate_confidence_interval, perform_t_test

random.seed(1234)
points1 = random.sample(range(10, 30), 10)
points2 = random.sample(range(15, 35), 10)

p_value = perform_t_test(points1, points2)
print("P-value for the sample data:", p_value)

confidence_interval = calculate_confidence_interval(points1, 0.95)
print("Calculated confidence interval:", confidence_interval)
```

## Demo Notebook

For a comprehensive demonstration with visualizations and real-world examples, see the [demo.ipynb](demo.ipynb) Jupyter notebook. It includes:

- Basic usage examples
- Statistical interpretation
- A/B testing scenarios
- Data visualization
- Understanding statistical significance
