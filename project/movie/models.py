from django.db import models

# Create your models here.

class country(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', auto_created=True)
    c_name = models.CharField('国家名',max_length=20)

    def __str__(self):
        return self.c_name

class actors(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', auto_created=True)
    a_name = models.CharField('演员',max_length=100)

    def __str__(self):
        return self.a_name

class type(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', auto_created=True)
    type = models.CharField('电影类型',max_length=20)

    def __str__(self):
        return self.type


class movies(models.Model):
    id = models.AutoField(primary_key=True, db_column='id',auto_created=True)
    title = models.CharField('标题',max_length=100)
    cover = models.ImageField('封面',upload_to='static/images')
    director = models.CharField('导演',max_length=100)
    m_actors = models.ManyToManyField(actors,related_name='actorname')
    type = models.ManyToManyField(type,related_name='movietype')
    country = models.ManyToManyField(country,related_name='movieconutry')
    date = models.DateField('上映时间')
    hits = models.IntegerField('点击量',default=0)

    def __str__(self):
        return self.title


class comments(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', auto_created=True)
    content = models.TextField('评论')
    date = models.DateTimeField('评论时间', auto_now_add=True)
    movie = models.ForeignKey(movies, related_name='moviecomments', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)