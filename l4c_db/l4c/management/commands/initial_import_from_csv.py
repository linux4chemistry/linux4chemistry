import os
import csv
import collections
import itertools

from django.core.management.base import BaseCommand, CommandError

import oldsite
from l4c.models import Software, LicenseModel, Category


class Command(BaseCommand):

    help = (
        'Initial import of the historical data from the CSV document into ' +
        'the relational backend'
        )

    def handle(self, *args, **options):

        # preload the main software categories

        LICENSE_MODELS = (
            ('open_source', 'Open Source'),
            ('freeware', 'Freeware'),
            ('academic', 'Free for academics'),
            ('shareware', 'Shareware'),
            ('commercial', 'Commercial'),
            )

        license_models = dict(
            (name, LicenseModel.objects.create(label=label, name=name))
            for (label, name) in LICENSE_MODELS
            )

        CATEGORIES = (
            ('MD', 'Molecular Dynamics'),
            ('Viewer', '3D Viewer'),
            ('QM', 'Quantum Mechanics'),
            ('Rxn', 'Reactions'),
            ('Draw', '2D Draw'),
            ('Xtal', 'Crystallography'),
            ('NMR', 'NMR'),
            ('Cheminf', 'Cheminformatics'),
            ('MM', 'Molecular Mechanics'),
            ('Dock', 'Docking'),
            ('Thermo', 'Thermodynamics'),
            ('MS', 'Mass Spectrometry'),
            ('Electrochemistry', 'Electrochemistry'),
            ('Education', 'Education'),
            )

        categories = dict(
            (label, Category.objects.create(label=label, name=name))
            for (label, name) in CATEGORIES
            )

        # and now the Software records

        Record = collections.namedtuple(
            'Record', [
                'name', 'url', 'categories', 'other_categories', 
                'license_model', 'open_source_info', 
                'description', 'comments'
                ]
            )

        filepath = os.path.join(os.path.dirname(oldsite.__file__),
                                'data', 'l4c.txt')

        with open(filepath, 'rb') as csvfile:
            csvdata = csv.reader(csvfile, delimiter='\t')
            csvdata.next() # skip header
            for record in itertools.imap(Record._make, csvdata):
                model_data = record._asdict()
                
                lm = license_models[model_data['license_model']]
                model_data['license_model'] = lm

                cats = (
                    categories[cat.strip()] 
                    for cat in model_data['categories'].split(',') if cat
                    )
                del model_data['categories']

                sw = Software.objects.create(**model_data)
                sw.categories = cats
                sw.save()


                    
                
                
