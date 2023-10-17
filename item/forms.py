from django import forms
from .models import Item , Orders

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'remaining_quantity' ,'price', 'image')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'remaining_quantity' : forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description','remaining_quantity', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'remaining_quantity' : forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }

class OrdersForm(forms.ModelForm):
    PAYMENT_CHOICES = (
        ('Cash', 'Cash'),
        ('Bank Payment', 'Bank Payment'),
    )

    payment = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.Select(attrs={'class': INPUT_CLASSES}))

    class Meta:
        model = Orders
        fields = ('phonenumber', 'address' ,'quantity','payment')
        widgets = {
            'phonenumber': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'address': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'quantity': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
    def __init__(self, *args, **kwargs):
        super(OrdersForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['payment'].initial = self.instance.payment