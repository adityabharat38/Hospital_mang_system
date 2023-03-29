from django.contrib import admin

# Register your models here.

from hospital_app.models import appointment

# with this command -> we can now acess our database thorugh admin panel , perform crud opeartions at admin level
admin.site.register(appointment)