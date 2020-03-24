from django import forms

class LogInForm(forms.Form):
    """" """
    username = forms.CharField(max_length = 45, required = True,
    widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'type':'text',
            'placeholder':'Here...',
            'required':"required",
       }
   ),
       error_messages = {
           'required' : "This field is required",
           'invalid' : "This field is invalid",
   })

    password = forms.CharField(max_length = 45, required = True,
    widget=forms.TextInput(
        attrs = {
            'type':"password",
            'class':"form-control",
            'placeholder':"Here...",
            'required':"required",
        }
    ),
        error_messages = {
            'required' : "This field is required",
            'invalid' : "This field is invalid",
    })
    def clean(self):
        cleaned_data = super().clean()
        #Do Stuff