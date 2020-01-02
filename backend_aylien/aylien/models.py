from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class AylienUrl(models.Model):
    url = models.URLField(max_length=200, help_text="Url to analysis of Aylien")
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, help_text="User to send analysis")
    created_at = models.DateTimeField(auto_now=True, help_text="Date of url analysis with Aylien")

    def __str__(self):
        return self.URLField


class AylienSentiment(models.Model):
    url = models.ForeignKey(AylienUrl, blank=True,  on_delete=models.CASCADE, related_name='sentiment',
                            help_text="Url to analysis")
    polarity = models.CharField(max_length=200, blank=True, help_text="Aylien polarity sentiment analysis")
    subjectivity = models.CharField(max_length=200, blank=True, help_text="Aylien subjectivity sentiment analysis")
    text = models.TextField(blank=True, help_text="Aylien subjectivity sentiment analysis")
    polarity_confidence = models.DecimalField(max_digits=10, decimal_places=2,
                                             help_text="Aylien polarityconfidence sentiment analysis")
    subjectivity_confidence = models.DecimalField(max_digits=10, decimal_places=2,
                                                 help_text="Aylien subjectivityconfidence sentiment analysis")

    class Meta:
        unique_together = ('url', 'polarity')

    def __unicode__(self):
        return '%s: %s' % (self.polarity, self.subjectivity)

    def __str__(self):
        return self.text


class AylienClassify(models.Model):
    url = models.ForeignKey(AylienUrl, blank=True, on_delete=models.CASCADE, related_name='classify',
                            help_text="Url to analysis")
    language = models.CharField(max_length=200, blank=True, help_text="Aylien language classify analysis")
    text = models.TextField(blank=True, help_text="Aylien text classify analysis")
    categories = models.TextField(blank=True, help_text="Aylien categories classify analysis")

    def __str__(self):
        return self.text


class AylienConcepts(models.Model):
    url = models.ForeignKey(AylienUrl, blank=True, on_delete=models.CASCADE, related_name='concepts',
                            help_text="Url to analysis")
    language = models.CharField(max_length=200, blank=True, help_text="Aylien language concepts analysis")
    text = models.TextField(blank=True, help_text="Aylien text concepts analysis")
    concepts = models.TextField(blank=True, help_text="Aylien concepts analysis")

    def __str__(self):
        return self.text


class AylienEntities(models.Model):
    url = models.ForeignKey(AylienUrl, blank=True, on_delete=models.CASCADE, related_name='entities',
                            help_text="Url to analysis")
    language = models.CharField(max_length=200, blank=True, help_text="Aylien language entities analysis")
    text = models.TextField(blank=True, help_text="Aylien text entities analysis")
    entities = models.TextField(blank=True, help_text="Aylien entities analysis")

    def __str__(self):
        return self.text


class AylienSummary(models.Model):
    url = models.ForeignKey(AylienUrl, blank=True, on_delete=models.CASCADE, related_name='summary',
                            help_text="Url to analysis")
    text = models.TextField(blank=True, help_text="Aylien text summary analysis")
    sentences = models.TextField(blank=True, help_text="Aylien sentences summary analysis")

    def __str__(self):
        return self.text