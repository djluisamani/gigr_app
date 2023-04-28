from django.test import Client, TestCase
from django.urls import reverse
from gigs.models import Client


class ClientViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client.objects.create(
            name="John Doe", email="johndoe@example.com")

    def test_client_list_view(self):
        url = reverse('client_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")

    def test_client_detail_view(self):
        url = reverse('client_detail', args=[self.client.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")
        self.assertContains(response, "johndoe@example.com")
