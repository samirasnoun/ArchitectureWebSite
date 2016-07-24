from django.contrib.sitemaps import Sitemap
from .models import Chantier, Media
import datetime 
from django.core.urlresolvers import reverse


class ChantierSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Chantier.objects.all()


class MediaSitemap(Sitemap):
    changefreq='weekly'
    priority=0.9
    def items(self):
        return Media.objects.all()





class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['profil', 'contact']

    def location(self, item):
        return reverse(item)

        
    # def changefreq(self, obj):
    #     return 'monthly'

    # def lastmod(self, obj):
    #     return datetime.datetime.now()

    # def location(self, obj):
    #     return reverse(obj)




# from django.contrib.sitemaps import Sitemap
# from .models import Post
# class PostSitemap(Sitemap):
#     changefreq = 'weekly'
#     priority = 0.9
#     def items(self):
#         return Post.published.all()
#     def lastmod(self, obj):
#         return obj.publish