from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'django-analytical', 'url': 'http://pypi.python.org/pypi/django-analytical/2.4.0'},
	{'name':'django-shop', 'url': 'http://pypi.python.org/pypi/django-shop/0.11.3'},
	{'name':'django-guardian', 'url': 'http://pypi.python.org/pypi/django-guardian/1.4.9'},
    ]
    context = {
        'title': 'sgmagar-crowdbotics-dev-87',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
