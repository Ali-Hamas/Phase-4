FROM python:3.13-slim

WORKDIR /app

ENV PIP_DEFAULT_TIMEOUT=1000

COPY pyproject.toml ./
COPY poetry.lock* ./

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]