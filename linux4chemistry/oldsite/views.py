import os
from collections import namedtuple

from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, FormView

from l4c.models import Software

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
        softwares = self.get_softwares(self._form2search(self.get_initial()))
        context = dict(form=form, softwares=softwares)
        return self.render_to_response(self.get_context_data(**context))

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        # instead of redirecting to a new page we render the current one
        # again.
        softwares = self.get_softwares(self._form2search(form.cleaned_data))
        context = dict(form=form, softwares=softwares)
        return self.render_to_response(self.get_context_data(**context))

    def form_invalid(self, form):
        # we expect the form to be valid in any configuration
        raise NotImplementedError

    def get_softwares(self, searchdata):
        """Return a list of the selected softwares"""

        category = searchdata['category']
        licenses = set(k for (k, v) in searchdata.items() 
                       if k in forms.LICENSE_NAMES and v)

        queryset = Software.objects.all()
        
        queryset = queryset.filter(license_model__name__in=licenses)

        if category not in ('all', 'other'):
            queryset = queryset.filter(categories__label=category)
        elif category == 'other':
            queryset = queryset.filter(categories=None)
            
        return queryset.order_by('name')

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
            

class ContributorsView(TemplateView):
    template_name = 'oldsite/contributors.html'
