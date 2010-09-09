from django.conf.urls.defaults import *
import os.path
from apps.settings import *

from django.contrib import admin
admin.autodiscover()

from apps.shout.views import *
from apps.feedback.views import *

PROJECT_DIR = os.path.dirname(__file__)

urlpatterns = patterns('',
    (r'^$', index),
    (r'^add/', add),
    (r'^admin/', include(admin.site.urls)),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': PROJECT_DIR + '/media'}),

    #URLs para FeedBack
    (r'^feedback/', feedback),
    (r'^enviar/', enviar),
    (r'^album/(?P<slug>[-\w]+)/$', 'apps.galeria.views.gallery'),
    (r'^crear/', 'apps.galeria.views.crear_galeria'),
    (r'^new-album/', 'apps.galeria.views.crear_album'),
    (r'^coment/', 'apps.galeria.views.create_comment'),
    (r'^getcomet/', 'apps.galeria.views.get_comment'),

)

