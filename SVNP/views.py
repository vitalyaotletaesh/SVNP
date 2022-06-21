from django.shortcuts import render

def post_list(request):
    return render(request, 'SVNP/post_list.html', {})