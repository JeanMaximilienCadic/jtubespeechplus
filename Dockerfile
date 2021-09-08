FROM python:3.8

COPY dist/*.whl /
RUN pip install *.whl && rm -r *.whl



