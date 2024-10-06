from django import forms

class ValuationForm(forms.Form):
    revenue = forms.FloatField(label='Revenue', min_value=0)
    ebitda = forms.FloatField(label='EBITDA', min_value=0)
    growth_rate = forms.FloatField(label='Growth Rate', min_value=0, max_value=1)
    current_price = forms.FloatField(label='Current Price', min_value=0)
