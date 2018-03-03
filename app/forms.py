from django import forms

# A view handling form -- this will recieve the file data
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()