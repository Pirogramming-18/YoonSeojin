from django.db import models

class Tools(models.Model) :
    toolName = models.CharField(max_length=100)
    toolCategory = models.CharField(max_length=100)
    toolContent = models.TextField()

toolCategories = []
for c in toolCategories.objects.all():
    cat = (c.toolName, c.toolName)
    toolCategories.append(cat)

class Ideas(models.Model) :
    ideaName = models.CharField(max_length=100)
    ideaImg = models.ImageField(blank=True, upload_to='posts/%Y%m%d')
    ideaContent = models.TextField()
    ideaInterest = models.IntegerField()
    ideaTool = models.CharField(max_length=64, choices=tuple(toolCategories), null=True, blank=True)
    ideaLike = models.ManyToManyField('IdeaLike', related_name='likes', blank=True)


class IdeaLike(models.Model) :
    idea = models.ForeignKey('Ideas', null=True, blank=True)