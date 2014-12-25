from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, TemplateView
from django.contrib.auth import authenticate, login, logout

from braces.views import LoginRequiredMixin

from .forms import UserRegistrationForm, LoginForm

class RegisterUserView(FormView):

	template_name = 'users/user_registration.html'
	form_class = UserRegistrationForm
	success_url = '/'

	def form_valid(self, form):
		user = form.save()
		if self.request.POST.get('teacher') == 'on':
			user.teacher = True
		if self.request.POST.get('student') == 'on':
			user.student = True
		user.set_password(user.password)
		user.save()
		return super(RegisterUserView, self).form_valid(form)

class LoginUserView(FormView):

	template_name = 'users/user_login.html'
	form_class = LoginForm
	success_url = '/'

	def form_valid(self, form):
		user = authenticate(email = form.cleaned_data['email'],
							password = form.cleaned_data['password'])
		if user:
			login(self.request, user)
		return super(LoginUserView, self).form_valid(form)


def LogOut(request):
	logout(request)
	return redirect('/')

class PremiumUserView(LoginRequiredMixin, TemplateView):

	template_name = 'users/premium.html'
	login_url = '/login/'