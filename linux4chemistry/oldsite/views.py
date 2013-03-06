from django.views.generic import TemplateView

class Linux4ChemistryView(TemplateView):
    template_name = 'oldsite/linux4chemistry.html'

class LicenseDefinitionView(TemplateView):
    template_name = 'oldsite/definition.html'

class LeaveCommentView(TemplateView):
    template_name = 'oldsite/leavecomment.html'
