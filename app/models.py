from django.db import models

class Partido(models.Model):
	nombre_partido = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre_partido

class Team(models.Model):
	partido = models.ManyToManyField(Partido)
	codigo_equipo = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=200, blank=True)
	logo = models.ImageField(blank=True, null=True, upload_to="image_team/")

	def __str__(self):
		return self.nombre

class Player(models.Model):
	team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=200)
	apodo = models.CharField(max_length=200)
	fecha_nacimiento = models.DateField()
	edad = models.IntegerField()
	rut = models.CharField(max_length=12)
	email = models.EmailField()
	estatura = models.DecimalField(max_digits=5, decimal_places=2)
	peso = models.DecimalField(max_digits=5, decimal_places=2)
	fotografia = models.ImageField(blank=True, null=True, upload_to="image_player/")
	Base = "Base"
	Escolta = "Escolta"
	Alero = "Alero"
	Ala_pivot = "Alero-pivot"
	Pivot = "Pivot"
	posicion_opciones = (
		(Base, 'Base'),
		(Escolta, 'Escolta'),
		(Alero, 'Alero'),
		(Ala_pivot, 'Ala-pivot'),
		(Pivot, 'Pivot'),
	)
	posicion = models.CharField(max_length=200, choices=posicion_opciones, default=Base)

	def __str__(self):
		return self.nombre

class Coach(models.Model):
	team = models.OneToOneField(Team, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=200)
	edad = models.IntegerField()
	email = models.EmailField()
	rut = models.CharField(max_length=12)
	apodo = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre