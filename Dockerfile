FROM python:3.12.10

COPY dist/*.whl /
RUN pip install *.whl && rm -r *.whl



