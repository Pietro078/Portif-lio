from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        labels = {
            "name": "Nome",
            "email": "E-mail",
            "message": "Mensagem",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Seu nome", "class": "form-input"}
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "seu@email.com", "class": "form-input"}
            ),
            "message": forms.Textarea(
                attrs={"placeholder": "Sua mensagem...", "class": "form-input", "rows": 5}
            ),
        }
