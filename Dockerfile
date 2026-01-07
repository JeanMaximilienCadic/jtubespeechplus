FROM python:3.14.2

COPY dist/*.whl /
RUN pip install *.whl && rm -r *.whl



