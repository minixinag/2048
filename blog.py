from django.db import models

#Create your models here.

class Article(models.Model):
  tilte = models.CharField(max_length=100) #文章的标题
  category = models.CharField(max_length=5,blank=True) #文章的分类
  date_time = models.DateTimeField(auto_now_add=Ture) #文章创建时间
  content = models.TextField(blank=Ture,null=True) #文章内容
  
  def __unicode__(self): #__str__
    return self.title
  class Meta: #排序
    ordering = ['-date_time']
