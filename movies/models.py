from django.db import models
class Genre(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return self.name

class Format(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return self.name

class Cinema(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return self.name

class Cast(models.Model):
    cast_name_english = models.CharField(max_length=255,blank=True, null=True)
    cast_name_arabic = models.CharField(max_length=255,blank=True, null=True)
    cast_role_english = models.CharField(max_length=255,blank=True, null=True)
    cast_role_arabic = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return f"{self.cast_name_english} - {self.cast_role_english}"

class Crew(models.Model):
    crew_name_english = models.CharField(max_length=255,blank=True, null=True)
    crew_name_arabic = models.CharField(max_length=255,blank=True, null=True)
    crew_role_english = models.CharField(max_length=255,blank=True, null=True)
    crew_role_arabic = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return f"{self.crew_name_english} - {self.crew_role_english}"


class Movie(models.Model):
    movienain= models.CharField(max_length=255,blank=True, null=True)
    movienaar= models.CharField(max_length=255,blank=True, null=True)
    redate=models.DateField(max_length=15,blank=True, null=True)
    tedate=models.DateField(max_length=15,blank=True, null=True)
    mduration= models.CharField(max_length=255,blank=True, null=True)
    mdiscription= models.CharField(max_length=255,blank=True, null=True)
    mdiscriptionar= models.CharField(max_length=255,blank=True, null=True)
    Rating= models.CharField(max_length=255,blank=True, null=True)
    trailer= models.CharField(max_length=255,blank=True, null=True)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE , null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE , null=True)
    format = models.ForeignKey(Format, on_delete=models.CASCADE , null=True)
    casts = models.ManyToManyField(Cast, related_name='movies' )
    crews = models.ManyToManyField(Crew, related_name='movies' )

    def __str__(self):
        return f"{self.cinema} - {self.genre} - {self.language} - {self.format}"
    

# Create your models here.
