FROM python:3.12-slim-trixie

WORKDIR /usr/src/app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY pyproject.toml .
RUN uv sync

# RUN pip install pipenv
# COPY Pipfile ./
# RUN pipenv install

COPY . .

CMD [ "uv", "run", "main.py" ]