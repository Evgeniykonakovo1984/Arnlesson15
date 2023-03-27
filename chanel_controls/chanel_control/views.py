from django.shortcuts import render
from .models import Transaction, PaidContent

# Create your views here.


def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, "transaction_list.html", {"transactions":transactions})
    #return render(request, "base.HTML")

def index(request):
    paidcontents = PaidContent.objects.all()
    #transactions = Transaction1.objects.all()
    # return render(request, "transaction_list.html", {"transactions":transactions})
    return render(request, "index.html", {"paidcontents":paidcontents})

def list1(request):
    return render(request, "list1.html")


def list2(request):
    return render(request, "list2.html")