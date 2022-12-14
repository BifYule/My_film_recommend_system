# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApiTestBook(models.Model):
    id = models.BigAutoField(primary_key=True)
    book_name = models.CharField(max_length=128)
    add_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'api_test_book'


class ApiTestUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=128)
    user_password = models.IntegerField()
    add_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'api_test_user'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Movies(models.Model):
    movie_id = models.CharField(db_column='MOVIE_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(db_column='ALIAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    actors = models.CharField(db_column='ACTORS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cover = models.CharField(db_column='COVER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    directors = models.CharField(db_column='DIRECTORS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    douban_score = models.CharField(db_column='DOUBAN_SCORE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    douban_votes = models.CharField(db_column='DOUBAN_VOTES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    genres = models.CharField(db_column='GENRES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imdb_id = models.CharField(db_column='IMDB_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    languages = models.CharField(db_column='LANGUAGES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mins = models.CharField(db_column='MINS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    official_site = models.CharField(db_column='OFFICIAL_SITE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regions = models.CharField(db_column='REGIONS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    release_date = models.CharField(db_column='RELEASE_DATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    slug = models.CharField(db_column='SLUG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storyline = models.TextField(db_column='STORYLINE', blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='TAGS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='YEAR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    actor_ids = models.CharField(db_column='ACTOR_IDS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    director_ids = models.CharField(db_column='DIRECTOR_IDS', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movies'
