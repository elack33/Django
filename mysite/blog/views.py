from django.shortcuts import render_to_response

from .models import BlogArticle, BlogComment


def page_with_links(request):
    return render_to_response(
        'blog_list.html',
        context={
            'blogs': BlogArticle.objects.all(),
        }
    )

def one_at_a_time(request, blog_id):
    return render_to_response(
        'one_at_a_time.html',
        context={
            'blog': BlogArticle.objects.get(pk=blog_id),
            # 'comment': BlogComment.objects.filter(blog__blog_article_id=blog_id),


        }
    )

def about_page(request):
    return render_to_response(
        'about_page.html',

    )