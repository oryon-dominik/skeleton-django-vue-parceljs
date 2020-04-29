
from django.views.generic import TemplateView
from django.conf import settings


class ApplicationView(TemplateView):
	template_name = 'application.html'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['TITLE'] = settings.TITLE
		return context
