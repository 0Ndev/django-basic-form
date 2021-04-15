from django import forms
from django.core import validators


# build-in-validation
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("NAME NEEDS TO START WITH Z")


class FormBasic(forms.Form):
    name = forms.CharField()
    # name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    # valid email
    verify_email = forms.EmailField(label='enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.ChoiceField(required=False,
                                   widget=forms.HiddenInput,
                                   validators=[
                                       validators.MaxLengthValidator(0)]
                                   )

    # custom valid form
    def clean(self):
        all_clean_date = super().clean()
        email = all_clean_date['email']
        vmail = all_clean_date['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILs MATCH")

    # botcatcher
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT")
