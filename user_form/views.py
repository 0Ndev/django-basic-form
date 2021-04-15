from basicapp.views import index
from django.shortcuts import render
from user_form.forms import NewUserForm


def users(req):
    form = NewUserForm()
    if req.method == 'POST':
        form = NewUserForm(req.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(req)
        else:
            print("ERROR form invalid")

    return render(req, 'user.html', {'form': form})
