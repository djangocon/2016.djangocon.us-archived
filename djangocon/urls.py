from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from symposion import views as symposion_views
from djangocon import views as djangocon_views
from djangocon import data_views


urlpatterns = [
    url(r'^$', djangocon_views.homepage, name='home'),
    url(r'^account/', include('account.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', include('contact_form.urls')),
    url(r'^schedule/json/$', djangocon_views.schedule_json, name='schedule_json'),
    url(r'^guidebook/news/feed/', djangocon_views.guidebook_news_feed,
        name='guidebook_news_feed'),
]

# Data urls
urlpatterns += [
    url(r'^data/$', data_views.data_home, name='data_home'),
    url(r'^data/proposal_export/', data_views.proposal_export, name='proposal_export'),
    url(r'^data/schedule_guidebook/', data_views.schedule_guidebook, name='schedule_guidebook'),
    url(r'^data/guidebook_sponsor_export/', data_views.guidebook_sponsor_export, name='guidebook_sponsor_export'),
    url(r'^data/guidebook_speaker_export/', data_views.guidebook_speaker_export, name='guidebook_speaker_export'),
]

# Speakers CSV URL
urlpatterns += [
    url(r'^speakers/download/', view=djangocon_views.get_speakers_csv, name='speakers_csv'),
]

# Symposion urls
urlpatterns += [
    url(r'^dashboard/', symposion_views.dashboard, name='dashboard'),
    url(r'^proposals/', include('symposion.proposals.urls')),
    url(r'^reviews/', include('symposion.reviews.urls')),
    url(r'^schedule/', include('symposion.schedule.urls')),
    url(r'^speaker/', include('symposion.speakers.urls')),
    url(r'^sponsors/', include('symposion.sponsorship.urls')),
    url(r'^teams/', include('symposion.teams.urls')),
]

# Pinax urls
urlpatterns += [
    url(r'^boxes/', include('pinax.boxes.urls')),
    url(r'^blog/', include('pinax.blog.urls')),
    url(r'^', include('pinax.pages.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
