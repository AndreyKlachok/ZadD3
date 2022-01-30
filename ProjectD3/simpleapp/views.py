from django.views.generic import ListView, DetailView
from .models import New
from datetime import datetime

class NewsList(ListView):
    model = New
    template_name = 'News.html'
    context_object_name = 'news'
    queryset = New.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class NewDetail(DetailView):
    model = New
    template_name = 'new.html'
    context_object_name = 'new'