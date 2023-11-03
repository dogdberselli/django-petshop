from django.db import models

class Contato(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=50)
    email = models.EmailField(verbose_name='E-mail')
    mensagem = models.CharField(verbose_name='Mensagem', max_length=3000)
    data = models.DateTimeField(verbose_name='Data Envio', auto_now_add=True)
    lido = models.BooleanField(verbose_name='Lido', default=False, blank=True)
    def __str__(self):
        return f'{self.nome} [{self.email}]'
    class Meta:
        verbose_name = 'Formulário de Contato'
        verbose_name_plural = 'Formulários de Contatos'
        ordering = ['-data']

class Reserva(models.Model):
    nome_pet = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    data_reserva = models.DateField()
    observacoes = models.CharField(max_length=3000)

# Create your models here.
