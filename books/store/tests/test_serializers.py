# -*- coding: utf-8 -*-

from django.test import TestCase
from store.serializer import BooksSerializer
from store.models import Book

class BookserializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='1984', price=12.99)
        book_2 = Book.objects.create(name='War and peace', price=100.00)
        data = BooksSerializer([book_1, book_2], many=True).data
        excepted_data = [
            {
            'id': book_1.id,
            'name': "1984",
            'price': '12.99',
            'author_name': 'Orwell'
            },
            {
                'id': book_2.id,
                'name': "War and peace",
                'price': '9.45',
                'author_name': 'Tolstoy'
            },
        ]
        self.assertEqual(excepted_data, data)