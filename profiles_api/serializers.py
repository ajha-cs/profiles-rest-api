from rest_framework import serializers

from profiles_api import models
#Serializer - class name - that's why caps
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    # This is a field that we want to accept input for
    # validation is done by serializer
    
    name = serializers.CharField(max_length=10)
        
class UserProfileSerializer(serializers.ModelSerializer):
    """Serialaize a user profile model"""
    
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password') 
        #password -> write_only - only used to create or update an object -> must not be retrieved
        #dictionary
        extra_kwargs = {
            'password': {
                'write_only': True,
                # ccustom style - only for browsable api
                'style': {'input_type': 'password'}
            }
        }
        
        # allows you to create simple obj in db - used default create function
        # overwrite this functionality -> so pwd created as a hash
        
    def create(self, validated_data):
        """Create and return  a new user"""
        user = models.UserProfile.objects.create_user(
            email= validated_data['email'],
            name= validated_data['name'],
            password= validated_data['password']
        )
        
        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}