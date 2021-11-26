from django.forms import ModelForm, TextInput, Textarea, CheckboxInput

from product.models import Variant


class VariantForm(ModelForm):
    class Meta:
        model = Variant
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'active'})
        }
