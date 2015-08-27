from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse

from .models import CommentBox

def index(request):
    # print 'HELLO'
    # x = 0
    # for i in range(100):
    #     x += i

    total_comments = CommentBox.objects.count()

    texts = ''
    approved_comments = 0
    for comment in CommentBox.objects.all():
        if comment.approved:
            approved_comments += 1
            texts += comment.comment_text



    return HttpResponse(
        # "<strong>Hello, world. Isn't this the coolest thing ever?? SOMETHING FUN!</strong>"
        # 'The number is {}'.format(x)
        'There are currently {} comment(s), there are {} approved comments, here they are: {}.'.format(
            total_comments, approved_comments, texts)
    )


def comment_page(request):
    comments = CommentBox.objects.all()
    # for comment in CommentBox.objects.all():
    #     comments.append(comment.comment_text)

    print comments # this should show up int he terminal running the server
    return render_to_response(
        'comment_return.html',
        context={
            'comments': comments,  # the first part is the name of the variable in the html page {{}}
        }
    )












