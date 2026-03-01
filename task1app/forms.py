from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date"]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter task title"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Enter description (optional)"
            }),
            "due_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
        }

    #  Extra safety validation (small but professional)
    def clean_title(self):
        title = self.cleaned_data.get("title")

        if not title or title.strip() == "":
            raise forms.ValidationError("Title cannot be empty.")

        return title.strip()