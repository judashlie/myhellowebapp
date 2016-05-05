from django.contrib import admin

# import models
from collection.models import Problem

# set up slug creation
class ProblemAdmin(admin.ModelAdmin):
	model = Problem
	list_display = ('name', 'description',)
	prepopulated_fields = {'slug': ('name',)}

# register models
admin.site.register(Problem, ProblemAdmin)
