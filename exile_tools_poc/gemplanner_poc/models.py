from django.db import models

class POESkillGem(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=1)
    gemtype = models.CharField(max_length=20)

class POECharacterClass(models.Model):
    name = models.CharField(max_length=200)

class POEQuest(models.Model):
    name = models.CharField(max_length=200)

class POECharSkillGemMapping(models.Model):
    skill_gem_id = models.IntegerField()
    class_id = models.IntegerField()
    min_level = models.IntegerField()
