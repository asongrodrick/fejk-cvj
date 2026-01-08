from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Project
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def api_projects(request):
    if request.method == 'GET':
        qs = Project.objects.order_by('-created_at').all()
        data = []
        for p in qs:
            data.append({
                'id': p.id,
                'title': p.title,
                'description': p.description,
                'image': p.image,
                'project_url': p.project_url,
                'created_at': p.created_at,
            })
        return JsonResponse({'projects': data}, safe=False)
    return HttpResponseNotAllowed(['GET'])

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status':'ok','message':'Saved'})
        else:
            return JsonResponse({'status':'error','errors': form.errors}, status=400)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
