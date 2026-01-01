from django.db import models

class Mensagem(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now=True)

    def __stf__(self):
        return f"{self.nome} - {self.email}"