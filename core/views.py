from rest_framework import generics, permissions
from .serializers import *
from rest_framework.response import Response
from .models import *




class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
class DeleteTodo(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
class ListInventory(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
class CreateInventory(generics.CreateAPIView):
    queryset = Inventory
    serializer_class = InventorySerializer
class DeleteInventory(generics.DestroyAPIView):
    queryset = Inventory
    serializer_class = InventorySerializer
class ListBarnMgt(generics.ListAPIView):
    queryset = BarnMgt.objects.all()
    serializer_class = BarnMgtSerialzer
class CreateBarnMgt(generics.CreateAPIView):
    queryset = BarnMgt
    serializer_class = BarnMgtSerialzer
class DeleteBarnMgt(generics.DestroyAPIView):
    queryset = BarnMgt
    serializer_class = BarnMgtSerialzer
class CreateProfile(generics.CreateAPIView):
    queryset = Profile
    serializer_class = ProfileSerializer


class ListProfiles(generics.ListAPIView):
    queryset = Profile
    serializer_class = ProfileSerializer

# class CreateProfile(generics.GenericAPIView):
#     serializer_class = ProfileSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         Profile = serializer.save()
#         return Response({
#         "Profile": ProfileSerializer(Profile, context=self.get_serializer_context()).data,
#         "token": AuthToken.objects.create(Profile)[1]
#         })