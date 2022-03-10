import json
from tokenize import group
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum
from home.models import *
from .forms import *
import math

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = request.user
        groups_joined_num = GroupMember.objects.filter(user = user).count()
        transactions_getter_num = Transaction.objects.filter(getter = user).count()
        transactions_spender_num = + Transaction.objects.filter(spender = user).count()
        purchases_num = Purchase.objects.filter(spender = user).count()
        groups_all = GroupMember.objects.filter(user = user)
        picture = prof_pic(request)
        transactions_num = transactions_getter_num + transactions_spender_num
        expenses = []
        for group in groups_all:
            user_money_spent = Transaction.objects.filter(spender = request.user, group = group.group)
            total_user_spent = 0.0
            for x in user_money_spent:
                total_user_spent += x.amount
            expenses.append(total_user_spent)
            

        # purchases = Purchase.objects.filter(spender = user)
        # transactions_getter = Transaction.objects.filter(getter = user)
        # transactions_spender = Transaction.objects.filter(spender = user)

        if groups_joined_num >=3:
            groups_joined = GroupMember.objects.filter(user = user)[groups_joined_num - 3:groups_joined_num]
        else:
            groups_joined = GroupMember.objects.filter(user = user)

        if transactions_getter_num >=3:
            transactions_getter = Transaction.objects.filter(getter = user)[transactions_getter_num - 3:transactions_getter_num]
        else:
            transactions_getter = Transaction.objects.filter(getter = user)
            
        if transactions_spender_num >=3:
            transactions_spender = Transaction.objects.filter(spender = user)[transactions_spender_num - 3:transactions_spender_num]
        else:
            transactions_spender = Transaction.objects.filter(spender = user)

        if purchases_num >=3:
            purchases = Purchase.objects.filter(spender = user)[purchases_num - 3: purchases_num]
        else:
            purchases = Purchase.objects.filter(spender = user)    

        context = {
            'groups_joined' : groups_joined,
            'groups_joined_num' : groups_joined_num,
            'transactions_getter_num' : transactions_getter_num,
            'transactions_spender_num' : transactions_spender_num,
            'purchases_num' : purchases_num,
            'purchases' : purchases,
            'transactions_getter' : transactions_getter,
            'transactions_spender' : transactions_spender,
            'groups_all': groups_all,
            'expenses': expenses,
            'transactions_num': transactions_num,
            'picture': picture,
        }
        return render(request, "index.html", context)
    else:
        return render(request, "login.html")    

@csrf_exempt
def login_my(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username= username, password= password)
    if user is not None:
        login(request, user)
        print("User Authenticated") 
        response_data = {
        'authenticated': 'yes',
        } 
    else:
        print("User Not Authenticated") 
        response_data = {
        'authenticated': 'no',
        }    
    return JsonResponse(response_data)

@csrf_exempt
def register_my(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    nickname = request.POST.get("nickname")
    user = User.objects.create_user(username, None , password)
    user.first_name = nickname
    user.save()
    response_data = {
        'created': 'yes',
    }
    login(request, user) 
    return JsonResponse(response_data)

def register_page(request):
    return render(request, "register.html")

def login_page(request):
    return render(request, "login.html")   

def logout_my(request):
    logout(request)
    response_data = {
        'logout': 'yes',
    }
    return JsonResponse(response_data)

def group_view(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    else: 
        user_needed = request.user
        groups_num = GroupMember.objects.filter(user = user_needed).count()
        groups_get = GroupMember.objects.filter(user = user_needed)
        picture = prof_pic(request)
        context = {
            "groups_get": groups_get,
            "groups_num": groups_num,
            'picture': picture,
        }
        return render(request, "group.html", context)

def group_details(request, groupid):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    else:
        group = Group.objects.get(id = groupid)
        group_members = GroupMember.objects.filter(group = group)
        group_members_count = GroupMember.objects.filter(group = group).count()
        purchases = Purchase.objects.filter(group = group)
        transactions = Transaction.objects.filter(group = group)
        purchases_num = Purchase.objects.filter(group = group).count()
        transactions_num = Transaction.objects.filter(group = group).count()
        user_money_spent = Transaction.objects.filter(spender = request.user, group = group)
        user_money_received = Transaction.objects.filter(getter = request.user, group = group)
        picture = prof_pic(request)

        total_user_spent = 0.0
        for x in user_money_spent:
            total_user_spent += x.amount

        for x in purchases:
            if x.spender == request.user:
                total_user_spent += (group_members_count -1)*(x.amount)

        total_user_received = 0.0
        for x in user_money_received:
            total_user_received += x.amount

        for x in purchases:
            if x.spender != request.user:
                total_user_received += x.amount

        if total_user_received - total_user_spent > 0:
            net_amount = total_user_received - total_user_spent
            status = "negative"
            getter = get_getter(request, groupid)
            getter_count = len(getter)
            if getter_count == 1:
                getter = getter[0] 
            context = {
            'group' : group,
            'group_members' : group_members,
            'purchases': purchases,
            'purchases_num': purchases_num,
            'transactions_num': transactions_num,
            'transactions': transactions,
            'user_money_spent': total_user_spent,
            'user_money_received': total_user_received,
            'status': status,
            'net_amount': net_amount,
            'picture': picture,
            'getter' : getter,
            'getter_count': getter_count,
            }
            print(getter)                    
        elif total_user_spent == total_user_received:
            net_amount = 0.0
            status = "neutral"
            context = {
            'group' : group,
            'group_members' : group_members,
            'purchases': purchases,
            'purchases_num': purchases_num,
            'transactions_num': transactions_num,
            'transactions': transactions,
            'user_money_spent': total_user_spent,
            'user_money_received': total_user_received,
            'status': status,
            'net_amount': net_amount,
            'picture': picture,
            }                
        else:
            net_amount = total_user_spent - total_user_received
            status = "positive"
            context = {
            'group' : group,
            'group_members' : group_members,
            'purchases': purchases,
            'purchases_num': purchases_num,
            'transactions_num': transactions_num,
            'transactions': transactions,
            'user_money_spent': total_user_spent,
            'user_money_received': total_user_received,
            'status': status,
            'net_amount': net_amount,
            'picture': picture,
            }    
        # print(net_amount)
        return render(request, "groupdetails.html", context)    


def get_getter(request, groupid):
    group = Group.objects.get(id = groupid)
    group_members = GroupMember.objects.filter(group = group)
    members_with_negative = []
    for member in group_members:
        if member.user != request.user:
            money_spent = 0
            money_get = 0
            total_transactions_spent = TotalTransaction.objects.filter(group = group, spender = member.user)
            total_transactions_get = TotalTransaction.objects.filter(group = group, getter = member.user)
            for x in total_transactions_spent:
                money_spent += x.amount
            for x in total_transactions_get:
                money_get += x.amount
            if money_get < money_spent:
                members_with_negative.append(member)
    return members_with_negative            

@csrf_exempt
def purchase_submit(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    else:
        spender = request.user
        topic = request.POST.get("topic")
        date = request.POST.get("date")
        details = request.POST.get("details")
        group = Group.objects.get(id = request.POST.get("id"))
        groupmembers = GroupMember.objects.filter(group = group)
        amount = request.POST.get("amount")
        new_purchase = Purchase.objects.create(spender = spender, topic = topic, datecreated = date, details = details, group = group, amount = amount)
        new_purchase.save()
        for member in groupmembers:
            if member.user != spender:
                new_totaltransaction = TotalTransaction.objects.create(spender = spender, amount = amount, getter = member.user, group = group)
                new_totaltransaction.save()
        response_data = {
           'message': 'successful',
        }

    return JsonResponse(response_data)    

@csrf_exempt
def transaction_submit(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    else:
        spender = request.user
        topic = request.POST.get("topic")
        group = Group.objects.get(id = request.POST.get("id"))
        amount = request.POST.get("amount")
        getter = User.objects.get(id = request.POST.get("getter_id"))
        new_transaction = Transaction.objects.create(spender = spender, topic = topic, group = group, amount = amount, getter = getter)
        new_transaction.save()
        new_totaltransaction = TotalTransaction.objects.create(spender = spender, getter = getter, amount = amount, group = group)
        new_totaltransaction.save()
        response_data = {
           'message': 'successful',
        }
        
    return JsonResponse(response_data)   

@csrf_exempt
def add_user(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    else:
        user_check = request.POST.get("user_check")
        owner = request.user.username
        if user_check == owner:
            response_data = {
                'message': 'same'
            }
        else:
            if_user_with_same_username_exits = User.objects.filter(username = user_check).count()
            if if_user_with_same_username_exits == 1:
                response_data = {
                    'message': 'created'
                }
            else:
                response_data = {
                    'message': 'not found'
                }
        return JsonResponse(response_data)                   

@csrf_exempt
def add_group(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    else:
        print("Hello")    
        title = request.POST.get("group_name")
        datecreated = date.today()
        owner = request.user
        details = request.POST.get("details")
        username_array = request.POST.getlist("username_array[]")
        new_group = Group.objects.create(title = title, owner = owner, datecreated = datecreated, details = details)
        new_group.save()
        new_group_member = GroupMember.objects.create(user = owner, group = new_group)
        new_group_member.save()

        for username in username_array:
            username_get = User.objects.get(username = username)
            new_group_member_other = GroupMember.objects.create(user = username_get, group = new_group)
            new_group_member_other.save()

        response_data = {
            'message' : 'created'
        }
        return JsonResponse(response_data)

def group_pic(request):
    if not request.user.is_authenticated:
        return render(request, "login.hmtl")
    else:
        group_num = Group.objects.filter(owner = request.user).count()
        group = Group.objects.filter(owner = request.user)[group_num-1]
        group.image = request.FILES.get('image')
        group.save()

        response_data = {
            'message': 'image added',
        }
        return JsonResponse(response_data)            

def prof_pic(request):
    user = request.user
    if ProfilePicture.objects.filter(user = user).count() == 0:
        picture = ProfilePicture.objects.get(user = User.objects.get(username = 'admin'))
    else:
        picture_num = ProfilePicture.objects.filter(user = user).count()    
        picture = ProfilePicture.objects.filter(user = user)[picture_num-1]
    return picture

def profile(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    else:    
        picture = prof_pic(request)
        transactions_spender = Transaction.objects.filter(spender = request.user)
        purchases = Purchase.objects.filter(spender = request.user)
        groups = GroupMember.objects.filter(user = request.user)
        groups_num = GroupMember.objects.filter(user = request.user).count()
        groups_created = Group.objects.filter(owner = request.user)
        groups_created_num = Group.objects.filter(owner = request.user).count()
        total_purchase_amount = 0
        total_transaction_amount = 0
        for transaction in transactions_spender:
            total_transaction_amount += transaction.amount
        for purchase in purchases:
            total_purchase_amount += purchase.amount
        print(groups_created_num)         
        context = {
            'picture': picture,
            'total_transaction_amount': total_transaction_amount,
            'total_purchase_amount': total_purchase_amount,
            'groups': groups,
            'groups_num': groups_num,
            'groups_created': groups_created,
            'groups_created_num': groups_created_num,
        }
        return render(request, "profile.html", context)

def profile_picture_view(request):
    user = request.user
    image = request.FILES.get('image')
    new_image = ProfilePicture.objects.create(picture = image, user = user)
    print("reached this view")
    new_image.save()
    return JsonResponse("done", safe=False)
