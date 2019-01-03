from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# account attr = iban, pin, balance, username, failed_attempts, status

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    objects = models.Manager()

    class Meta:
        ordering = ['-user']


class BankAccount(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=200, blank=True)
    iban = models.CharField(max_length=200)
    pin = models.IntegerField()
    balance = models.FloatField()
    failed_attempts = models.IntegerField()
    status = models.BooleanField(default=True)
    objects = models.Manager()

    class Meta:
        ordering = ['-iban']

    # def __unicode__(self):
    #     return '{}'.format(self.username)

    def __str__(self):
        return 'iban {}'.format(self.iban)


class TransactionModel(models.Model):
    rec_account = models.ForeignKey(BankAccount, null=True, on_delete=models.CASCADE,
                                    related_name="receiving_account")  # receiving account
    sen_account = models.ForeignKey(BankAccount, null=True, on_delete=models.CASCADE,
                                    related_name="sending_account")  # sending account
    message = models.CharField(max_length=500, blank=True)  # Verwendungszweck
    date = models.DateTimeField(auto_now_add=True, blank=True)
    amount = models.FloatField()

    def __str__(self):
        return 'von: {}, an {}'.format(self.sen_account, self.rec_account)


# def check1(iban):
#     account = Accounts.objects.get(id=iban) #select from account where id = iban
#     if account.status == "ok":
#         return account
#     elif account.status == "blocked":
#         exec("keep card")
#     else:
#         exec("return card")


# def check2(pin, amount, iban):
#     account = check1(iban)
#     afa = account.failed_attempts
#     if pin == account.pin:
#         afa = 0
#         if amount <= account.balance:
#             #balance - amount
#             exec("return "+amount)
#         else:
#             print("not enough money")
#     else:
#         afa += 1
#         if afa == 3:
#             exec("keep card")
#             print("The card is blocked")
#             account.status = "blocked"
