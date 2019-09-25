from django.conf.urls import url
from django.urls import include

from books.views import get_books_from_api

urlpatterns = [
    url(r'^external-books/$', get_books_from_api),
    url('^v1/', include('books.api.v1.urls')),
    ]
