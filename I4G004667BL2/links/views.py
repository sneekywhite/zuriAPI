from django.shortcuts import render

from links.serializer import LinkSerializer
from .models import link
from .serializer import LinkSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView,UpdateAPIView, DestroyAPIView

# Create your views here.
class PostListApi(ListAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostDetailApi(RetrieveAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostUpdateApi(UpdateAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostDeleteApi(DestroyAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostCreateApi(CreateAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer

