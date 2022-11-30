from rest_framework import serializers
from .models import *


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'Title', 'Description', 'Date', 'Completed')

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id','Item','Quantity','Price')
class BarnMgtSerialzer(serializers.ModelSerializer):
    class Meta:
        model = BarnMgt
        feilds = ('id','Product','Quantity','Price')
        fields = '__all__'
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','Name','Length','Breadth','email','Phone_no','Tags')
        fields = '__all__'

