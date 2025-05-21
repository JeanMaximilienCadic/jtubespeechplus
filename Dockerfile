FROM python:3.13.3

COPY dist/*.whl /
RUN pip install *.whl && rm -r *.whl



