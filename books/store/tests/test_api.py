from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from store.models import Book
from store.serializer import BooksSerializer


class BooksApiTestCase(APITestCase):


    def setUp(self):
        self.book_1 = Book.objects.create(name='1984', price = 12.99, author_name='Orwell')
        self.book_2 = Book.objects.create(name='War and peace', price = 9.45, author_name='Tolstoy')
        self.book_3 = Book.objects.create(name='Gatsby', price = 5.00, author_name='Finker')
        self.book_4 = Book.objects.create(name='Басни', price = 2.00, author_name='Orwell')

    def test_get(self):
        url = reverse('book-list')
        print('url ', url)
        response = self.client.get(url)
        print('response ', response.data)
        serializer_data = BooksSerializer([self.book_1, self.book_2,
                                           self.book_3, self.book_4], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        # self.test_get()
        url = reverse('book-list')
        print('url ', url)
        response = self.client.get(url, data={'search': 'Orwell'})
        print('response ', response.data)
        serializer_data = BooksSerializer([self.book_1, self.book_4], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)