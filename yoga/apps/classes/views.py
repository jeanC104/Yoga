from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

from braces.views import LoginRequiredMixin

from .forms import CreateClassForm

class HomeView(TemplateView):

	template_name = 'classes/home.html'

class CreateClassView(LoginRequiredMixin, CreateView):

	form_class = CreateClassForm
	template_name = 'classes/create_class.html'
	success_url = '/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(CreateClassView, self).form_valid(form)

class AboutView(TemplateView):

	template_name = 'classes/about.html'

class ProfilesView(TemplateView):

	template_name = 'classes/profiles.html'

class ResourcesView(TemplateView):

	template_name = 'classes/resources.html'

class CalendarView(TemplateView):

	template_name = 'classes/calendar.html'