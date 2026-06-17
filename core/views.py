from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactForm
from .models import Experience, Project, Skill

# Edite estas informações com os seus dados reais.
OWNER = {
    "name": "Pietro Scatine Traverso",
    "role": "Desenvolvedor & Analista de Dados",
    "tagline": "Transformo dados em decisões e tarefas manuais em automações.",
    "location": "Brasil",
    "email": "pietro.s.thor@gmail.com",
    "github": "https://github.com/seu-usuario",
    "linkedin": "https://www.linkedin.com/in/seu-usuario",
}


def _group_skills_by_category(skills):
    grouped = {}
    for skill in skills:
        grouped.setdefault(skill.get_category_display(), []).append(skill)
    return grouped


def _send_contact_notification(contact):
    """Envia um e-mail avisando que uma nova mensagem chegou pelo site.

    Se o e-mail de destino (CONTACT_EMAIL) não estiver configurado, ou se o
    envio falhar por qualquer motivo (ex: credenciais erradas), a mensagem
    já está salva no banco e visível em /admin/ — então não interrompemos
    a navegação do visitante por causa disso.
    """
    if not settings.CONTACT_EMAIL:
        return

    email = EmailMessage(
        subject=f"Novo contato pelo site — {contact.name}",
        body=(
            f"Você recebeu uma nova mensagem pelo formulário de contato do site.\n\n"
            f"Nome: {contact.name}\n"
            f"E-mail: {contact.email}\n\n"
            f"Mensagem:\n{contact.message}"
        ),
        from_email=settings.DEFAULT_FROM_EMAIL or "no-reply@portfolio.local",
        to=[settings.CONTACT_EMAIL],
        reply_to=[contact.email],
    )
    try:
        email.send(fail_silently=False)
    except Exception:
        # Em produção, troque por logging.exception(...) para investigar
        # falhas de envio (credenciais inválidas, provedor bloqueando, etc.).
        pass


def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            _send_contact_notification(contact)
            messages.success(
                request, "Mensagem enviada com sucesso! Em breve eu respondo."
            )
            return redirect(f"{reverse('core:home')}#contato")
        messages.error(
            request, "Não foi possível enviar sua mensagem. Verifique os campos abaixo."
        )
    else:
        form = ContactForm()

    skills = Skill.objects.all()

    context = {
        "owner": OWNER,
        "experiences": Experience.objects.all(),
        "projects": Project.objects.all(),
        "skills_by_category": _group_skills_by_category(skills),
        "form": form,
    }
    return render(request, "core/home.html", context)
