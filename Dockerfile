FROM python:3.14.3

COPY dist/*.whl /
RUN pip install *.whl && rm -r *.whl



