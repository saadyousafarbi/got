from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from books.models import Book, Author, Publisher, Country


class BookAPISerializer(serializers.Serializer):
    name = serializers.CharField()
    isbn = serializers.CharField()
    authors = serializers.ListField()
    publisher = serializers.CharField()
    numberOfPages = serializers.IntegerField()
    country = serializers.CharField()
    released = serializers.DateTimeField()


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)

    def to_representation(self, instance):
        return instance.name

    def to_internal_value(self, data):
        return Author.objects.get(name=data)

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name', )

    def to_representation(self, instance):
        return instance.name

    def to_internal_value(self, data):
        return Country.objects.get(name=data)

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('name', )

    def to_representation(self, instance):
        return instance.name

    def to_internal_value(self, data):
        return Publisher.objects.get(name=data)

class BookModelSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    publisher = PublisherSerializer()
    country = CountrySerializer()

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        authors = validated_data.pop('authors')
        new_book = Book.objects.create(**validated_data)
        new_book.authors.add(*authors)
        new_book.save()
        return new_book

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.country = validated_data.get('country', instance.country)
        if validated_data.get('author'):
            instance.authors.add(*validated_data.get('authors'))
        instance.released_date = validated_data.get('released_date', instance.released_date)
        instance.number_of_pages = validated_data.get('number_of_pages', instance.number_of_pages)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.save()
        return instance
