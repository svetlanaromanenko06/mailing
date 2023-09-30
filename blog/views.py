from django.views.generic import ListView, DetailView
from blog.models import Blog

class BlogListView(ListView):
    'Класс для просмотра статей блога'
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object