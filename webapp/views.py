#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from models import Mobile
import jieba
import re

# Create your views here.
def index(request):
    #cnt是一个保存各个价格区间手机数量的列表
    cnt = [0,0,0,0,0,0,0]
    cnt[0] = len(Mobile.objects.filter(price__range=(0,1000)))
    cnt[1] = len(Mobile.objects.filter(price__range=(1000,2000)))
    cnt[2] = len(Mobile.objects.filter(price__range=(2000,3000)))
    cnt[3] = len(Mobile.objects.filter(price__range=(3000,4000)))
    cnt[4] = len(Mobile.objects.filter(price__range=(4000,5000)))
    cnt[5] = len(Mobile.objects.filter(price__range=(5000,6000)))
    cnt[6] = len(Mobile.objects.filter(price__gte=6000))

    #cntListDate是一个保存各个上市年份区间手机数量的列表
    cntListDate = [0,0,0,0,0,0,0]
    cntListDate[0] = Mobile.objects.filter(listDate__contains='2016').count()
    cntListDate[1] = Mobile.objects.filter(listDate__contains='2015').count()
    cntListDate[2] = Mobile.objects.filter(listDate__contains='2014').count()
    cntListDate[3] = Mobile.objects.filter(listDate__contains='2013').count()
    cntListDate[4] = Mobile.objects.filter(listDate__contains='2012').count()
    cntListDate[5] = Mobile.objects.filter(listDate__contains='2011').count()
    cntListDate[6] = Mobile.objects.all().count() - (cntListDate[0]+cntListDate[1]+cntListDate[2]+cntListDate[3]+cntListDate[4]+cntListDate[5])

    smart = []
    nsmart = []
    for mobile in Mobile.objects.all():
        try:
            year = re.findall("\d+", mobile.listDate)[0]
        except:
            continue
        if mobile.isSmart==u'是':
            smart.append([mobile.price, int(year)])
        elif mobile.isSmart==u'否':
            nsmart.append([mobile.price,int(year)])
    print smart
    return render(request,'index.html',{'cnt': cnt, 'cntListDate': cntListDate, 'smart': smart, 'nsmart': nsmart})

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def search(request):
    sea = request.GET['search']
    s = jieba.lcut(sea,cut_all=False)    #s为输入的关键字经过jiebe分词后产生的列表
    while ' ' in s:
        s.remove(' ')
    results = []
    for ss in s:
        keywords = Mobile.objects.filter(keywords__icontains=ss)    #对每个分词逐一查找
        results.append(keywords)
    res = list(set(results[0]).union(*results[1:]))    #res为所有查找结果的并集
    products = {}    #products为匹配度字典
    for pro in res:
        products[pro] = pipeidu(pro.keywords,s)    #计算所有结果的匹配度
    pros = sorted(products.iteritems(),key=lambda products:products[1],reverse=True)    #按照匹配度排序
    len_list = len(pros)
    return render(request,'results.html',{'pros':pros,'len_list':len_list})

#计算匹配度，str_strkeywords为商品关键字，list_fenci为输入的关键字分词列表
def pipeidu(str_keywords,list_fenci):
    cnt = 0
    for fenci in list_fenci:
        if fenci in str_keywords:
            cnt += 1
    return cnt

def addCompare(request):
    id_list = request.GET.getlist('mobile')
    detail_list = []
    data_list = []
    for id in id_list:
        details = Mobile.objects.get(skuid=id)
        detail_list.append(details)
        data = open('F:\Projects\PCAS2\webapp\static\datas\\'+id+'.txt','r').read().split(',')
        data_num = map(float,data)
        data_num.append(details.keywords)
        data_list.append(data_num)
    return render(request,'cmps.html',{'detail_list':detail_list, 'data_list': data_list})
