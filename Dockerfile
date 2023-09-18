FROM python:3.10.4-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# ENV PYTHONPATH .
# ENV THENEWBOSTON_SETTING_IN_DOCKER true

RUN set -xe \
  && apt-get update \
  && apt-get install -y --no-install-recommends build-essential \
  && pip install virtualenvwrapper poetry==1.5.1 \
  # && apt-get autoremove python -y\
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# RUN curl -sSL https://install.python-poetry.org | python3 -

COPY ["poetry.lock", "pyproject.toml", "./"]
RUN poetry install --no-root

COPY ["README.md", "Makefile", "auctions", "commerce", "manage.py", "./"]
# COPY auctions /usr/src/app
# COPY commerce /usr/src/app
# COPY auctions /usr/src/app
# COPY commerce commerce

# EXPOSE 8000


# COPY scripts/entrypoint.sh /entrypoint.sh
# RUN chmod a+x /entrypoint.sh

# ENTRYPOINT ["/entrypoint.sh"]

CMD ["poetry", "run", "python3", "runserver", "0.0.0.0:8000"]

# FROM python:3
# WORKDIR /usr/src/app
# RUN pip install -r requirements.txt
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
