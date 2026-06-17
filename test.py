from django.core.mail import send_mail

send_mail(
    "Teste SMTP",
    "Funcionando!",
    None,
    ["seuemail@gmail.com"],
    fail_silently=False
)