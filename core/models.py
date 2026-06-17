from django.db import models


class Skill(models.Model):
    """Uma habilidade técnica exibida na seção 'Habilidades'."""

    class Category(models.TextChoices):
        LINGUAGEM = "linguagem", "Linguagens & Frameworks"
        DADOS = "dados", "Dados & Automação"
        FERRAMENTA = "ferramenta", "Ferramentas"

    name = models.CharField("nome", max_length=60)
    category = models.CharField(
        "categoria", max_length=20, choices=Category.choices, default=Category.LINGUAGEM
    )
    proficiency = models.PositiveSmallIntegerField(
        "proficiência (1 a 5)",
        default=3,
        help_text="Use um número de 1 a 5. É usado para desenhar a barrinha de nível.",
    )
    order = models.PositiveSmallIntegerField("ordem", default=0)

    class Meta:
        ordering = ["category", "order", "name"]
        verbose_name = "Habilidade"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return self.name

    @property
    def proficiency_percent(self):
        return min(max(self.proficiency, 0), 5) * 20


class Experience(models.Model):
    """Um item da linha do tempo de experiência profissional."""

    company = models.CharField("empresa", max_length=120)
    role = models.CharField("cargo", max_length=120)
    location = models.CharField("local", max_length=120, blank=True)
    start_date = models.DateField("data de início")
    end_date = models.DateField("data de término", null=True, blank=True)
    description = models.TextField("descrição")
    is_current = models.BooleanField("é o emprego atual", default=False)
    order = models.PositiveSmallIntegerField(
        "ordem", default=0, help_text="Menor número aparece primeiro na linha do tempo."
    )

    class Meta:
        ordering = ["order", "-start_date"]
        verbose_name = "Experiência"
        verbose_name_plural = "Experiências"

    def __str__(self):
        return f"{self.role} @ {self.company}"


class Project(models.Model):
    """Um projeto exibido na seção 'Projetos'."""

    title = models.CharField("título", max_length=120)
    description = models.TextField("descrição")
    image = models.ImageField("imagem", upload_to="projetos/", blank=True, null=True)
    tags = models.CharField(
        "tags", max_length=200, blank=True, help_text="Separe as tags por vírgula. Ex: Python, Django, SQL"
    )
    link = models.URLField("link do projeto", blank=True)
    repo_link = models.URLField("link do repositório", blank=True)
    featured = models.BooleanField("destaque", default=False)
    order = models.PositiveSmallIntegerField("ordem", default=0)

    class Meta:
        ordering = ["order", "-id"]
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self):
        return self.title

    @property
    def tag_list(self):
        return [tag.strip() for tag in self.tags.split(",") if tag.strip()]


class ContactMessage(models.Model):
    """Mensagem enviada pelo formulário de contato."""

    name = models.CharField("nome", max_length=120)
    email = models.EmailField("e-mail")
    message = models.TextField("mensagem")
    created_at = models.DateTimeField("recebida em", auto_now_add=True)
    read = models.BooleanField("lida", default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Mensagem de contato"
        verbose_name_plural = "Mensagens de contato"

    def __str__(self):
        return f"{self.name} <{self.email}>"
