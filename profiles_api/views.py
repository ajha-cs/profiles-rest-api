from rest_framework.views import APIView
# return standard responses when dj called our api view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import models
from profiles_api import permissions
#status - list of handy http status codes
# 200 - ok
# 201 - created
# 400 - bad request
# 401 - unauthorized
# 403 - forbidden
# 404 - not found
# 500 - internal server error

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    #Allows us to define application logic for our endpoint (url) -
    # we gonna assigned to this view -> djrestfmwk assigned the url to the view 
    # and it handle as per http request made 
    
    #get - to get list or single object
    
    # serialiser tell our api view to what to expect when making post/pu/pthc request to our api
    
    serializer_class = serializers.HelloSerializer 
    
    def get(self, request, format=None):
        #request - passed by djrestfmwk
        #format - suffix to end of endpoint url
        """Returns a list of APIView features"""
        
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        
        #return a response object
        #Response(dictionary or list) get op-d when api is called
        # response object converted to - convert to json
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self,request):
        """Create a hello message with our name"""
        #request - passed by djrestfmwk
        #format - suffix to end of endpoint url
        
        serializer = self.serializer_class(data=request.data)
        #self.serializer_class - get the serializer class assigned to this view
        #data=request.data - get the data that was passed in the request
        #serialiser validate the data 
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            #serializer.errors - give the dictionary of errors based on validation rules
            #by default - 200 ok is returned
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )
            
    def put(self, request, pk=None):
        """Handle updating an object"""
        #update the enitre object with waht wee provided in the request
        #pk - primary key - used to specify a specific object (specific url key) 
        # like id of the object
        #replacing the object with the object provided in the request
        
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        
        #update only the fields provided in the request
        # only updates the fields that are provided in the request
        
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """Delete an object"""
        
        #delete the object
        
        return Response({'method': 'DELETE'})
    
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    #ViewSet - class that provides functionality to manage models through http methods
    
    #list - typically a HTTP GET  to the root linked to the viewset
    #create - typically a HTTP POST to the root linked to the viewset
    #retrieve - typically a HTTP GET to a specific object linked to the viewset
    #update - typically a HTTP PUT to a specific object linked to the viewset
    #partial_update - typically a HTTP PATCH to a specific object linked to the viewset
    
    serializer_class = serializers.HelloSerializer
    
    def list(self,request):
        """Return a hello message"""
        # just like above an_apiview here a_viewset
        
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]
        
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Create a new Hello Message"""
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )
            
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        
        return Response({'method': 'GET'})
    
    def update(self, request, pk=None):
        """Handle updating an object"""
        
        return Response({'method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        
        return Response({'method':'PATCH'})
    
    def destroy(self, request, pk=None):
        """Handle removing an object"""
        
        return Response({'method':'DELETE'})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    #queryset - list of objects that we want to manage
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    #we can add multiple authentication classes
    #created as tuple , is added - multiple authentication classes
    #ModelViewSet - standard viewset that automatically generates list, create, retrieve, update, partial_update, destroy    
    filter_backends = (filters.SearchFilter,)
    # , added to make it a tuple
    search_fields = ('name','email',)
    #search_fields - list of fields that we want to enable search on

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    #ObtainAuthToken - standard view provided by djrestfmwk
    # that we can add to our api to provide a login endpoint
    # To make it visible in admin website
    
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
    #renderer_classes - standard setting provided by djrestfmwk
    # to enable the view to be rendered in the browser

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    
    serializer_class = serializers.ProfileFeedItemSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )
    
    #we wannaset user_profile to read on;y
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        # get called every time POST request is made to our view set
        # since token authentication is added to our view set if user has auth-d then request will have user when user is authenticated
        serializer.save(user_profile=self.request.user)