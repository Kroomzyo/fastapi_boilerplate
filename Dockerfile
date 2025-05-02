FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


ENV POETRY_VERSION=2.1.2
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 -
ENV PATH="/opt/poetry/bin:$PATH"


WORKDIR /app


COPY pyproject.toml poetry.lock* /app


RUN poetry config virtualenvs.create false

RUN poetry install --no-root

# EXPOSE 8000

COPY . /app


# CMD ["uvicorn", "--factory", "main:create_app", "--host", "0.0.0.0", "--port", "8000", "--reload"]