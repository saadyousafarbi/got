import requests

from books.serializers import BookAPISerializer


class IceAndFireAPI:
    """
    Ice and Fire API to retrieve books.
    """
    url_endpoint = "https://www.anapioficeandfire.com/api/books"
    serializer = BookAPISerializer

    def update_endpoint_with_query_params(self, name):
        """
        Helper function to parse query params for Ice and Fire API.
        :param name:
        :return:
        """
        if name is not None:
            self.url_endpoint += "?name={}".format(name)

    def get_books(self, query_params):
        """
        Retrieve books from Ice and Fire API.
        """
        self.update_endpoint_with_query_params(query_params.get('name', None))
        api_response = requests.get(self.url_endpoint)
        serializer = self.serializer(data=api_response.json(), many=True)
        serializer.is_valid()
        return serializer.validated_data
