from datetime import datetime, time
from django.contrib.syndication.views import Feed

from .models import BlogPage

# Djangocon Feed
class BlogFeed(Feed):
    title = "The Djangocon Blog"
    link = "/blog/"
    description = "The latest news and views from Djangocon.us"

    def items(self):
        return BlogPage.objects.live().order_by('-date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return item.full_url

    def item_author_name(self, item):
        pass

    def item_pubdate(self, item):
        return datetime.combine(item.date, time())