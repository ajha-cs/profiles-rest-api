from rest_framework.views import APIView
# return standard responses when dj called our api view
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    #Allows us to define application logic for our endpoint (url) -
    # we gonna assigned to this view -> djrestfmwk assigned the url to the view 
    # and it handle as per http request made 
    
    #get - to get list or single object
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
    