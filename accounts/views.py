from django.shortcuts import render  # Django Funktion, Parameter werden uebergeben
from django.http import HttpResponse  # Statustext
from .models import BankAccount, TransactionModel
from .forms import TransactionForm
from django.contrib.auth.decorators import login_required
import json         #Java Script oriented notation



def hello(request):
    return render(request, 'accounts/landingpage.html')  #


@login_required
def myprofile(request):
    user = request.user
    accounts = BankAccount.objects.filter(user=user)
    return render(request, 'accounts/myprofile.html', {"accounts": accounts, "user": user})


@login_required
def myaccount(request, iban):
    account = BankAccount.objects.filter(
        iban=iban).first()  # SQL Abfrage - Vergleich Variable mit Klassenattribut, first fuer Objekt aus Query Set = Array
    acc_sender = TransactionModel.objects.filter(sen_account=account)
    acc_receiver = TransactionModel.objects.filter(rec_account=account)
    context = {
        "account": account, 
        "acc_sender": acc_sender, 
        "acc_receiver": acc_receiver,
    }
    user = request.user
    if account:
        if user == account.user:
            return render(request, 'accounts/myaccount.html', context)
        else:
            return HttpResponse("You have no authority for this account")
    else:
        return HttpResponse("The requested account doesn't exist")

@login_required
def transaction(request):
    context = {
        "trans_form": TransactionForm,
    }
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data['message'])
            #html returns iban as string
            rec_account = form.cleaned_data['rec_account']
            sen_account = form.cleaned_data['sen_account']
            amount = form.cleaned_data['amount']
            message = form.cleaned_data['message']
            # SQL query iban string -> Bankaccount.object, compares the committed html iban with iban in db
            account_owner = BankAccount.objects.filter(iban=sen_account).first()
            receiving_account = BankAccount.objects.filter(iban=rec_account).first()
            #new transaction saved as line in db
            new_object = TransactionModel(rec_account=receiving_account,sen_account=account_owner,message=message,amount=amount)
            new_object.save()

            if account_owner.balance > float(amount):
                #calculate new balance after transaction and save it in db
                account_owner.balance = account_owner.balance - float(amount)
                account_owner.save()
                receiving_account.balance = receiving_account.balance + float(amount)
                receiving_account.save()
            else:
                context["info_text"] = "Not enough money for the transaction"
    return render(request, 'accounts/transaction.html', context)


@login_required
def alltransactions(request):
    '''
    "__" kann man uber ein foreignkey auf ein attribut des verbundenen objectes
    zugreifen. sen_account__user greift also uber den foreignkey vom TransactionModel auf das "user"
    attribut vom "BankAccount(Model)" zu.
    Somit erhalten wir alle transaktionen die vom user gesendet wurden (egal von welchem BankAccount)

    '''
    acc_sender = TransactionModel.objects.filter(sen_account__user=request.user) #request.user = derzeitiger user
    acc_receiver = TransactionModel.objects.filter(rec_account__user=request.user)
    context = {
        "acc_sender":acc_sender, 
        "acc_receiver":acc_receiver
    }
    # die beiden variablen (acc_trans,acc_trans2) werden als context ans HTML ubergeben
    return render(request, 'accounts/alltransactions.html', context)


def checkiban(request, iban):
    account = BankAccount.objects.filter(
        iban=iban).first()  # SQL Abfrage - Vergleich Variable mit Klassenattribut, first fuer Objekt aus Query Set = Array
    if account:
        return HttpResponse("Die Iban: " + iban + " ist korrekt")
    return HttpResponse("Die eingegebene Iban: " + iban + " ist nicht korrekt. Gebe die Iban erneut ein")


@login_required
def checkiban_sender_api(request, iban):
    user = request.user
    account = BankAccount.objects.filter(iban=iban).first()
    #print(user)
    #print(account.user)
    if account and user == account.user: #if account exist and user matches the account owner
        example = {"answer": True}
    else:
        example = {"answer": False}
    return HttpResponse(json.dumps(example))    #host replys with HttpResponse to the client/ Browser --> transaction.html, in terminal states 200 for ok


@login_required
def checkiban_receiver_api(request, iban):
    user = request.user
    account = BankAccount.objects.filter(iban=iban).first()
    if account:
        example = {"answer": True}
    else:
        example = {"answer": False}
    return HttpResponse(json.dumps(example))   


@login_required
def checkamount_sender_api(request, amount, iban):
    user = request.user
    account = BankAccount.objects.filter(iban=iban).first()
    if account and user == account.user: 
        if float(amount) < account.balance:
            example = {"answer": True}
        else:
            example = {"answer": False}
    else:
        example = {"answer": False}
    return HttpResponse(json.dumps(example))    