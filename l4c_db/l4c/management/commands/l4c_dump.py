from django.core.management import call_command
from django.core.management.base import BaseCommand

from l4c import fixture_path

class Command(BaseCommand):

    help = (
        'A simple shortcut to the dumpdata management command'
        )

    def handle(self, *args, **options):

        with open(fixture_path, "w") as fixture: 
            call_command("dumpdata", "l4c", format="json", indent=4,
                         stdout=fixture)
