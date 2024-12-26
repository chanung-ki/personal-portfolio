from django.shortcuts import render
import logging

logger = logging.getLogger('django')

# Create your views here.
def index(request):
    raise Exception
    return render(request, 'index.html')