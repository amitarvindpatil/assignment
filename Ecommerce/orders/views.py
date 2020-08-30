from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Product,OrderItem,Order
from .serializers import ProductSerializers,OrderSerializers,OrderItemSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from User_Profile import permissions

# ---------Product API----------------------------
@permission_classes([IsAuthenticated])
class get_post_product(ListCreateAPIView):
    serializer_class = ProductSerializers

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset

    # Get method of Product

    def get(self, request):
        get_data = self.get_queryset()
        serializer = ProductSerializers(get_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #  Post method of Product
    def post(self, request):
        serializer = ProductSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {'message': 'Product Saved!'}
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

# For Delete the product------------------------------------------------
    # def delete(self, request, pk):
    #     get_data = self.get_queryset(pk)
    #     get_data.delete()
    #     content = {
    #         'message': 'Data Deleted!'
    #     }
    #     return Response(content, status=status.HTTP_204_NO_CONTENT)


@permission_classes([IsAuthenticated])
class get_delete_update_product(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializers

    def get_queryset(self, pk):
        try:
            get_query = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_400_NOT_FOUND)
        return get_query

    # Get the perticuler data of Product
    def get(self, request, pk):
        get_data = self.get_queryset(pk)
        serializer = ProductSerializers(get_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update the data of Product
    def put(self, request, pk):
        get_data = self.get_queryset(pk)
        serializer = ProductSerializers(get_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            content = {
                'message': 'Product Updated'
            }
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ---------orderItem----------------------------
@permission_classes([IsAuthenticated])
class get_post_orderitem(ListCreateAPIView):
    serializer_class = OrderItemSerializers

    def get_queryset(self):
        queryset = OrderItem.objects.all()
        return queryset

    # Get method

    def get(self, request):
        get_data = self.get_queryset()
        serializer = OrderItemSerializers(get_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderItemSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {'message': 'OrderItem Saved!'}
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
class get_delete_update_orderitems(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializers

    def get_queryset(self, pk):
        try:
            get_query = OrderItem.objects.get(pk=pk)
        except OrderItem.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_400_NOT_FOUND)
        return get_query

    # Get the perticuler data of orderitem
    def get(self, request, pk):
        get_data = self.get_queryset(pk)
        serializer = OrderItemSerializers(get_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update the data of orderitem
    def put(self, request, pk):
        get_data = self.get_queryset(pk)
        serializer = OrderItemSerializers(get_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            content = {
                'message': 'OrderItem Updated'
            }
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ---------order API ----------------------------
@permission_classes([IsAuthenticated])
class get_post_order(ListCreateAPIView):
    serializer_class = OrderSerializers

    def get_queryset(self):
        queryset = Order.objects.all()
        # authentication_classes = (TokenAuthentication,)
        return queryset

    # Get method

    def get(self, request):
        get_data = self.get_queryset()
        serializer = OrderSerializers(get_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {'message': 'Order Saved!'}
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
class get_delete_update_order(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializers

    def get_queryset(self, pk):
        try:
            get_query = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_400_NOT_FOUND)
        return get_query

    # Get the perticuler data of order
    def get(self, request, pk):
        get_data = self.get_queryset(pk)
        serializer = OrderSerializers(get_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update the data of order
    def put(self, request, pk):
        get_data = self.get_queryset(pk)
        serializer = OrderSerializers(get_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            content = {
                'message': 'Order Updated'
            }
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
