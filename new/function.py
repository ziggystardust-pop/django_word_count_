


from django.http import HttpResponse
from django.shortcuts import render

def home(request):#request是用户发出的请求,点击网页上某个按钮，向web服务器发出一个请求
    # return HttpResponse('hello')
    return render(request,"home.html")#获得一个请求，返回一个网页


def count(request):#request是用户发出的请求,点击网页上某个按钮，向web服务器发出一个请求
    # return HttpResponse('hello')
    # home.html中submit按钮将text文本框中的文本提交给count网页
    # 怎么获得它：
    # print(request.GET['text'])#字典形式{'text':xxxx}
    user_text = request.GET['text']
    total_count = len(request.GET['text'])
    word_dict = {}#找出每个字出现的次数
    for word in user_text:
        word_dict[word] = word_dict.get(word, 0) + 1
    sorted_dict = sorted(word_dict.items(),key = lambda w:w[1],reverse=True)
    return render(request,"count.html",{'total':total_count,
                                        'user_text':user_text
                                        ,'word_dic':word_dict,'sorted':sorted_dict})#获得一个请求，返回一个网页

def third(request):#request是用户发出的请求,点击网页上某个按钮，向web服务器发出一个请求
    # return HttpResponse('hello')
    return render(request,"third.html")#获得一个请求，返回一个网页

def about(request):
    return render(request,'about.html')
