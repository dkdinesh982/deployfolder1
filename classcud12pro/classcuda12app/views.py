from django.shortcuts import render
from .models import Employee
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
# Create your views here.
class Createview(CreateView):
    model = Employee
    fields = '__all__'
class CompanyDetailView(DetailView):
    model = Employee
class CompanyListView(ListView):
    model = Employee
class CompanyUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
class CompanyDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('list')
#email verication code
# from django.core.mail import BadHeaderError, send_mail
# from django.http import HttpResponse, HttpResponseRedirect
# def send_email(request):
#     subject = request.POST.get('subject', '')
#     message = request.POST.get('message', '')
#     from_email = request.POST.get('from_email', '')
#     if subject and message and from_email:
#         try:
#             send_mail(subject, message, from_email, ['admin@example.com'])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return HttpResponseRedirect('/contact/thanks/')
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return HttpResponse('Make sure all fields are entered and valid.')
