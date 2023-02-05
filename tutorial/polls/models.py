"""Model を定義
"""

from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    """質問
    django.db.models.Model のサブクラス
    """
    # 質問内容
    question_text = models.CharField(max_length=200)
    # 公開日時
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)


class Choice(models.Model):
    """質問に対する選択肢
    django.db.models.Model のサブクラス
    """
    # That tells Django each Choice is related to a single Question.
    # Question に紐付いた外部キー
    # models.CASCADE: Question の削除時、外部キーで紐付いた Choise も削除
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 選択肢内容
    choice_text = models.CharField(max_length=200)
    # 投票数
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
