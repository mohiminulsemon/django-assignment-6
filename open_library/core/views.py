from django.shortcuts import render
from django.views.generic import TemplateView
from books.models import Book
from books.constants import CATEGORY_CHOICES
# Create your views here.

# class HomeView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['books'] = Book.objects.all()
#         context['categories'] = CATEGORY_CHOICES
#         return context





def home(request, book_category=None):
    books = Book.objects.all()
    categories = [category[0] for category in CATEGORY_CHOICES]
    for book in books: 
        print(book)
    # print(categories)
    bookCategory = book_category
    if book_category:
        books = books.filter(categories=bookCategory)


    return render(request, 'index.html', {'books': books, 'categories': categories})
