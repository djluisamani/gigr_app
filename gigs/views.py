from rest_framework import generics
from .models import Gig, Payment, Client
from .serializers import GigSerializer, PaymentSerializer, ClientSerializer
from django.shortcuts import render


class GigList(generics.ListCreateAPIView):
    queryset = Gig.objects.all()
    serializer_class = GigSerializer

class GigDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gig.objects.all()
    serializer_class = GigSerializer

class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

def splash(request):
    return render(request, 'gigr_app/splash.html')