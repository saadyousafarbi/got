from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from books.models import Book
from books.serializers import BookModelSerializer


class BooksViewSet(ModelViewSet):
    lookup_field = 'pk'
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'country']

    def list(self, request, *args, **kwargs):
        queryset = Book.objects.all()
        serializer = BookModelSerializer(queryset, many=True)
        return Response({"status_code": 200,
                         "status": "success",
                         "data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = BookModelSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response({"status_code": 201,
                         "status": "success",
                         "data": serializer.data})

    def update(self, request, *args, **kwargs):
        book_instance = Book.objects.get(id=self.kwargs['pk'])
        book_name = book_instance.name
        serializer = BookModelSerializer(book_instance, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response({"status_code": 200,
                         "status": "success",
                         "message": "The book {} was updated successfully".format(book_name),
                         "data": serializer.data})

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({"status_code": 200,
                         "status": "success",
                         "data": serializer.data})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"status_code": 204,
                         "status": "success",
                         "message": "The book {} was deleted successfully".format(instance.name),
                         "data": []})
