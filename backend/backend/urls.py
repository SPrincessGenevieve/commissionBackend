from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views as todo_views
from local import views as local_views
from pictures import views as picture_views  # Import your images views
from django.conf import settings
from django.conf.urls.static import static

# Define routers for each app
router = routers.DefaultRouter()
router.register(r'tasks', todo_views.TodoView, 'task') 

local_router = routers.DefaultRouter()
local_router.register(r'tasks', local_views.LocalView) 

picture_router = routers.DefaultRouter()
picture_router.register(r'tasks', picture_views.PictureViewSet) 


  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include the 'todo' app's router
    path('api/local/', include(local_router.urls)),  
    path('api/pictures/', include(picture_router.urls)), 
    path('api/upload/image/', include(picture_router.urls), name='upload_image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
