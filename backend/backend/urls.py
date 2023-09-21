from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views as todo_views
from local import views as local_views

# Define routers for each app
router = routers.DefaultRouter()
router.register(r'tasks', todo_views.TodoView, 'task')  # For the 'todo' app

local_router = routers.DefaultRouter()
local_router.register(r'tasks', local_views.LocalView)  # For the 'local' app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include the 'todo' app's router
    path('api/local/', include(local_router.urls)),  # Include the 'local' app's router

]
