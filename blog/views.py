from ast import Delete
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import BlogApp


class BlogAppCreateView(CreateView):
   model = BlogApp
   
   fields = ['title',
             'description'
   ]
   
   template_name = 'home.html'
   success_url = "list.html"
class BlogAppListView(ListView):
   model = BlogApp
   template_name = 'list.html'

class BlogAppDetailView(DetailView):
   model = BlogApp
   template_name = 'detail.html'
   
class BlogAppUpdateView(UpdateView):
   model = BlogApp
   field =[
      "title",
      "description"
   ]
   template_name = 'update.html'
   success_url = '/'
   
   
class BlogAppDeleteView(DeleteView):
   model = BlogApp
   template_name = 'delete.html'
   success_url = '/'


