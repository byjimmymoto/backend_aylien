from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import AylienUrl, AylienSentiment, AylienClassify, AylienConcepts, AylienEntities, AylienSummary


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class AylienSentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AylienSentiment
        fields = ('polarity', 'subjectivity', 'polarity_confidence', 'subjectivity_confidence', 'text')


class AylienClassifySerializer(serializers.ModelSerializer):
    class Meta:
        model = AylienClassify
        fields = ('language', 'text', 'categories')


class AylienConceptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AylienConcepts
        fields = ('language', 'text', 'concepts')


class AylienEntitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AylienEntities
        fields = ('language', 'text', 'entities')


class AylienSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = AylienSummary
        fields = ('text', 'sentences')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class AylienUrlSerializer(serializers.ModelSerializer):
    sentiment = AylienSentimentSerializer(many=True)
    classify = AylienClassifySerializer(many=True)
    concepts = AylienConceptsSerializer(many=True)
    entities = AylienEntitiesSerializer(many=True)
    summary = AylienSummarySerializer(many=True)

    class Meta:
        model = AylienUrl
        fields = ('id', 'url', 'sentiment', 'classify', 'concepts', 'entities', 'summary',)


class AylienUrlBasicSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.URLField(max_length=200)

    class Meta:
        model = AylienUrl
        fields = ('id', 'url',)
