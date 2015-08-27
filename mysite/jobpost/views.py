from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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

def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)















