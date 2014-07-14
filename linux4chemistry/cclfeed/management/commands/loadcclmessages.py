import ftplib
import tempfile
import mailbox
import pytz
import datetime
import email

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from cclfeed.models import MessageData

CCLFEED_LOADMSGS_DAYS = getattr(settings, "CCLFEED_LOADMSGS_DAYS", 5)

class Command(BaseCommand):
    help = 'Read messages from ftp.ccl.net and store them in the database'

    def handle(self, *args, **options):
        today = datetime.date.today()
        days = [today - datetime.timedelta(days=days) 
                for days in range(CCLFEED_LOADMSGS_DAYS-1, -1, -1)]

        imported = 0
        messages = 0
        f = ftplib.FTP('ftp.ccl.net', 'anonymous')
        for day in days:
            mbox = tempfile.NamedTemporaryFile()
            directory = '/pub/chemistry/archived-messages/{0}/{1:02}'.format(day.year, day.month)
            try:
                self.stdout.write('reading file {0}/{1:02}'.format(directory, day.day))
                f.cwd(directory)
                f.retrbinary('RETR {0:02}'.format(day.day), mbox.write)

                parser = mailbox.mbox(mbox.name)
                for i, msg in enumerate(parser):
                    messages += 1
                    datehdr = msg['Date']
                    if datehdr is None:
                        # without date it is not possible to build the
                        # link to the original message on the CCL website
                        continue
                    timestamp = email.utils.mktime_tz(
                        email.utils.parsedate_tz(get_header(datehdr)))
                    date = datetime.datetime.fromtimestamp(timestamp, pytz.utc)
                    body = get_body(msg) 
                    _, created = MessageData.objects.get_or_create(
                        msg_id=get_header(msg['Message-Id']),
                        subject=get_header(msg['Subject']),
                        sent_on=date,
                        sender=get_header(msg['X-Original-From']),
                        text=body,
                        ordinal=i+1
                        )
                    if created:
                        imported += 1
            except Exception as e:
                self.stdout.write('Error: {0}'.format(e))

        self.stdout.write('%s messages read, % s new ' % (messages, imported))


# some useful utility functions from 
# http://ginstrom.com/scribbles/2007/11/19/parsing-multilingual-email-with-python/

def get_header(header_text, default="ascii"):
    """Decode the specified header"""

    headers = email.header.decode_header(header_text)
    header_sections = [
        unicode(text, charset or default) for text, charset in headers
        ]
    return u"".join(header_sections)


def get_charset(message, default="ascii"):
    """Get the message charset"""

    if message.get_content_charset():
        return message.get_content_charset()
    if message.get_charset():
        return message.get_charset()
    return default


def get_body(message):
    """Get the body of the email message"""

    if message.is_multipart():
        #get the plain text version only
        text_parts = [
            part for part in email.Iterators.typed_subpart_iterator(message,
                                                                    'text',
                                                                    'plain')
            ]
        body = []
        for part in text_parts:
            charset = get_charset(part, get_charset(message))
            body.append(unicode(part.get_payload(decode=True), 
                                charset,
                                "replace"))

        return u"\n".join(body).strip()

    else: # if it is not multipart, the payload will be a string
          # representing the message body
        body = unicode(message.get_payload(decode=True),
                       get_charset(message),
                       "replace")
        return body.strip()
