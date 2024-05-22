FROM python:3.12

WORKDIR /to_do_list

RUN pip install --upgrade pip
RUN pip install poetry

COPY pyproject.toml poetry.lock /to_do_list/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000

CMD ["python to_do_list/manage.py migrate"]
