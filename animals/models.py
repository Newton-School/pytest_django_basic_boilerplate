from django.db import models


class Animal(models.Model):
  name = models.CharField(max_length=255)
  sound = models.CharField(max_length=255)

  def speak(self):
    # Complete this function.
    # It should return a string `The {name} says "{sound}"`
    return f''