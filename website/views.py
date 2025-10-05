from django.views.generic import TemplateView

from phrasebook.models import PhrasebookSection
from names.models import NameCategory

from .models import ProjectInfo


class AboutView(TemplateView):
    template_name = 'website/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_info'] = ProjectInfo.objects.order_by('-updated_at').first()
        return context


class PhrasebookView(TemplateView):
    template_name = 'website/phrasebook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sections'] = (
            PhrasebookSection.objects.prefetch_related('phrases').all()
        )
        return context


class NamesView(TemplateView):
    template_name = 'website/names.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = (
            NameCategory.objects.prefetch_related('names').all()
        )
        return context
