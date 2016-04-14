from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from jobeet.models import Job


def index(request):
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
