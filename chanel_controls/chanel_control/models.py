from django.db import models

class Users(models.Model):
    telegram_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=255, null=True)
    full_name = models.CharField(max_length=255, null=True)
    create_at =models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'User: {self.telegram_id}'

class Orders(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    order_info = models.JSONField()
    amount = models.DecimalField(max_digits=16, decimal_places=4)
    paid = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Transaction(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    pay_address = models.CharField(max_length=255)
    currency = models.CharField(max_length=16)
    usd_amount = models.DecimalField(max_digits=16, decimal_places=4)
    pay_amount = models.DecimalField(max_digits=16, decimal_places=8)
    paid = models.BooleanField(default=False)
    payment_id = models.IntegerField(null=True)
    order =  models.ForeignKey(Orders, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=255, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'transaction'

class PaidContent(models.Model):
    id = models.BigIntegerField(primary_key=True)
    content_name = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)
    content_HTML = models.CharField(max_length=2047, null=True)

    class Meta:
        db_table = 'paid_content'

