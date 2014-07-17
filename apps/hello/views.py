from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from models import Info


class InfoView(DetailView):
    context_object_name = 'myinfo'
    template_name = 'index.html'
    model = Info

    def get_object(self):
        info = get_object_or_404(Info, pk=1)
        return info

