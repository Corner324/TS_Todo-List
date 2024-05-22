#!/bin/sh

python manage.py loaddata todo/fixtures/todo/tasks_fixture.json || echo "Фикстуры уже загружены или произошла ошибка."
python manage.py loaddata todo/fixtures/todo/tags_fixture.json || echo "Фикстуры уже загружены или произошла ошибка."