from django.shortcuts import render,HttpResponseRedirect
from django.utils.html import escape
from .models import Information
from django.contrib import messages
from django.db.models import Q
import requests,json
from datetime import datetime
from django.http import JsonResponse
# Create your views here.
def Home(request):
    data=Information.objects.all()
    headers={
      'x-access-token': 'coinrankingb9e594ff76bd0a26c8b806102f94478f2ca9c8cc13162d63'
         }
    url='https://api.coinranking.com/v2/coin/Qwsogvtv82FCd/history?timePeriod=7d'
    jsons=requests.get(url ,headers=headers).json()
    history=jsons['data']['history']
    price=[]
    time=[]
    for values in history:
        price.append(values['price'])
        timestamp=int(values['timestamp'])
        times=datetime.utcfromtimestamp(timestamp).strftime('%A %H:%M')
        time.append(str(times))
    price=price[::-1]
    time=time[::-1]    
    context={
        'data':data,
        'price':price,
        'time':time
    }
    return render(request, 'index.html',context)

def Insert(request):
    #Protacting data from XSS inection
    #Using form Api was easy but fixing bugs more comfortable for me.
    name=escape(request.POST.get('name'))
    amount=escape(request.POST.get('amount'))
    location=escape(request.POST.get('location'))
    data=Information(name=name,amount=amount,location=location)
    data.save()
    messages.success(request, 'Data inserted...')
    return HttpResponseRedirect('/')

def Edit(request,id):
    info=Information.objects.get(id=id)
    data=Information.objects.all()
    context={
        'data':data,
        'info':info,
    }
    return render(request, 'edit.html',context)

def Update(request,id):
    name=escape(request.POST.get('name'))
    amount=escape(request.POST.get('amount'))
    location=escape(request.POST.get('location'))
    data=Information(id=id,name=name,amount=amount,location=location)
    data.save()
    messages.success(request, 'Data Updated...')
    return HttpResponseRedirect('/')

def Delete(request,id):
    try:
        Information.objects.get(id=id).delete()
        messages.success(request, 'Data deleted...')
        return JsonResponse({"status":"success"}) 
    except:
        messages.success(request, 'Something went wrong')
        return JsonResponse({"status":"failed"})   

def Search(request):
    #data=escape(request.GET.get('search'))
    data=request.GET.get('search')
    context=None
    if not data:
        return HttpResponseRedirect('/')
    else:    
        results=Information.objects.filter(Q(name__icontains=data) | Q(amount__icontains=data) |Q(location__icontains=data))
        context={
            'data':data,
            'results':results,
        }
    return render(request,'search.html',context)
