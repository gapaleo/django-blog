from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post


class LatestPostsFeed(Feed):
    title = 'My posts'
    link = '/latest/feed/'
    description = 'Latest published posts of my blog.'

    def items(self):
        published = Post.objects.exclude(published_date__exact=None)
        posts = published.order_by('-published_date')
        return posts

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])
