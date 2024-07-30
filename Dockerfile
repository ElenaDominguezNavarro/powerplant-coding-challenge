FROM python:3.12-slim

WORKDIR /code

COPY requirements.txt .

RUN pip install "uvicorn[standard]"
RUN pip install sqlalchemy
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

COPY init.sql /docker-entrypoint-initdb.d/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]
