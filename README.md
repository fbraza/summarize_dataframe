# Summarize dataframe

[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]

<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/summarize_dataframe
[pypi-url]: https://pypi.org/project/summarize-dataframe/
[build-image]: https://github.com/fbraza/summarize_dataframe/actions/workflows/ci.yml/badge.svg
[build-url]: https://github.com/fbraza/summarize_dataframe/blob/master/.github/workflows/ci.yml

## Feature

This python library permits to get some statistic about your pandas DataFrame. It returns the number of rows and columns
and the frequency of each datatype present in the DataFrame

## Usage

To install the package, run:

```bash
pip install summarize-dataframe
```

It has been tested for Python `3.7`, `3.8` and `3.9`

## Developers

To run the tests:

install first [poetry]() and run:

```bash
poetry install
```

Next run:

```
poetry run pytest
```

or:

```bash
tox
```

## About

Faouzi Braza
