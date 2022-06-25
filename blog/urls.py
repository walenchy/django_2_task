from django.urls import path
from .views import BlogAppCreateView, BlogAppListView, BlogAppDetailView, BlogAppUpdateView, BlogAppDeleteView


urlpatterns = [
  path('', BlogAppCreateView.as_view(),
  name='home'),
  path('list/', BlogAppListView.as_view()),
  path('detail/<pk>/', BlogAppDetailView.as_view()),
  path('<pk>/update', BlogAppUpdateView.as_view()),
  path('delete/<pk>/',BlogAppDeleteView.as_view())  
]