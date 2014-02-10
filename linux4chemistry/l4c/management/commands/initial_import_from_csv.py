import os
import csv
import collections
import itertools

from django.core.management.base import BaseCommand, CommandError

import oldsite
from l4c.models import Software

Record = collections.namedtuple(
    'Record', [
        'name', 'url', 'category', 'additional_category', 
        'license_model', 'open_source_info', 
        'description', 'comments'
        ]
    )

class Command(BaseCommand):
    help = (
        'Initial import of the historical data from the CSV document into ' +
        'the relational backend'
        )

    def handle(self, *args, **options):

        filepath = os.path.join(os.path.dirname(oldsite.__file__),
                                'data', 'l4c.txt')

        with open(filepath, 'rb') as csvfile:
            csvdata = csv.reader(csvfile, delimiter='\t')
            for record in itertools.imap(Record._make, csvdata):
                Software.objects.create(**record._asdict())


                    
                
                
