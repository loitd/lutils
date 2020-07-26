ECHO OFF
REM Set initializer
SET PIPENV_VENV_IN_PROJECT="enabled"
pipenv install

REM To do the test and produce .coverage only
REM pipenv run python -m pytest --cov=lutils

REM To do the test and produce .coverage + XML report
pipenv run python -m pytest --cov=lutils --cov-report=xml

REM To do the test and produce the coverage output HTML + .coverage
REM pipenv run python -m pytest --cov=lutils --cov-report html:cov_html

REM Run as python -m to load current dir into sys.path which is a standard Python behavior.
REM pipenv run python -m pytest

REM To test some marked function
REM pipenv run python -m pytest -m config

REM Upload code cov XML report to codecov.io
pipenv run python -m codecov --token=1aa8175d-dd1b-4608-9a44-867903349afe