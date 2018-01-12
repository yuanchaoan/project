from django.contrib import admin
from movie.models import movies,comments,country,type,actors
# Register your models here.
admin.site.register(movies)
admin.site.register(comments)
admin.site.register(country)
admin.site.register(type)
admin.site.register(actors)