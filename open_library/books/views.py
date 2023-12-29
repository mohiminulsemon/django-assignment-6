from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from . import forms, models
from django.contrib.auth.models import User



def book_detail(request, book_id):
    book = get_object_or_404(models.Book, id=book_id)

    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.book = book
            new_comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('book_detail', book_id=book.id)


    comments = models.Comment.objects.filter(book=book)
    comment_form = forms.CommentForm(initial={'user': request.user})


    return render(request, 'book_detail.html', {'book': book, 'comments': comments, 'comment_form': comment_form})