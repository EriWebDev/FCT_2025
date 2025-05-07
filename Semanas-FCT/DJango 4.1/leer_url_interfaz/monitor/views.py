import hashlib
import requests
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import UrlMonitor, BoletinUrl
import urllib3

# Deshabilitar advertencias de SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def index(request):
    active_tab = request.GET.get('tab', 'todos')  # Por defecto, "todos"

    # Diccionario para mapear pestañas a filtros
    tab_filters = {
        'boe': BoletinUrl.objects.all().order_by('has_changed', 'last_checked'),
        'pendientes': UrlMonitor.objects.filter(has_changed=True, is_checked=False).order_by('last_checked'),
        'vistos': UrlMonitor.objects.filter(is_checked=True).order_by('last_checked'),
        'todos': UrlMonitor.objects.all().order_by('has_changed', 'last_checked'),
    }

    # Obtener las URLs según la pestaña activa
    urls = tab_filters.get(active_tab, tab_filters['todos'])

    return render(request, 'monitor/index.html', {
        'urls': urls,
        'active_tab': active_tab,
    })

def check_changes(request):
    # Determinar la tabla según la pestaña activa
    active_tab = request.POST.get('tab', 'todos')
    if active_tab == 'boe':
        urls = BoletinUrl.objects.all()
    else:
        urls = UrlMonitor.objects.all()

    for url_entry in urls:
        try:
            # Deshabilitar la verificación SSL
            response = requests.get(url_entry.url, timeout=10, verify=False)
            content = response.content
            new_hash = hashlib.md5(content).hexdigest()
            if url_entry.hash != new_hash:
                url_entry.has_changed = True
                url_entry.is_checked = False
                url_entry.hash = new_hash
            url_entry.last_checked = timezone.now()
            url_entry.save()
        except Exception as e:
            print(f"Error fetching {url_entry.url}: {e}")
    return redirect(f'/?tab={active_tab}')

def mark_all_checked(request):
    active_tab = request.POST.get('tab', 'todos')
    if active_tab == 'boe':
        BoletinUrl.objects.filter(has_changed=True, is_checked=False).update(is_checked=True)
    else:
        UrlMonitor.objects.filter(has_changed=True, is_checked=False).update(is_checked=True)
    return redirect(f'/?tab={active_tab}')

def reset_status(request):
    active_tab = request.POST.get('tab', 'todos')
    if active_tab == 'boe':
        urls = BoletinUrl.objects.all()
    else:
        urls = UrlMonitor.objects.all()

    for url in urls:
        url.has_changed = False
        url.is_checked = False
        url.save()
    return redirect(f'/?tab={active_tab}')



