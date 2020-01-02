from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from backend_aylien.aylien.serializers import UserSerializer, AylienUrlBasicSerializer,\
    GroupSerializer, AylienUrlSerializer
from .models import AylienUrl, AylienSentiment, AylienClassify, AylienConcepts, AylienEntities, AylienSummary
from aylienapiclient import textapi


class UserViewSet(viewsets.ModelViewSet):
    # View of User registers
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    # View of Groups
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser]


class AylienUrlViewSet(viewsets.ModelViewSet):
    # View of Aylien query
    queryset = AylienUrl.objects.all()
    serializer_class = AylienUrlSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        Display list of urls upload of users
        :param request: receive data
        :return: serializer urls of user
        """
        queryset = AylienUrl.objects.filter(user=request.user)
        serializer = AylienUrlBasicSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, pk=None):
        """
        Function of create new urls and send to Aylien
        :param request: receive data
        :param pk: id to create
        :return: serializer url of user with Aylien response
        """
        urlAylien = AylienUrl(url=request.data['url'], user=request.user)
        urlAylien.save()
        urls = AylienUrl.objects.filter(user=request.user)
        clientApiAylien(urlAylien)
        serializer = AylienUrlBasicSerializer(urls, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Function of update urls and resend to Aylien
        :param request:  receive data
        :param pk: id to update
        :return: serializer url of user with Aylien response
        """
        urlAylien = AylienUrl(url=request.data['url'], user=request.user)
        urlAylien.save()
        urls = AylienUrl.objects.filter(user=request.user)
        clientApiAylien(urlAylien)
        serializer = AylienUrlBasicSerializer(urls, many=True)
        return Response(serializer.data)


def clientApiAylien(urlAylien):
    """
    Function of request of API Aylien
    :param urlAylien: Url to send
    :return: None
    """
    url = urlAylien.url
    client = textapi.Client("36d9f8a0", "e764896220f148f153bd8297869ab1d5")
    sentiment = client.Sentiment({'url': url})
    aylienSentiment = AylienSentiment(url=urlAylien, polarity=sentiment['polarity'], subjectivity=sentiment['subjectivity'],
                                      text=sentiment['text'], polarity_confidence=sentiment['polarity_confidence'],
                                      subjectivity_confidence=sentiment['subjectivity_confidence'])
    classify = client.Classify({'url': url})
    aylienClassify = AylienClassify(url=urlAylien, language=classify['language'], text=classify['text'],
                                    categories=classify['categories'])
    concepts = client.Concepts({'url': url})
    aylienConcepts = AylienConcepts(url=urlAylien, language=concepts['language'], text=concepts['text'],
                                    concepts=concepts['concepts'])
    entities = client.Entities({'url': url})
    aylienEntities = AylienEntities(url=urlAylien, language=entities['language'], text=entities['text'],
                                    entities=entities['entities'])
    summary = client.Summarize(url)
    aylienSummary = AylienSummary(url=urlAylien, text=summary['text'], sentences=summary['sentences'])

    aylienSentiment.save()
    aylienClassify.save()
    aylienConcepts.save()
    aylienEntities.save()
    aylienSummary.save()




