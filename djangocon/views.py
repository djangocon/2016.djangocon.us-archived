import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render

from pinax.blog.models import Post
from symposion.speakers.models import Speaker

def homepage(request):
    return render(request, "homepage.html", {
        'latestposts': Post.objects.published().order_by("published")[:10]})

@login_required
def get_speakers_csv(request):
    if request.user.is_superuser:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Djangocon Speakers.csv"'

        writer = csv.writer(response)
        writer.writerow(['Name', 'Email'])

        for speaker in Speaker.objects.all():
            writer.writerow([speaker.name, speaker.email])

        return response

    return HttpResponseForbidden("Forbidden")
