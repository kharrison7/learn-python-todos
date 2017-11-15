from django import forms

#inherits Form from forms, imported above
class BMIForm(forms.Form):
    # for more on forms, check out python forms documentation
    """
    Height is in meters. Weight is in Kg.
    """
    name = forms.CharField(required=False)
    height = forms.FloatField(label="Height in meters", required=True, min_value=0)
    weight = forms.FloatField(required=True, min_value=0)
