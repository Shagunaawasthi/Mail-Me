from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import EmailMessage
import time

from datetime import timedelta


from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt


class IndexView(View):

    @method_decorator(csrf_protect)
    def get(self, request):
    	return render(request, 'mymail/about.html', {})

    

    
    @method_decorator(csrf_protect)
    def post(self, request):
        email = EmailMessage('yolo', 'chal gaya yeaa', to=['XXXXXX@gmail.com'])
        email.send()
        return render(request, 'mymail/about.html', {})


