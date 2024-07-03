from django import forms
from myapp1.models import OrderItems, Item


class OrderItemForm(forms.ModelForm):

    class Meta:
        model = OrderItems
        fields = ('items', 'client', 'number_of_items')
        widgets = {
            'client': forms.RadioSelect(attrs={"class": "form__input"}),
        }
        labels = {'client': 'ClientName', 'number_of_items': 'Quantity'}


class InterestedForm(forms.Form):
    CHOICES = [
        ('0', 'No'),
        ('1', 'Yes'),
    ]
    interested = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
    quantity = forms.IntegerField(min_value=1)
    comments = forms.CharField( widget=forms.Textarea, label='Additional Comments', required=False)
    class Meta:
        model = Item
        fields = ['interested']
