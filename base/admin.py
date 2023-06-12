from django.contrib import admin
from base.models import Var, DOE, DOEvar, Varlevel, DOErun 

# Register your models here.
admin.site.register(Var)
admin.site.register(DOE)
admin.site.register(DOEvar)
admin.site.register(Varlevel)
admin.site.register(DOErun)