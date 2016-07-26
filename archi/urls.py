# -*- coding: utf8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from website.views import *
#from website.sitemap import *
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import ChantierSitemap, MediaSitemap,  StaticViewSitemap


sitemaps = { 'chantiers': ChantierSitemap, 'medias':MediaSitemap, 'static': StaticViewSitemap,}


urlpatterns = patterns('', 
    
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$' ,'website.views.index4', name='index'),
    
    url(r'^profil/$' ,Profil.as_view(), name='profil'),
    url(r'^profile/$', ProfileDetail.as_view(), name='profile-view', ),
    # url(r'^projets/$' ,'website.views.index_chantier_selection', name='index'),
    url(r'^projets/$' ,'website.views.index_projets', name='index'),
    # url(r'^projets/(?P<code_projet>\w+)/$' ,'website.views.index_chantier_selection', name='index_chantier_selection'),
    url(r'^projet/(?P<pk2>\w+)/$', ProjetcDetail.as_view(), name='projet-view', ),    

    url(r'^artsetartisanats/$', 'website.views.index_ArtsArtisanat', name='media-view', ),
    url(r'^artsetartisanats/(?P<code_projet>\w+)/$' ,'website.views.index_media_selection', name='index_media_selection'),
    url(r'^artsetartisanat/(?P<pk3>\w+)/$', MediaDetail.as_view(), name='media-view-detail', ),

    url(r'^images/(?P<pk>\d+)/$', ImageView.as_view(), name='image-view',),

    url(r'^contact/$', 'website.views.contact', name='contact',),
    url(r'^tinymce/', include('tinymce.urls')),

    (r'^sitemap\.xml', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

 

    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# sitemaps = {
#  'Chantier':ChantierSitemap,
#  'site':Sitemap(['name_of_url', 'name_of_url']),
# }