import requests

from books.serializers import BookAPISerializer


class IceAndFireAPI:
    url_endpoint = "https://www.anapioficeandfire.com/api/books"
    serializer = BookAPISerializer

    def update_endpoint_with_query_params(self, name):
        if name is not None:
            self.url_endpoint += "?name={}".format(name)

    def get_books(self, query_params):
        self.update_endpoint_with_query_params(query_params.get('name', None))
        api_response = requests.get(self.url_endpoint)
        serializer = self.serializer(data=api_response.json(), many=True)
        serializer.is_valid()
        return serializer.validated_data
