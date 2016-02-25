import djangocon.views
import symposion.views

from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView


admin.autodiscover()

WIKI_SLUG = r'(([\w-]{2,})(/[\w-]{2,})*)'
urlpatterns = patterns('')

if 'comps' in settings.INSTALLED_APPS:
    urlpatterns += patterns('', url(r'^', include('comps.urls')))

urlpatterns += patterns(
    '',
    url(r'^$',
        TemplateView.as_view(template_name='homepage.html'), name='home'),

    url(r'^404/$',
        TemplateView.as_view(template_name='404.html'), name='phor-oh-phor'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^account/signup/$', symposion.views.SignupView.as_view(), name='account_signup'),
    url(r'^account/login/$', symposion.views.LoginView.as_view(), name='account_login'),
    url(r'^account/', include('account.urls')),
    url(r'^contact/', include('contact_form.urls')),
    url(r'^schedule/json/$', djangocon.views.schedule_json, name='schedule_json'),

    url(r'^blog/', include('biblion.urls')),
    url(r'^dashboard/', symposion.views.dashboard, name='dashboard'),
    url(r'^speaker/', include('symposion.speakers.urls')),
    url(r'^proposals/', include('symposion.proposals.urls')),
    url(r'^proposals/export/', djangocon.views.proposal_export,
        name='proposal_export'),
    url(r'^sponsors/', include('symposion.sponsorship.urls')),
    url(r'^sponsors/raw/$',
        TemplateView.as_view(template_name='sponsorship/raw.html'), name='sponsors_raw'),

    url(r'^sponsors/guide/$',
        TemplateView.as_view(template_name='sponsorship/guide.html'), name='sponsors_guide'),

    url(r'^sponsors/sponsor_file\.zip$', 'djangocon.lost_levels.views.export_sponsors',
        name='export_sponsors'),

    # Guidebook exports...
    url(r'^guidebook/schedule/$', djangocon.views.schedule_guidebook,
        name='guidebook_schedule'),

    url(r'^guidebook/speakers/', djangocon.views.guidebook_speaker_export,
        name='guidebook_speakers'),

    url(r'^guidebook/sponsors/', djangocon.views.guidebook_sponsor_export,
        name='guidebook_sponsors'),

    url(r'^guidebook/news/feed/', djangocon.views.guidebook_news_feed,
        name='guidebook_news_feed'),

    url(r'^boxes/', include('symposion.boxes.urls')),
    url(r'^teams/', include('symposion.teams.urls')),
    url(r'^reviews/', include('symposion.reviews.urls')),
    url(r'^schedule/', include('symposion.schedule.urls')),
    url(r'^markitup/', include('markitup.urls')),


    url(r'^', include('symposion.cms.urls')),
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
