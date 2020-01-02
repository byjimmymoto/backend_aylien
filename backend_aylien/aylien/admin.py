from django.contrib import admin

from .models import AylienUrl, AylienSentiment, AylienClassify, AylienConcepts, AylienEntities, AylienSummary

admin.site.register(AylienUrl)
admin.site.register(AylienSentiment)
admin.site.register(AylienClassify)
admin.site.register(AylienConcepts)
admin.site.register(AylienEntities)
admin.site.register(AylienSummary)