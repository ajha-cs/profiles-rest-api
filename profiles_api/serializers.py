from rest_framework import serializers
#Serializer - class name - that's why caps
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    # This is a field that we want to accept input for
    # validation is done by serializer
    
    name = serializers.CharField(max_length=10)
    