from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from jobeet.models import Job
from jobeet.models import * # to be scrutinized
from jobeet.models import Category # to be scrutinized

"""
This function returns nothing and is called with the wrong
number of arguments, it should be pointed out in Scrutinizer
"""
def do_something(arg1, arg2):
    print("Hello")

def index(request):
    # This is a comment way too long and I will probably see some errors in Scrutinizer for this :)
    signature = 'Unused string' # to be scrutinized
    do_something('just_one_arg')
    if sgnature: # intentional typo to be scrutinized
        pass

    return render(request, 'jobeet/index.html', {
        'signature': 'C3-PO, Human-Cyborg relations.'
    })


class JobList(ListView):
    model = Job


class JobCreate(CreateView):
    model = Job
    success_url = reverse_lazy('job_list')


class JobUpdate(UpdateView):
    model = Job
    success_url = reverse_lazy('job_list')


class JobDelete(DeleteView):
    model = Job
    success_url = reverse_lazy('job_list')
