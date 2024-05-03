from django.test import TestCase

from orders.models import Book
from datetime import datetime


class CatalogViewTest(TestCase):

    def setUp(self) -> None:
        num_of_books = 15
        for book_id in range(num_of_books):
            Book.objects.create(
                author=f"Mike Vasovsky {book_id}",
                title="Monsters",
                description="some description",
                pages=100*book_id,
                available=True,
                price=123.69*book_id,
                release=datetime.now(),
            )
    
    def test_view_catalog_exist(self):
        response = self.client.get("/catalog/")
        print(response.templates)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog.html")
