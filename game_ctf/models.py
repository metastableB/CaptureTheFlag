#
# @author:metastableB
# models.py
# 
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from CaptureTheFlag.settings import BASE_DIR

class Question(models.Model):
	valid = models.BooleanField(default = True)
	# @metastableB : useage of FilePathField might not be as straight forward
	# refer to the documentation
	source_file = models.FilePathField(path=BASE_DIR+"/Questions/")
	points = models.IntegerField()

'''
@metastableB : We are not using a leaderboard specific data structure for this app
	Our assumption is that the number of users will always remain under, say 1000.
	This means we can afford to query this table, and sort the users according to
	the points alloted to populate the leaderboard.

	In case the number of users gets significant or this querying gets slow, we will
	have to resort to a better LeaderBoard ranking system and scheme, like the ones
	followed by steam/counter_strike/SO etc
'''
class PointsPerUser(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	points = models.IntegerField(default = 0)

