from django import forms

class ReviewForm(forms.Form):
  user_name=forms.CharField(label='Your Name',max_length=100,error_messages={
    'required':'your name must not be empty',
    'max_length':'please enter a shorter name'
  })
  