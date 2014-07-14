from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.conf import settings

from cclfeed.models import MessageData

CCLFEED_MAX_MSGS = getattr(settings, "CCLFEED_MAX_MSGS", 50)

class LatestMessagesFeed(Feed):
    title = "CCL"
    link = "http://www.ccl.net/"
    description = "RSS Feed of the world's greatest computational chemistry"
    "mailing list, chemistry@ccl.net (the CCL list)",

    def items(self):
        return MessageData.objects.order_by('-sent_on')[:CCLFEED_MAX_MSGS]

    def item_title(self, item):
        return item.subject

    def item_description(self, item):
        return item.text.replace('\n', '<br>')

