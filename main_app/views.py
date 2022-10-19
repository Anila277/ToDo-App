from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin




def home(request): 
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')


def signup(request):
    error_message = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasks')
        else:
            error_message = 'Signup Input Invalid, Try Again.'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', { 'form': form, 'error': error_message })



class TaskList(LoginRequiredMixin, ListView): 
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self):
        context = super().get_context_data()
        search_input = self.request.GET.get('Search-Area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['search_input'] = search_input
        
        return context


    def get(self, request):
        self.object_list = self.get_queryset().filter(user=self.request.user)
        context = self.get_context_data()
        return self.render_to_response(context)



class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'

    success_url = reverse_lazy('tasks')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')




