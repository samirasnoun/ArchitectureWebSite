# -*- coding: utf8 -*- 
from django.db import models  
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from fields import ThumbnailImageField
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.conf import settings
from tinymce.models import HTMLField
 
"""
def get_aticle_default():
    return Article.objects.get(id=1)
"""

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = ThumbnailImageField(upload_to='', blank=True)
    content = HTMLField()
    
    
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    def __unicode__(self):
        return 'Profile for user {}'.format(self.user.username)

class Image(models.Model):
    AFFI_PAGE_ACCUEIL = (
        ('oui', 'Afficher dans la page Home'),
        ('non', 'Ne pas l afficher dans la page Home'),
    )
    
    title = models.CharField(max_length=100)
    photo =  ThumbnailImageField(upload_to='')
    caption = models.CharField(max_length=250, blank=True)
    afficher = models.CharField(max_length=3, choices=AFFI_PAGE_ACCUEIL, default='oui')

    class Meta:
        ordering = ['title']

    def affiche(self):
        return self.afficher == 'oui'

    def get_chantier(self):
        return  ImagesDe.objects.filter(image=self)[0].chantier

    def get_media(self):
        return ImagesDe.objects.filter(image=self)[0].media

    
    def __unicode__(self):
        return self.title

    def get__absolute_url(self):        
        return str(self.photo)

    def get_url(self):
        return "/images/"  + str(self.id) 

    def get_images_media(self):
        return Image.objects.filter(media=self)  

    def get_thumb(self):        
        return str(self.photo).replace('.jpg' , '.thumb.jpg')

# Projet 
class Chantier(models.Model): 
    NIVEAU1 = (

        ('ARCHITE', 'Architecture'),
        ('AMEURBA', 'Aménagement'),
        ('DESIGN', 'Design'),
        ('URBAPAY', 'Urbanisme et paysages'),

    )
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)   
    date = models.DateField()
    text = models.TextField(max_length=500)
    images = models.ManyToManyField(Image, through='ImagesDe', blank=True, null=True)
    niveau1 = models.CharField(max_length=7, choices=NIVEAU1, default='ARCHITE')

    def get_absolute_url(self):
        return reverse('projet-view', kwargs={'pk2': self.pk})

    def get_niveaux(self):
        return self.NIVEAU1
    
    def get_images_chantier(self):
        return Image.objects.filter(chantier=self)  
    
    def get_niveau(self):
        return self.niveau1 

    def get_niveau_v(self):
        for k in self.NIVEAU1:
            if(k[0]==self.niveau1):
                return k[1]
        return self.niveau1 

    def get_resume(self):
        return self.text     
    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"

    def __unicode__(self):
        return self.title   

# Art et Artisanat
class Media(models.Model):
   
    
    NIVEAU1 = (
        ('EXPO', 'Exposition'),
        ('PUBLI', 'Publications'),
        ('ARTICL', 'Articles'),
    )

    title = models.CharField(max_length=250)
    date = models.DateField()
    text = models.TextField(max_length=500)
    images = models.ManyToManyField(Image, through='ImagesDe', blank=True, null=True)
    niveau1 = models.CharField(max_length=7, choices=NIVEAU1, default='ARTICL')

    class Meta:
        verbose_name = "Arts et Artisanat"
        verbose_name_plural = "Arts et Artisanat"

    def get_images_media(self):
        return Image.objects.filter(media=self) 

    def get_niveaux(self):
        return self.NIVEAU1

    def get_niveau(self):
        return self.niveau1

    def get_niveau_v(self):
        for k in self.NIVEAU1:
            if(k[0]==self.niveau1):
                return k[1]
        return self.niveau1 

    def get_resume(self):
        return self.text 
    
    def get_absolute_url(self):
        return reverse('media-view-detail', kwargs={'pk3': self.pk})

    def __unicode__(self):
        return self.title 
        
  

# Relation image / projet  ou art et artisanat
class ImagesDe(models.Model):
    image = models.ForeignKey(Image, blank=True)
    chantier = models.ForeignKey(Chantier, blank=True, null=True)
    media = models.ForeignKey(Media, blank=True, null=True)
    def __unicode__(self):
        if self.chantier :
            return "Photo : " + self.image.title + " du chantier : " + self.chantier.title
  
        if self.media :
            return "Photo : " + self.image.title + " du media : " + self.media.title    




#class non utilisee
class Contact(models.Model):
    nameField = models.CharField(max_length=255)
    firstNameField = models.CharField(max_length=255)
    descField = models.TextField(max_length=500)
    phoneField = models.CharField(max_length=14, default='')
    emailField = models.EmailField()
    def __unicode__(self):
        return    (str(self.nameField)).upper() + "  " +  str(self.firstNameField)





"""
contact non utilisee
"""

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
   pass  


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'caption', 'afficher')
    search_fields = ('title',)


class ImagesInline(admin.TabularInline):
    model = Chantier.images.through


class ImageInline(admin.ModelAdmin):
    inlines = [
        ImagesInline,
    ]

       
@admin.register(Chantier)
class ChantierAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInline,
    ]
    exclude = ('produit', 'media', )


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInline,
    ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','date_of_birth', 'photo', 'content',)