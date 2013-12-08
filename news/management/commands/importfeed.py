from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
import feedparser
from time import mktime
from news.models import Feed, Entry


class Command(BaseCommand):
    help = 'Import entries from remote feed'
    args = '<RSS URL>'

    def handle(self, *args, **options):
        if len(args) < 1:
            raise CommandError('Url must be specified')
        url = args[0]

        doc = feedparser.parse(url)
        if 'bozo_exception' in doc:
            raise CommandError('RSS parse error')

        feed = self.update_or_create_feed(doc['feed'])
        for entry in doc['entries']:
            entry = self.update_or_create_entry(entry, feed)
            print 'Added entry {0}'.format(entry.link)

    def update_or_create_feed(self, feed_original_data):
        feed_data = {
            'link': feed_original_data['link'],
            'title': feed_original_data['title'],
            'description': feed_original_data['description'],
        }
        if Feed.objects.filter(link=feed_data['link']).exists():
            feed = Feed.objects.get(link=feed_data['link'])
            Feed.objects.filter(pk=feed.pk).update(**feed_data)
        else:
            feed = Feed.objects.create(**feed_data)
        return feed

    def update_or_create_entry(self, entry_original_data, feed):
        entry_data = {
            'link': entry_original_data['link'],
            'title': entry_original_data['title'],
            'summary': entry_original_data['summary'],
            'published': datetime.fromtimestamp(mktime(entry_original_data['published_parsed'],)),
            'feed': feed,
        }
        # find picture url
        for link in entry_original_data['links']:
            if 'image' in link['type']:
                entry_data['picture'] = link['href']

        if Entry.objects.filter(link=entry_data['link']).exists():
            entry = Entry.objects.get(link=entry_data['link'])
            Entry.objects.update(**entry_data)
        else:
            entry = Entry.objects.create(**entry_data)
        return entry
