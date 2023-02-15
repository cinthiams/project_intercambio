from django.db import models

# Create your models here.
class Base(models.Model):
  publicacao = models.DateTimeField(auto_now_add=True)
  atualização = models.DateTimeField(auto_now=True)
  ativo = models.BooleanField(default=True)
  
  class Meta:
    abstract = True 
    
class User(Base):
  pass

class Dados(Base):
  #user = models.forekey
  euro = models.DecimalField(max_digits=2,decimal_places=1)
  real_valor = models.DecimalField(max_digits=2,decimal_places=1)
  taxas = models.DecimalField(max_digits=2,decimal_places=1)
  comprovacao_valor = models.DecimalField(max_digits=2,decimal_places=1)
  passagem = models.DecimalField(max_digits=2,decimal_places=1)
  acomodação = models.DecimalField(max_digits=2,decimal_places=1)
  class Meta:
    verbose_name ='Dados'
  
  
  
  
  
  