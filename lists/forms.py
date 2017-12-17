from django import forms
from lists.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"

class ItemForm(forms.models.ModelForm):
    
    class Meta:
        model = Item                    # specify for which model id the form
        fields = ('text',)              # specify which fields we want it to use
        widgets = {
                'text': forms.fields.TextInput(attrs={
                    'placeholder': 'Enter a to-do intem',
                    'class': 'form-control input-lg',
                }),
        }
        error_messages = {
                'text': {'required': EMPTY_ITEM_ERROR}
        }

    item_text = forms.CharField(
            widget=forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg',
            }),
    )
