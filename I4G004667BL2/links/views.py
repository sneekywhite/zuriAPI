from django.shortcuts import render

from links.serializer import LinkSerializer
from .models import link
from .serializer import LinkSerializer
from rest_framework.generics import ListAPIView

# Create your views here.
class PostListApi(ListAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostDetailApi(ListAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostUpdateApi(ListAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostDeleteApi(ListAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostCreateApi(ListAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer

