from app.core import forms


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=150, required=True,
                              widget=forms.Textarea,)
    """widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'type':'text',
            'id':'commentArea',
            'rows':'3',
            'placeholder':'Add comment',
            'required':"required",
       }
   ),
       error_messages = {
               'required' : "This field is required",
           'invalid' : "This field is invalid",
   })"""
