from django import forms
from .models import BookReview

class BookReviewForm(forms.ModelForm):

    star_given = forms.IntegerField(min_value=1,max_value=5)
    class Meta:
        model = BookReview
        fields = ['commit','star_given']

        widgets = {
            'star_given':forms.NumberInput(attrs={
                'class':'input',
                'placeholder':'Star',
            }),
            'commit':forms.Textarea(attrs={
                'class':'input',
                'placeholder':'Commit'
            })
        }
