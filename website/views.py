# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from website.models import  Image, Chantier, Media, Profile
from django.views.generic import DetailView, ListView, TemplateView
from website.forms import ContactFeedForm, ContactForm, Contact2Form
from django.core.mail import send_mail
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext, loader
from django.core.mail import mail_managers, mail_admins 
from django.http import Http404
from itertools import chain 

  

# Create your views here.

#Mosaique Projets
def index_projets(request):
    images =[]
    try:
        chantiers = Chantier.objects.all()
        #chantiers = get_list_or_404(Chantier)
    except Chantier.DoesNotExist:
        raise Http404
    
    for m in chantiers:
        ims = m.get_images_chantier()
        for im in ims:            
            if (im.afficher == 'oui' and im not in images):
                images.append(im)

    return render_to_response('index3.html', {"images": images,  "niveaux": Chantier.NIVEAU1 } )







#Mosaique Art et Artisanat 
# def ArtsArtisanat(request):
#     tuple_images =[]
#     medias = Media.objects.all()
    
#     for m in medias:
#         ims = m.get_images_media()
#         for im in ims:            
#             if (im.afficher == 'oui'):
#                 tuple_images.append(im)

#     return render_to_response('index_ArtsArtisanat.html', {"images_list": tuple_images } )




def index_chantier_selection(request, code_projet):
    if code_projet:
        print '++++++++++++'
        chantiers = Chantier.objects.filter(niveau1=code_projet)
        tuple_images =[]
        for ch in chantiers:
            ims = ch.get_images_chantier()
            for i in ims:
                if (i.affiche()):
                    tuple_images.append(i)

        return render_to_response('index2.html', {"images_list": tuple_images } )

    else:
        print '----------------------'
        pass

    return render_to_response('index3.html', {"images_list": Image.objects.filter(afficher='oui') } )




def index4(request):
    
    images =[]
    try:
        chantiers = Chantier.objects.all()
        
        for ch in chantiers:
            ims = ch.get_images_chantier()
            for i in ims:
                if (i.affiche() and not i in images):
                    images.append(i)
        
       
        
          

    except Chantier.DoesNotExist:
        raise Http404

    try:
        medias = Media.objects.all()
        
        for md in medias:
            ims = md.get_images_media()
            for i in ims:
                if (i.affiche() and not i in images):
                    images.append(i)
    except Media.DoesNotExist:
        raise Http404
  
  
    return render_to_response('index3.html', {"images": images, "niveaux": Chantier.NIVEAU1 + Media.NIVEAU1} )




def index_ArtsArtisanat(request):

    images =[]
    try:
        medias = Media.objects.all()
        
        for md in medias:
            ims = md.get_images_media()
            for i in ims:
                if (i.affiche()):
                    images.append(i)
    except Media.DoesNotExist:
        raise Http404
    return render_to_response('index3_artsartisanat2.html', {"images": images, "niveaux": Media.NIVEAU1} )
















def index_media_selection(request, code_projet):
    if code_projet:
        
        medias = Media.objects.filter(niveau1=code_projet)
        tuple_images =[]
        for md in medias:
            ims = md.get_images_media()
            
            for i in ims:
                if (i.affiche()):
                    tuple_images.append(i)
                    
                    
        return render_to_response('index_ArtsArtisanat.html', {"images_list": tuple_images } )
    else:
        pass
    return render_to_response('index_ArtsArtisanat.html', {"images_list": Image.objects.filter(afficher='oui') } )






#Mosaique 
def Produits(request):
    return render_to_response('index_produits.html', {"produits_list": Image.objects.filter(afficher='oui') } )

def index2(request):
    return render_to_response('index2.html')


class Profil(TemplateView):
    template_name = 'profile2.html'



class ProfileDetail(TemplateView):
    template_name = 'profile2.html'    
    model = Profile
    def get_context_data(self, **kwargs):
        context = super(ProfileDetail, self).get_context_data(**kwargs)
        context['profiles'] = Profile.objects.all()
        print '+++++++++++++'
        print context
        return context
        

class ProjetcDetail(TemplateView):
    template_name = 'chantier_detail3.html'
    model = Chantier
    def get_context_data(self, **kwargs):
        context = super(ProjetcDetail, self).get_context_data(**kwargs)
        context['projet'] = Chantier.objects.get(id=self.kwargs['pk2'])
        print '-----------'
        return context





class MediaDetail(TemplateView):
    template_name = 'media_detail.html'
    model = Chantier
    def get_context_data(self, **kwargs):
        context = super(MediaDetail, self).get_context_data(**kwargs)
        
        context['media'] = Media.objects.get(id=self.kwargs['pk3'])
        return context





class ChantierView(DetailView):
    template_name = 'chantier_detail2.html'
    model = Chantier
    def get_context_data(self, **kwargs):
        
        context = super(ChantierView, self).get_context_data(**kwargs)
        
        context['chantier_list'] = Chantier.objects.all()
        context['count'] = Chantier.objects.all().count()
        context['chantier'] = Chantier.objects.get(id=2)

        return context

class ImageView(DetailView):
    template_name = 'image_detail.html'
    model = Image    
    context_object_name = 'image'

"""

view ok avec l'url 
url(r'^contactfeed/$', 'website.views.contactFeed', name='contactfeed',),

"""
def contactFeed(request):    
    if request.method == 'POST':
        form = ContactFeedForm(request.POST)
        if form.is_valid():
            
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']

            #send_mail('Feedback from your site, topic: %s' % topic,message, sender,['samir.asnoun@gmail.com'])
            
            #mail_managers(topic + " from " + sender, message, fail_silently=False, connection=None, html_message=None)
            
            if topic and message and sender:
                try:
                    mail_admins(topic + " from " + sender, message, fail_silently=False, connection=None, html_message=None)
                    
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                
                return render_to_response('thanks.html')            
            else:
            # In reality we'd use a form class
            # to get proper validation errors.
                return HttpResponse('Make sure all fields are entered and valid.')        

        else:
            return render(request, 'contactfeedform.html', {'form': form})
    else:
        
        form = ContactFeedForm()
        return render(request, "contactfeedform.html", {'form': form })



"""
view ok avec l'url url(r'^contact/$', 'website.views.contact', name='contact',),
"""
def contact(request): 
    t = 'contact2.html' 
    if request.method == 'POST':
        form = Contact2Form(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nameField']
            prenom = form.cleaned_data['firstNameField']
            email = form.cleaned_data['emailField']
            telephone = form.cleaned_data['phoneField']
            description = form.cleaned_data['descField']

            #send_mail('Feedback from your site, topic: %s' % topic,message, sender,['samir.asnoun@gmail.com'])
            #mail_managers(topic + " from " + sender, message, fail_silently=False, connection=None, html_message=None)
            
            if nom and prenom and email:
                try:
                    
                    mail_admins("from " + prenom + "  " + nom, "nom" +  nom + "\nprenom = " + prenom + "\ndescription = " + description + "\nphone=" +  telephone + "\nemail = "  + email , fail_silently=False, connection=None, html_message=None)
                    form.save()  
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                
                return render_to_response('thanks.html' , {'prenom': prenom} )            
            else:
                return render(request, t, {'form': form })
        else:
            

            return render(request, t, {'form': form })
    else:
        
        form = ContactForm()
        return render(request, t, {'form': form })




"""

view en test l'url url(r'^contact2/$', 'website.views.contact2', name='contact2',),

    nameField = models.CharField(max_length=255)
    firstNameField = models.CharField(max_length=255)
    descField = models.TextField(max_length=500)
    #phoneField = models.CharField(max_length=14)
    emailField = models.EmailField()


"""
def contact2(request):   
    t = 'contact2.html' 
    if request.method == 'POST':
        form = Contact2Form(request.POST)
       
        if form.is_valid():
            nameField = form.cleaned_data['nameField']
            firstNameField = form.cleaned_data['firstNameField']
            descField = form.cleaned_data['descField']
            emailField = form.cleaned_data['emailField']

            #send_mail('Feedback from your site, topic: %s' % topic,message, sender,['samir.asnoun@gmail.com'])
            
            #mail_managers(topic + " from " + sender, message, fail_silently=False, connection=None, html_message=None)
            
            if nameField and firstNameField and descField:
             
                #mail_admins(topic + " from " + sender, message, fail_silently=False, connection=None, html_message=None)
                mail_admins("from " + prenom + "  " + nom, "nom" +  nom + "prenom = " + prenom + "description = " + description + " phone=" +  telephone + "email = "  + email , fail_silently=False, connection=None, html_message=None)
                form.save()  
                return render_to_response('thanks.html')            
            else:
                return HttpResponse('Make sure all fields are entered and valid.')        

        else:
            return render(request, t, {'form': form})
    else:
        form = Contact2Form()
        return render(request, t, {'form': form })




