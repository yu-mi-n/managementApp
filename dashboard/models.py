from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=100)
    # 仮想残高（ペソ）
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    # 引き出し目標額
    target_balance = models.DecimalField(max_digits=8, decimal_places=2, default=500.00)
    rank = models.CharField(max_length=50, default='ブロンズ')
    # 報酬倍率
    rank_multiplier = models.FloatField(default=1.0)

    @property
    def progress_percentage(self):
        """目標額に対する現在の達成率を計算"""
        if self.target_balance == 0:
            return 0
        percentage = (self.balance / self.target_balance) * 100
        return min(int(percentage), 100)

    def __str__(self):
        return self.name