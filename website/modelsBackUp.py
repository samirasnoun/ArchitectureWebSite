from django.db import models
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from fields import ThumbnailImageField

"""
class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
    	ordering = ['name']

    def __unicode__(self):
    	return self.name

    @models.permalink
    def get__absolute__url(self):
    	return("item_detail",None, {'object_id':self.id} ) """


class Address(models.Model):
    number = models.CharField(_('Number'), max_length = 30, blank = True)
    street_line1 = models.CharField(_('Address 1'), max_length = 100, blank = True)
    street_line2 = models.CharField(_('Address 2'), max_length = 100, blank = True)
    zipcode = models.CharField(_('ZIP code'), max_length = 5, blank = True)
    city = models.CharField(_('City'), max_length = 100, blank = True)
    country = models.CharField(_('Country'), max_length = 100, blank = True)

    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adresses"
        ordering = ['country']

    def __unicode__(self):
        return self.number + " " + self.street_line1  + " " + self.zipcode + " " + self.city + " " + self.country.upper() 

class Article(models.Model): 
  #  id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=250)
  #  address = models.ForeignKey(Address)
    date = models.DateField()
    text = models.TextField(max_length=500)
  
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title   

"""
def get_aticle_default():
    return Article.objects.get(id=1)
"""

class Photo(models.Model):
 #   item = models.ForeignKey(Item)
#    photos_id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article)
    title = models.CharField(max_length=100)
    photo =  ThumbnailImageField(upload_to='photos')
    caption = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title

    @models.permalink 
    def get__absolute_url():
        return ('photo_detail', None , {'object_id': self.id})





class Auteur(models.Model):
    nom = models.CharField(max_length=50, blank=True)

class Livre(models.Model):
    titre = models.CharField(max_length=50,blank=True)
    auteur = models.ForeignKey(Auteur)

class LivreInLine(admin.StackedInline):
    model = Livre

@admin.register(Auteur)
class AuteurAdmin(admin.ModelAdmin):
    inlines = [LivreInLine,]




class PhotoInline(admin.StackedInline):
    model = Photo
#    raw_id_fields = ("article",)

#class ItemAdmin(admin.ModelAdmin):
#    inlines = [PhotoInline,]

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
   inlines = [PhotoInline,]

@admin.register(Address, Photo)
class AdressAdmin(admin.ModelAdmin):
   pass        

