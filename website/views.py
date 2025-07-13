from django.views.generic import TemplateView
from .models import ProjectInfo


class AboutView(TemplateView):
    template_name = 'website/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_info'] = ProjectInfo.objects.order_by('-updated_at').first()
        return context
