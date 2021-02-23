from django.contrib import messages
from django.contrib.auth.backends import UserModel
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.models import User
from .forms import UserCreationForm, PasswordChangeForm
import re


def login_view(request, *args, **kwargs):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect('webapp:index')
        else:
            context['has_error'] = True
            context['next'] = next_url
            context['username'] = username
    else:
        context = {'next': request.GET.get('next')}
    return render(request, 'registration/login.html', context=context)


def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('webapp:index')


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')

    else:
        form = UserCreationForm()
    return render(request, 'user_create.html', context={'form': form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, ('Your account have been confirmed.'))
        return redirect('webapp:index')
    else:
        return HttpResponse('Activation link is invalid!')


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'


class UserPasswordChangeView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_password_change.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_obj'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def get_success_url(self):
        return reverse('accounts:login')


class EmailEditView(View):
    def post(self, request):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        user = User.objects.get(pk=int(request.POST['user_id']))
        if (re.search(regex, request.POST['email'])):
            user.email = request.POST['email']
            user.save()
            return JsonResponse({'status': 'Your email successfully changed', 'email': user.email})
        return JsonResponse({'status': 'email is not valid'})


class UsernameEditView(View):
    def post(self, request):
        user = User.objects.get(pk=int(request.POST['user_id']))
        print(request.POST['username'])
        try:
            User.objects.get(username=request.POST['username'])
            return JsonResponse({'status': 'error', 'error': 'Username is already exist, please choose another one!'})
        except Exception:
            user.username = request.POST['username']
            user.save()
            return JsonResponse({'status': 'Username is successfully changed', 'username': user.username})


class FirstNameEditView(View):
    def post(self, request):
        user = User.objects.get(pk=int(request.POST['user_id']))
        user.first_name = request.POST['first_name']
        user.save()
        return JsonResponse({'status': 'Your name is successfully edited', 'first_name': user.first_name})


class LastNameEditView(View):
    def post(self, request):
        user = User.objects.get(pk=int(request.POST['user_id']))
        user.last_name = request.POST['last_name']
        user.save()
        # print(request.POST)
        return JsonResponse({'status': 'Your last name is successfully edited', 'last_name': user.last_name})

