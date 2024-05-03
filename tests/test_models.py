from django.test import TestCase
from datetime import datetime, timedelta

from orders.models import Book


class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Book.objects.create(
            author="Mike Vasovsky",
            title="Monsters",
            description="some description",
            pages=100,
            available=True,
            price=123.69,
            release=datetime.now(),
        )
        Book.objects.create(
            author="Ernest Hamingway",
            title="Lore",
            description="some lore description",
            pages=50,
            available=False,
            price=23.69,
            release=datetime.now() + timedelta(days=10),
        )

    def test_book_author_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("author").verbose_name
        self.assertEqual(field_label, "author")
    
    def test_book_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "title")

    def test_book_author_max_length(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("author").max_length
        self.assertEqual(field_label, 40)
    
    def test_book_title_max_length(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("title").max_length
        self.assertEqual(field_label, 100)

    def test_book_object_name(self):
        book = Book.objects.get(id=1)
        expected_book_name = book.title
        self.assertEqual(str(book), expected_book_name)