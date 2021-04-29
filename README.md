# Summarize dataframe

[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![Code Quality][quality-image]][quality-url]

<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/podsearch
[pypi-url]: https://pypi.org/project/podsearch/
[build-image]: https://github.com/nalgeon/podsearch-py/actions/workflows/build.yml/badge.svg
[build-url]: https://github.com/nalgeon/podsearch-py/actions/workflows/build.yml
[quality-image]: https://api.codeclimate.com/v1/badges/3130fa0ba3b7993fbf0a/maintainability
[quality-url]: https://codeclimate.com/github/nalgeon/podsearch-py

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
