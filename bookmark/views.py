from django.shortcuts import render

# Create your views here.



from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template

from django.shortcuts import render_to_response

from django.contrib.auth.models import User
from django.contrib.auth import logout

from bookmark.forms import *

from django.template import RequestContext


def index(request):
    template = get_template('bookmark/index.html')
    variables = Context({
        'user': request.user
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
        'user': request.user,
        'username': username,
        'bookmarks': bookmarks
    })

    output = template.render(variables)

    return HttpResponse(output)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
                email = form.cleaned_data['email']
            )
            return HttpResponseRedirect('/')

    else:
            form = RegistrationForm()

    variables = RequestContext(request, {
            'form' : form
        })

    return render_to_response(
        'registration/register.html',
        variables
    )