from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getImages(request):
  routes = [
    {
      'image_url': 'https://media1.giphy.com/media/S4H2ZREgH8c2EG6TmV/giphy.gif'
    },
  ]
  return Response(routes)
