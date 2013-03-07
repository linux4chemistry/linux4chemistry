import os
from collections import namedtuple

from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, FormView

from . import forms

class Linux4ChemistryView(FormView):
    template_name = 'oldsite/linux4chemistry.html'
    form_class = forms.Linux4ChemistryForm
    initial = {
        'open_source': True,
        'freeware': True,
        'free_for_academics': True,
        'shareware': True,
        'commercial': True,
        'category': 'all',
        }

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates a blank version of the form.
        """
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        programs = self.get_programs(**self.get_initial())
        context = dict(form=form, programs=programs)
        return self.render_to_response(self.get_context_data(**context))

    def get_programs(self, **kwargs):
        """Return a list of the selected programs"""
        Program = namedtuple('Program', 
                             'name web categories lic lang desc')
        filepath = os.path.join(os.path.dirname(__file__), 'data', 'l4c.txt')

        programs = []

        with open(filepath, 'r') as data:
            data.next() # skip header
            for record in data:
                fields = [f.strip() for f in record.split('\t')]
                (name, web, cat, other_cat, lic, lang, desc) = fields[:7]
                cat = [c.strip() for c in cat.split(',')] if cat else []
                other_cat = ([c.strip() for c in other_cat.split(',')] 
                             if other_cat else [])
                # check 
                
                categories = ', '.join(
                    [forms.CATEGORIES.get(c, c) for c in cat] +
                    other_cat
                    )
                
                programs.append(
                    Program._make((name, web, categories, lic, lang, desc))
                    )

        return programs

    def get_success_url(self):
        return reverse('home')


class LicenseDefinitionView(TemplateView):
    template_name = 'oldsite/definition.html'


class LeaveCommentView(TemplateView):
    template_name = 'oldsite/leavecomment.html'
