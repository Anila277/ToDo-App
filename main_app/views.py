import imp
from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Task


def  home(request): 
    return render(request, 'home.html')

def  about(request): 
    return render(request, 'about.html')

class TaskList(ListView): 
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self):
        context = super().get_context_data()
        search_input = self.request.GET.get('Search-Area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['search_input'] = search_input
        
        return context



class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')




