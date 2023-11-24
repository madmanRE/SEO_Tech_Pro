from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = (
            "category",
            "title",
            "slug",
            "image",
            "text",
            "is_active",
        )


class SearchForm(forms.Form):
    query = forms.CharField()
