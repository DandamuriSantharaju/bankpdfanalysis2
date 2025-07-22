from django import forms

class PDFUploadForm(forms.Form):
    pdf = forms.FileField(label="Upload PDF")
    password = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Optional PDF Password'}))
    keyword = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Filter keyword'}))
