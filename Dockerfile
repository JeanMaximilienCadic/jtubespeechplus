FROM python:3.13.11

COPY dist/*.whl /
RUN pip install *.whl && rm -r *.whl



