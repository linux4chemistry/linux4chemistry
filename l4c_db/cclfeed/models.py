from django.db import models

class MessageData(models.Model):

    msg_id = models.CharField(primary_key=True, max_length=100)
    sender = models.CharField(max_length=100)
    sent_on = models.DateTimeField(auto_now=False, auto_now_add=False)
    subject = models.CharField(max_length=1000)
    text = models.TextField()
    ordinal = models.SmallIntegerField()

    def get_absolute_url(self):
        """Return the message URL from the CCL website"""
        baseurl = 'http://www.ccl.net/cgi-bin/ccl/message-new?'
        return baseurl + '{0}+{1:02}+{2:02}+{3:03}'.format(
            self.sent_on.year,
            self.sent_on.month,
            self.sent_on.day,
            self.ordinal
        )

    def __unicode__(self):
        return self.msg_id
