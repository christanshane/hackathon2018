from django.forms import ModelForm
from django import forms
from .models import Order, BC_Form, PC_Form, NBIC_Form, User_Portfolio

class OrderForm(ModelForm):
    OPTIONS = (
        ('',''),
        ('Postpay','Postpay'),
        ('Prepay (Full)','Prepay (Full)'),
        ('Prepay (Half)', 'Prepay (Half)')
    )
    OPTIONS2 = (
        ('Confirm', 'Confirm'),
        ('Ready', 'Ready'),
        ('Send', 'Send'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
        ('Cancelled', 'Cancelled')
    )
    order_status = forms.TypedChoiceField(required=False, choices=OPTIONS2, widget=forms.RadioSelect)
    payment_option = forms.ChoiceField(choices=OPTIONS)

    class Meta:
        model = Order
        fields = ['name','phone','address','delivery_date','product_id','payment_option','amount','order_status']


class BC_Form(ModelForm):
    class Meta:
        model = BC_Form
        fields = ['bc_name', 'bc_address', 'bc_age', 'bc_dateissued']

        widgets ={
            'bc_name': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'bc_address': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'bc_age': forms.TextInput(attrs={'placeholder': '', '': 'form-control'}),
            'bc_dateissued': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        }

class PC_Form(ModelForm):
    class Meta:
        model = PC_Form
        fields = ['pc_name', 'pc_address', 'pc_place_of_birth', 'pc_date_of_birth', 'pc_purpose']

        widgets = {
            'pc_name': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'pc_address': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'pc_place_of_birth': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'pc_date_of_birth': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'pc_purpose': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        }

class NBIC_Form(ModelForm):
    class Meta:
        model = NBIC_Form
        fields = ['nbic_name', 'nbic_gender', 'nbic_purpose', 'nbic_civil_status', 'nbic_place_of_birth', 'nbic_date_of_birth', 'nbic_nationality']

        widgets = {
            'nbic_name': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'nbic_gender': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'nbic_purpose': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'nbic_civil_status': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'nbic_place_of_birth': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'nbic_date_of_birth': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'nbic_nationality': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        }

# class UserPortfolioForm(ModelForm):
#     class Meta:
#         model = User_Portfolio
#         fields = ['name','phone','address','delivery_date','product_id','payment_option', 'amount', 'order_status']