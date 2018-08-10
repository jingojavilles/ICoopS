from django import forms
from .models import Client

class NewTopicForm(forms.ModelForm):
    # branch = forms.CharField(widget=forms.Textarea(), max_length=4000)
    address = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 2, 'placeholder': 'Current Address'}
            ),
        max_length=200,
        )

    class Meta:
        model = Client
        fields = ['acctid', 'fname', 'lname', 'address', 'contactnum', 'branch']
        labels = {
            'acctid' : 'Account ID',
            'fname': 'First Name',
            'lname': 'Last Name',
            'address': 'Address',
            'contactnum': 'Contact Number',
            'branch': 'Branch'
        }