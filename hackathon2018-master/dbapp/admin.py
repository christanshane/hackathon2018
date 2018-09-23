from django.contrib import admin
from .models import BC_Form, PC_Form, NBIC_Form, User_Portfolio
# Register your models here.
admin.site.register(BC_Form)
admin.site.register(PC_Form)
admin.site.register(NBIC_Form)
admin.site.register(User_Portfolio)
