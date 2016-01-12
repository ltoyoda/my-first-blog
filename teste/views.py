from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'teste/post_list.html', {})
