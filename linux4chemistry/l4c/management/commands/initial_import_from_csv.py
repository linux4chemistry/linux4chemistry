import os
import csv
import collections
import itertools

from django.core.management.base import BaseCommand, CommandError

import oldsite
from l4c.models import Software


Record = collections.namedtuple(
    'Record', [
        'name', 'url', 'categories', 'other_categories', 
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

        db_license_models = dict(
            (display_name, db_value) 
            for (db_value, display_name) 
            in Software.LICENSE_MODELS._display_map.items()
            )
 
        filepath = os.path.join(os.path.dirname(oldsite.__file__),
                                'data', 'l4c.txt')

        with open(filepath, 'rb') as csvfile:
            csvdata = csv.reader(csvfile, delimiter='\t')
            csvdata.next() # skip header
            for record in itertools.imap(Record._make, csvdata):
                model_data = record._asdict()
                license_model = db_license_models[model_data['license_model']]
                model_data['license_model'] = license_model
                Software.objects.create(**model_data)


                    
                
                
