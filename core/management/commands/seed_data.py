from datetime import date

from django.core.management.base import BaseCommand

from core.models import Experience, Project, Skill


class Command(BaseCommand):
    help = "Popula o banco de dados com informações iniciais para o portfólio."

    def handle(self, *args, **options):
        self._seed_skills()
        self._seed_experiences()
        self._seed_projects()
        self.stdout.write(self.style.SUCCESS("Dados iniciais criados com sucesso!"))
        self.stdout.write(
            "Acesse /admin/ para editar ou substituir esses dados pelos seus."
        )

    def _seed_skills(self):
        skills = [
            ("Python", Skill.Category.LINGUAGEM, 5, 1),
            ("Django", Skill.Category.LINGUAGEM, 4, 2),
            ("SQL", Skill.Category.LINGUAGEM, 5, 3),
            ("JavaScript", Skill.Category.LINGUAGEM, 3, 4),
            ("Automação de e-mails", Skill.Category.DADOS, 5, 1),
            ("Power BI", Skill.Category.DADOS, 4, 2),
            ("Excel avançado", Skill.Category.DADOS, 4, 3),
            ("ETL / Pandas", Skill.Category.DADOS, 4, 4),
            ("Git & GitHub", Skill.Category.FERRAMENTA, 4, 1),
            ("VS Code", Skill.Category.FERRAMENTA, 5, 2),
            ("Linux", Skill.Category.FERRAMENTA, 3, 3),
        ]
        for name, category, proficiency, order in skills:
            Skill.objects.get_or_create(
                name=name,
                defaults={"category": category, "proficiency": proficiency, "order": order},
            )

    def _seed_experiences(self):
        Experience.objects.get_or_create(
            company="Prosegur",
            role="Analista de Dados",
            defaults={
                "location": "Brasil",
                "start_date": date(2024, 1, 1),
                "end_date": None,
                "is_current": True,
                "order": 1,
                "description": (
                    "Atuo na análise de dados e na automação de processos, com foco "
                    "no desenvolvimento de rotinas em Python para geração e disparo "
                    "automático de relatórios por e-mail. Isso eliminou tarefas "
                    "manuais repetitivas e aumentou a confiabilidade das entregas "
                    "para as áreas internas."
                ),
            },
        )
        Experience.objects.get_or_create(
            company="Autônomo",
            role="Desenvolvedor Freelancer",
            defaults={
                "location": "Remoto",
                "start_date": date(2021, 1, 1),
                "end_date": date(2023, 12, 1),
                "is_current": False,
                "order": 2,
                "description": (
                    "Desenvolvimento de sistemas e sites sob demanda para clientes "
                    "diversos, atuando em todas as etapas do projeto: levantamento "
                    "de requisitos, desenvolvimento, testes e entrega final."
                ),
            },
        )

    def _seed_projects(self):
        projects = [
            (
                "Automação de Relatórios por E-mail",
                (
                    "Script em Python que gera relatórios a partir de bases de dados "
                    "e os envia automaticamente por e-mail aos destinatários certos, "
                    "no horário certo, eliminando o trabalho manual repetitivo."
                ),
                "Python, Pandas, SMTP, Agendamento",
                True,
                1,
            ),
            (
                "Dashboard de Indicadores",
                (
                    "Painel interativo para acompanhamento de indicadores de negócio, "
                    "com atualização automática a partir de planilhas e bancos de dados."
                ),
                "Power BI, SQL, ETL",
                True,
                2,
            ),
            (
                "Site Institucional sob Demanda",
                (
                    "Site desenvolvido como freelancer para um cliente, do zero ao "
                    "deploy, incluindo formulário de contato e painel administrativo."
                ),
                "Django, HTML, CSS, JavaScript",
                False,
                3,
            ),
        ]
        for title, description, tags, featured, order in projects:
            Project.objects.get_or_create(
                title=title,
                defaults={
                    "description": description,
                    "tags": tags,
                    "featured": featured,
                    "order": order,
                },
            )
