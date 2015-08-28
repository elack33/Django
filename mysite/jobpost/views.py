from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import logging
logger = logging.getLogger(__name__)

from .models import JobPost

from .forms import NewJobPost, DeleteListForm


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('../view_jobs')



@login_required(login_url='/accounts/login/')
def job_post(request):
    if request.method == 'POST':
        form = NewJobPost(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../view_jobs')

    else:
        form = NewJobPost(
            initial={'title': 'Rogue', 'description': 'Stabystaby'}
        )

    return render(request, 'post_job.html', {'form': form})


def view_jobs(request):
    return render_to_response(
        'view_jobs.html',
        context={
            'jobs': JobPost.objects.all()
        }
    )


def thanks(request):
    return render_to_response(
        'thanks.html'
    )

@login_required
def delete(request):
    if request.method == 'POST':
        form = DeleteListForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../view_jobs')

    else:
        form = DeleteListForm()

    return render(request, 'delete_post.html', {'form': form})

# def create_user(request):
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)


def job_detail(request, job_id):
    logger.debug('hello world!')
    logger.info('This is the INFO LEVEL! :D WOOO!')
    job = get_object_or_404(JobPost, id=job_id)
    return render(
        request,
        'job_detail.html',
        context={
            'job': job,
        }
    )















