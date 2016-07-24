# -*- coding: utf8 -*-
#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from website.models import Item, Photo
from django.views.generic import TemplateView


urlpatterns = patterns ('', 
    (r'^$', TemplateView.as_view(template_name="index.html", 
    	
    	kwargs={ 
    	     	'extra_context': {'item_list': lambda: Item.objects.all()},
        	},
	

	))  +  patterns('django.views.generic',




	url(r'^$', 'simple.direct_to_template',
		
		kwargs={
			'template': 'index.html',
			'extra_context': {'item_list': lambda: Item.objects.all()}
		},
		
		name='index'
	),

	url(r'^items/$', 'list_detail.object_list',
	 	
	 	kwargs={
			'queryset': Item.objects.all(),
		 	'template_name': 'items_list.html',
			'allow_empty': True,
		},
		
		name='item_list'
	),
	
	url(r'^items/(?P<object_id>\d+)/$', 'list_detail.object_detail',
		
		kwargs={
			'queryset': Item.objects.all(),
			'template_name': 'items_detail.html'
		},
		
		name='item_detail'
		
	),
	
	url(r'^photos/(?P<object_id>\d+)/$', 'list_detail.object_detail',
		
		kwargs={
			'queryset': Photo.objects.all(),
			'template_name': 'photos_detail.html'
		},
		
		name='photo_detail'
	),

	url(r'^detail/(?P<pk>\d+)/$', contacts.views.ChantierView.as_view(),
		name='chantier-view',),


)

