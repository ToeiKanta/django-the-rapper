from rest_framework import viewsets,status

from .serializers import ArtistSerializer,ArtistSaveSerializer
from .models import Artist

from rest_framework.decorators import api_view
from rest_framework.response import Response
class ArtistViewSet(viewsets.ModelViewSet):
  """
    This viewset automatically provides `list` and `detail` actions.
  """
  queryset = Artist.objects.all()
  serializer_class = ArtistSerializer

  @api_view(['GET'])
  def custom_list(self, format=None):
    queryset = Artist.objects.all()
    artist_serializer = ArtistSerializer(queryset,many=True)
    return Response(artist_serializer.data, status=status.HTTP_200_OK )

  @api_view(['POST'])
  def custom_create(self, format=None):
    artist_serializer = ArtistSaveSerializer(data=self.data)
    if artist_serializer.is_valid():
      artist_serializer.save()
      return Response(artist_serializer.data, status=status.HTTP_201_CREATED)
    return Response(artist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)