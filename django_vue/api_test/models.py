from __future__ import unicode_literals
from django.db import models

#用户信息表
class User(models.Model):
    user_name = models.CharField(max_length=128)
    user_password= models.IntegerField("密码", default=20)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user_name



#电影数据
class Movies(models.Model):
    MOVIE_ID = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    NAME = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    ALIAS = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    ACTORS = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    COVER = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    DIRECTORS = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    DOUBAN_SCORE = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    DOUBAN_VOTES = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    GENRES = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    IMDB_ID = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    LANGUAGES = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    MINS = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    OFFICIAL_SITE = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    REGIONS = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    RELEASE_DATE = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    SLUG = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    STORYLINE = models.TextField(blank=True, null=True)  # Field name made lowercase.
    TAGS = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    YEAR = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    ACTOR_IDS = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    DIRECTOR_IDS = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.

    
    def __unicode__(self):
        return self.MOVIE_ID

#热门电影
class popular_movies(models.Model):
    MOVIE_ID = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    NAME = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    ALIAS = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    ACTORS = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    COVER = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    DIRECTORS = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    DOUBAN_SCORE = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    DOUBAN_VOTES = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    GENRES = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    IMDB_ID = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    LANGUAGES = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    MINS = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    OFFICIAL_SITE = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    REGIONS = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    RELEASE_DATE = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    SLUG = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    STORYLINE = models.TextField(blank=True, null=True)  # Field name made lowercase.
    TAGS = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    YEAR = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    ACTOR_IDS = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    DIRECTOR_IDS = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
        return self.name


#评价表
class Commendts(models.Model):
    COMMENT_ID = models.CharField(max_length=255, blank=True, null=True)
    USER_MD5 = models.CharField(max_length=255, blank=True, null=True)
    MOVIE_ID = models.CharField(max_length=255, blank=True, null=True)
    CONTENT = models.TextField(max_length=255, blank=True, null=True)
    VOTES = models.CharField(max_length=255, blank=True, null=True)
    COMMENT_TIME = models.CharField(max_length=255, blank=True, null=True)
    RATING = models.CharField(max_length=255, blank=True, null=True)
    
    def __unicode__(self):
        return self.name



#用户评价表
class User_evaluate(models.Model):
    MOVIE_ID = models.CharField(max_length=255, blank=True, null=True)
    USER_NAME = models.CharField(max_length=255, blank=True, null=True)
    MOVIE_NAME = models.CharField(max_length=255, blank=True, null=True)
    SCORE = models.IntegerField( blank=True, null=True)


    def __unicode__(self):
            return self.name