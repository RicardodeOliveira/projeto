from django.shortcuts import render

def ctes_list(request):
    return render(request, 'listagem.html')