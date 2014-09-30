# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.template.loader import render_to_string
from django.http import HttpResponseBadRequest
from django.template import RequestContext


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(), max_length=1000)


def home(request):
    return render(request, 'test.html')


def contact_form(request):
    if request.GET:
        initial = {}
        if request.GET['name']:
            initial = {'name': request.GET['name']}
        form = ContactForm(initial=initial)
        return render(request, 'form.html', {'form':form})
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse(str(form.cleaned_data))
        else:
            return HttpResponseBadRequest(render_to_string('form.html', RequestContext(request, {'form': form})))