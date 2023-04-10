from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import Count,Q


# Create your models here.

class VocabularyModel(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    en = models.CharField(verbose_name='EN', max_length=200)
    ru = models.CharField(verbose_name='RU', max_length=200)

    def save(self, *args, **kwargs):  # перевод полей мой базы данных в lower стринг
        self.en = self.en.lower()
        self.ru = self.ru.lower()
        #ORM ЗАПРОС В БАЗУ ДАННЫХ ЧТОБЫ УБРАТЬ ВСЕ ДУПЛИКАТЫ
        w1 = VocabularyModel.objects.values('en', 'userid').annotate(en_count=Count('en'),user_count=Count('userid', distinct=True)).filter(en_count__gt=1, user_count__lte=1)
        for i in w1:
            en = i['en']
            userid = i['userid']
            roro = VocabularyModel.objects.filter(Q(en=en) & Q(userid=userid)).order_by('pk')
            for j in range(len(roro)):
                roro[j].delete()



        return super(VocabularyModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.en




class TestWordsModel(models.Model):
    UserID=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    translate=models.CharField(verbose_name='Перевод',max_length=100)



    def save(self, *args ,**kwargs):
        self.translate=self.translate.lower()
        return super(TestWordsModel,self).save(*args,**kwargs)
