FROM python:3.13.5

COPY dist/*.whl /
RUN pip install *.whl && rm -r *.whl



