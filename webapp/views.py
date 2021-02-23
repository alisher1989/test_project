from collections import OrderedDict
from django.views.generic import ListView
from djoser.conf import User
from rest_framework import permissions, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from webapp.models import Product
from webapp.serializer import ProductSerializer, UpdateUserSerializer, ChangePasswordSerializer


class IndexView(ListView):
    model = Product
    template_name = 'index.html'

    def get_queryset(self):
        queryset = Product.objects.filter(in_order=True)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context


class Pagination(PageNumberPagination):
    page_size = 4
    page_query_param = 'page_size'
    max_page_size = 200

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


class ProductView(ModelViewSet):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = Pagination
    permission_classes = [permissions.IsAuthenticated]


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChangePasswordSerializer