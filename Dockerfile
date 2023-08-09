FROM python:3.9.17-slim

WORKDIR /code
COPY . /code

RUN apt-get update && apt-get -y install python3-dev
RUN pip install --upgrade pip setuptools wheel pybind11
RUN pip install -e .[dev]
# RUN pip install --upgrade pip setuptools wheel
# RUN python -m pip install python-dev-tools --user --upgrade
# RUN conda install -c conda-forge hdbscan
# RUN pip install --no-binary :all: faiss-cpu
# RUN pip install -e .

ENV FLASK_APP=run.py
CMD [ "flask", "run", "--host=0.0.0.0"]

