from django import forms
from .models import TransactionModel


class TransactionForm(forms.Form):
    sen_account = forms.CharField(label='From Account', max_length=100)
    rec_account = forms.CharField(label='To Account', max_length=100)
    amount = forms.FloatField(label='Amount', min_value=0)
    message = forms.CharField(label='Message', max_length=500, required=False)


    class Meta:
        model = TransactionModel
        fields = ["sen_account", "rec_account", "amount", "message"]




