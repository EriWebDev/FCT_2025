from django.contrib import admin
from django.urls import path, include
# nuevo codigo Alejandro 19/5/2025 se implementa codigo 
from django.conf import settings
from django.conf.urls.static import static
# nuevo codigo Alejandro 19/5/2025 se implementa codigo 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('monitor.urls')),

# nuevo codigo Alejandro 19/5/2025 se implementa codigo 


]
# nuevo codigo Alejandro 19/5/2025 se implementa codigo 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# nuevo codigo Alejandro 19/5/2025 se implementa codigo     