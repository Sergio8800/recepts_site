from django.shortcuts import redirect

def redirect_lst(request):
    return redirect('index_start_app', permanent=True)