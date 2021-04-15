from django.shortcuts import render
from basicapp import forms

# Create your views here.


def index(req):
    return render(req, 'index.html')


def form_name_view(req):
    form = forms.FormBasic()

    if req.method == 'POST':
        form = forms.FormBasic(req.POST)

        if form.is_valid():
            print("validation success")
            print("NAME" + form.cleaned_data['name'])
            print("EMAIL" + form.cleaned_data['email'])
            print("TEXT" + form.cleaned_data['text'])

    return render(req, 'form.html', {'form': form})
