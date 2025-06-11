FROM python:3.13.4

COPY dist/*.whl /
RUN pip install *.whl && rm -r *.whl



