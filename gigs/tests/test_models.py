from django.test import TestCase
from gigs.models import Client, Gig, Payment


class ClientTestCase(TestCase):
    def setUp(self):
        self.client = Client.objects.create(
            name="John Doe", email="johndoe@example.com")

    def test_client_creation(self):
        self.assertEqual(self.client.name, "John Doe")
        self.assertEqual(self.client.email, "johndoe@example.com")


class GigTestCase(TestCase):
    def setUp(self):
        self.client = Client.objects.create(
            name="John Doe", email="johndoe@example.com")
        self.gig = Gig.objects.create(
            title="Test Gig", date="2023-05-01", location="Test Location", client=self.client)

    def test_gig_creation(self):
        self.assertEqual(self.gig.title, "Test Gig")
        self.assertEqual(str(self.gig.date), "2023-05-01")
        self.assertEqual(self.gig.location, "Test Location")
        self.assertEqual(self.gig.client, self.client)


class PaymentTestCase(TestCase):
    def setUp(self):
        self.client = Client.objects.create(
            name="John Doe", email="johndoe@example.com")
        self.gig = Gig.objects.create(
            title="Test Gig", date="2023-05-01", location="Test Location", client=self.client)
        self.payment = Payment.objects.create(amount=500, gig=self.gig)

    def test_payment_creation(self):
        self.assertEqual(self.payment.amount, 500)
        self.assertEqual(self.payment.gig, self.gig)
