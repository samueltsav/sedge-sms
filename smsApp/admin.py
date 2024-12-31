from django.contrib import admin
from .models import Staff, FormClass, Subject, Resources, Student


admin.site.register(Staff)
admin.site.register(FormClass)
admin.site.register(Subject)
admin.site.register(Resources)
admin.site.register(Student)