FROM python:3.14.0rc3

COPY dist/*.whl /
RUN pip install *.whl && rm -r *.whl



