from django.core.management import call_command
from django.core.management.base import BaseCommand

from l4c import fixture_path

class Command(BaseCommand):

    help = (
        'A simple shortcut to the loaddata management command'
        )

    def handle(self, *args, **options):

        call_command("loaddata", fixture_path)
