from rest_framework import generics
from .models import Owner, Animal
from .serializers import OwnerSerializer, AnimalSerializer

class OwnerList(generics.ListCreateAPIView):
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()

class OwnerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()

class AnimalList(generics.ListCreateAPIView):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()

    # def get_queryset(self):
        # queryset = Animal.objects.all()
        # owner = self.request.query_params.get('owner')
        # if owner is not None:
            # queryset = queryset.filter(owner=owner)
        # return queryset

class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()