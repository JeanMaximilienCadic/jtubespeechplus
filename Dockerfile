FROM python:3.14.0rc2

COPY dist/*.whl /
RUN pip install *.whl && rm -r *.whl



