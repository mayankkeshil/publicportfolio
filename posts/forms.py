from django import forms
from .models import Post

class PostForm(forms.ModelForm): # PostForm inherits features of forms.ModelForm
    class Meta: # Tells Django all the data to be in the form
        model = Post # Tells Django all the data submitted will be linked to Post object
        fields = ['title', 'content', 'featured_image', 'alt_text'] # Says all the fields that will be included in the form
    def clean(self):
        cleaned_data = super().clean()
        featured_image = cleaned_data.get('featured_image')
        alt_text = cleaned_data.get('alt_text')
        if featured_image and not alt_text: 
            raise forms.ValidationError("You must provide alt text for an image.")