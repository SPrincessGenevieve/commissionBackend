from django.shortcuts import render


from rest_framework import viewsets


from .serializers import LocalSerializer


from .models import Describe


class LocalView(viewsets.ModelViewSet):


	serializer_class = LocalSerializer
	queryset = Describe.objects.all()
