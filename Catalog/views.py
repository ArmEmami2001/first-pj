from django.shortcuts import render
from . import models
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import RenewBookForm
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
    template_name = 'Catalog/book_detail.html'

class AuthorlistView(generic.ListView):
    model = models.Author
    template_name = 'Catalog/author_list.html'

class AuthorDetailView (generic.DetailView):
    model = models.Author
    template_name = 'Catalog/author_detail.html'
    

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = models.BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return models.BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
    

@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    """
    View function for renewing a specific BookInstance by librarian
    """
    book_inst=get_object_or_404(models.BookInstance, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('my-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})




class AuthorCreate(CreateView):
    model = models.Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']
    initial={'date_of_death':'05/01/2018',}

class AuthorUpdate(UpdateView):
    model = models.Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']

class AuthorDelete(DeleteView):
    model = models.Author
    success_url = reverse_lazy('authors')
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