from django.shortcuts import render
from .models import Job, Catagory

def read_jobs(req):
    stored_jobs = Job.objects.all()
    context = {'jobs': stored_jobs}

    return render(req, 'job/jobs.html', context)

def job_detail(req, id):
    job = Job.objects.get(id=id)
    context = {'job': job}

    return render(req, 'job/job.html', context)
