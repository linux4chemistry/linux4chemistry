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
        'academic': True,
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
        programs = self.get_programs(self._form2search(self.get_initial()))
        context = dict(form=form, programs=programs)
        return self.render_to_response(self.get_context_data(**context))

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        # instead of redirecting to a new page we render the current one
        # again.
        programs = self.get_programs(self._form2search(form.cleaned_data))
        context = dict(form=form, programs=programs)
        return self.render_to_response(self.get_context_data(**context))

    def form_invalid(self, form):
        # we expect the form to be valid in any configuration
        raise NotImplementedError

    def get_programs(self, searchdata):
        """Return a list of the selected programs"""
        Program = namedtuple('Program', 
                             'name web categories lic lang desc')
        filepath = os.path.join(os.path.dirname(__file__), 'data', 'l4c.txt')

        programs = []

        category = searchdata['category']
        licenses = set(k for (k, v) in searchdata.items() 
                       if k in forms.LICENSE_NAMES and v)

        with open(filepath, 'r') as data:
            data.next() # skip header
            for record in data:
                fields = [f.strip() for f in record.split('\t')]
                (name, web, cat, other_cat, lic, lang, desc) = fields[:7]
                cat = [c.strip() for c in cat.split(',')] if cat else []
                other_cat = ([c.strip() for c in other_cat.split(',')] 
                             if other_cat else [])

                if lic not in licenses:
                    continue

                if (category not in ('all', 'other') and category not in cat):
                    continue

                if (category == 'other' and cat):
                    continue

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

    def _form2search(self, formdata):
        return {
            'Open Source': formdata.get('open_source', True),
            'Freeware': formdata.get('freeware', True),
            'Free for academics': formdata.get('academic', True),
            'Shareware': formdata.get('shareware', True),
            'Commercial': formdata.get('commercial', True),
            'category': formdata.get('category', 'all')
            }
            

class LicenseDefinitionView(TemplateView):
    template_name = 'oldsite/definition.html'
