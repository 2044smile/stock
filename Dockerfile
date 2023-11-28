# The base image we want to inhe`it from
FROM python:3.10-slim

# System deps:
RUN apt-get update \
  && apt-get install --no-install-recommends -y procps \
    bash \
    build-essential \
    curl \
    gettext \
    git \
    libpq-dev \
    wget \
  # Cleaning cache:
  && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
  && pip install poetry==1.2.2

# set work directory
WORKDIR /code
COPY pyproject.toml poetry.lock /code/

# Install dependencies:
RUN poetry install --no-root
# copy project
COPY . .

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000