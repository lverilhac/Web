from django.db import models

class Client(models.Model):
    login = models.CharField(max_length=10)
    passwd = models.CharField(max_length=10)


    

    def __str__(self):

        """ 

        Cette méthode que nous définirons dans tous les modèles

        nous permettra de reconnaître facilement les différents objets que 

        nous traiterons plus tard et dans l'administration

        """

        return self.login