from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    defaults = models.TextField()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class DefaultPerson(models.Model):
    first_name = models.CharField(max_length=100, default="Anonymous")


class ManualPrimaryKeyTest(models.Model):
    id = models.IntegerField(primary_key=True)
    data = models.CharField(max_length=100)


class Profile(models.Model):
    person = models.ForeignKey(Person, primary_key=True)


class Tag(models.Model):
    text = models.CharField(max_length=255, unique=True)


class Thing(models.Model):
    name = models.CharField(max_length=256)
    tags = models.ManyToManyField(Tag)


class Publisher(models.Model):
    name = models.CharField(max_length=100)


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, related_name='books', db_column="publisher_id_column")
