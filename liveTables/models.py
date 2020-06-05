from django.db import models
import http.client
import json
from django.core.exceptions import ValidationError

class Match(models.Model):
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    home_score = models.IntegerField(blank=True, null=True, default=None)
    away_score = models.IntegerField(blank=True, null=True, default=None)
    result = models.CharField(max_length=4)
    match_number = models.IntegerField(unique=True)
    status = models.CharField(max_length = 15)

    class Meta:
        verbose_name_plural = 'Matches'

    def setResult(self):
        if(self.home_score != None and self.away_score != None):
            if(self.home_score == self.away_score):
                self.result = "Draw"
            elif(self.home_score > self.away_score):
                self.result = "Home"
            elif(self.home_score < self.away_score):
                self.result = "Away"
        else:
            self.result = ""
    
    def __str__(self):
        home_value = "-"
        away_value = "-"
        if(self.home_score != None):
            home_value = str(self.home_score)
        if(self.away_score != None):
            away_value = str(self.away_score)
        return self.home_team + " " + str(home_value) + " v. " + str(away_value) + " " + self.away_team + " " + str(self.match_number)

    def validate_unique(self, *args, **kwargs):
        super(Match, self).validate_unique(*args, **kwargs)
        qs = Match.objects.filter(match_number=self.match_number)
        if qs.filter(match_number=self.match_number).exists():
            print(self.home_team + self.away_team)
            raise ValidationError({'match_number':['Number must be unique per match',]})
        
    
    def save(self, *args, **kwargs):
        super(Match, self).save(*args, **kwargs)
   
class Team(models.Model):
    name = models.CharField(max_length = 100)
    matches = models.ManyToManyField(Match)

    def __str__(self):
        return self.name