from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser

class Projeto(models.Model):
    nome = models.CharField(name = "nome", max_length = 200)
    def __str__(self):
        return (self.nome)

class ProjetoUsuario(models.Model):
    usuario = models.ForeignKey(User, default='')
    projeto = models.ForeignKey('Projeto')
    def __str__(self):
        return (self.usuario)

class Tarefa(models.Model):
    nome = models.CharField(name = "nome", max_length = 200)
    dataEHoraDeInicio = models.DateTimeField(name = "Data e Hora de Inicio", default = timezone.now)
    usuario = models.ForeignKey(User, default='')
    projeto = models.ForeignKey('Projeto')
    def __str__(self):
        return (self.nome)
# Create your models here.
