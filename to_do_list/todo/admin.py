from atexit import register
from django.contrib import admin

from to_do_list.todo.models import Tag, Task

admin.site.register(Tag)
admin.site.register(Task)