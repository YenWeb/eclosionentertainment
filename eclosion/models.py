from django.db import models

# Create your models here.

class Index(models.Model):
        
        name = "Caroussel Acceuil"

        titre1       = models.CharField(max_length=50)
        description1 = models.TextField()
        image1       = models.ImageField()

        titre2       = models.CharField(max_length=50)
        description2 = models.TextField()
        image2       = models.ImageField()

        titre3       = models.CharField(max_length=50)
        description3 = models.TextField()
        image3       = models.ImageField()

        def __str__(self):
            return self.name


class Project(models.Model):

      choix      = models.CharField(max_length=50)

      def __str__(self):
            return self.choix


class Categorie(models.Model):
      
      name        = models.CharField(max_length=50)
      image       = models.ImageField()
      


      def __str__(self):
            return self.name


class Film(models.Model):
      
      title       = models.CharField(max_length=50)
      description = models.TextField()
      affiche     = models.ImageField()
      categorie   = models.ForeignKey('Categorie', on_delete=models.CASCADE)
      timing      = models.ForeignKey('Project', on_delete=models.CASCADE)

      def __str__(self):
            return self.title