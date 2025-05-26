from django.shortcuts import render
from . import models
from django.views.generic.base import TemplateView

from django.views import generic

class HomePageView(TemplateView):

    template_name = "Catalog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_books'] = models.Book.objects.all().count()
        context['num_instances'] = models.BookInstance.objects.all().count()
        context['num_instances_available'] = models.BookInstance.objects.filter(status__exact='a').count()
        context['num_authors'] = models.Author.objects.count()
        return context
    
class BookListView(generic.ListView):
    model = models.Book
   
    template_name = 'Catlog/Book_list.html'
    # queryset = models.Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
   
   
class BookDetailView(generic.DetailView):
    model = models.Book # Specify your own template name/location
    template_name = 'Catlog/book_detail.html'

class AuthorlistView(generic.ListView):
    model = models.Author
    template_name = 'Catalog/author_list.html'
# def index(request):
#     """
#     View function for home page of site.wdwss
#     """
#     # Generate counts of some of the main objects
#     num_books=models.Book.objects.all().count()
#     num_instances=models.BookInstance.objects.all().count()
#     # Available books (status = 'a')
#     num_instances_available=models.BookInstance.objects.filter(status__exact='a').count()
#     num_authors=models.Author.objects.count()  # The 'all()' is implied by default.
    
#     # Render the HTML template index.html with the data in the context variable
#     return render(
#         request,
#         'Catalog/index.html',
#         context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
#     )