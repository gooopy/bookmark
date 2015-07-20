from django.shortcuts import render

# Create your views here.



from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from django.contrib.auth.models import User


def index(request):
    template = get_template('bookmark/index.html')
    variables = Context({
        'head_title': 'Horraaaay!!!',
        'page_title': 'Welcome Django-bookmark',
        'page_body': 'Save your bookmarks',
    })
    output = template.render(variables)

    return HttpResponse(output)


def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('Can\'t find')

    bookmarks = user.bookmark_set.all()

    template = get_template('bookmark/user_page.html')
    variables = Context({
        'username': username,
        'bookmarks': bookmarks
    })

    output = template.render(variables)

    return HttpResponse(output)