from django.views.generic import ListView, CreateView, UpdateView
from .models import Computer


class ComputerListView(ListView):
    model = Computer
    template_name = 'computer_list.html'
    context_object_name = 'computers'


class ComputerCreateView(CreateView):
    model = Computer
    template_name = 'computer_form.html'
    fields = ['computer_code', 'computer', 'quantity', 'unit_rate']
    success_url = '/list/'


class ComputerUpdateView(UpdateView):
    model = Computer
    template_name = 'computer_form.html'
    fields = '__all__'
    success_url = '/list/'


