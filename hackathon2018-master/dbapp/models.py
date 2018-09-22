from django.db import models
from django.urls import reverse

# Create your models here.
class BC_Form:
    bc_name = models.CharField(max_length=25, default='')
    bc_address = models.CharField(max_length=25, default='')
    bc_age = models.CharField(max_length=25, default='')
    bc_dateissued = models.DateField(blank=True)

    def __unicode__(self):
        return self.pk

class PC_Form:
    pc_name = models.CharField(max_length=25, default='')
    pc_address = models.CharField(max_length=25, default='')
    pc_place_of_birth = models.CharField(max_length=25, default='')
    pc_date_of_birth = models.DateField(blank=True)
    pc_purpose = models.CharField(max_length=25, default='')

    def __unicode__(self):
        return self.pk

class NBIC_Form:
    nbic_name = models.CharField(max_length=25, default='')
    nbic_gender = models.CharField(max_length=25, default='')
    nbic_purpose = models.CharField(max_length=25, default='')
    nbic_civil_status = models.CharField(max_length=25, default='')
    nbic_place_of_birth = models.CharField(max_length=25, default='')
    nbic_date_of_birth = models.CharField(max_length=25, default='')
    nbic_nationality = models.CharField(max_length=25, default='')

    def __unicode__(self):
        return self.pk

class User_Portfolio:
    up_name = models.CharField(max_length=25, default='')
    up_date_of_birth = models.DateField(blank=True)
    up_gender = models.CharField(max_length=25, default='')
    up_per_address = models.CharField(max_length=25, default='')
    up_cur_address = models.CharField(max_length=25, default='')
    up_email_address = models.CharField(max_length=25, default='')
    up_mobile_number = models.CharField(max_length=25, default='')
    up_civil_status = models.CharField(max_length=25, default='')
    up_place_of_birth = models.CharField(max_length=25, default='')
    up_nationality = models.CharField(max_length=25, default='')

    from django.db import models

    # Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=200);
    phone = models.CharField(max_length=20);
    address = models.TextField();
    delivery_date = models.DateField(blank=True);
    product_id = models.TextField();
    payment_option = models.CharField(max_length=50);
    amount = models.IntegerField();
    order_status = models.CharField(max_length=50);
