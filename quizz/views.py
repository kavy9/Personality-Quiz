from django.shortcuts import render
from django import forms
from django.http import HttpResponse 
#class Loginform():
#    name = forms.CharField(label="name")
#    email = forms.CharField(label="email")
#    result = forms.IntegerField(label="result")

def index(request):
    return render(request,"quiz/index.html")

#    name = request.POST.get('name')
      
def main_page(request):
    global name
    name = request.POST.get('name')
    return render(request,"quiz/quiz.html")

def result(request):
    list_=[0,0,0,0]
    plist=[
        ['e','s','t','j']
        ['i','n','f','p']
    ]
    per=""
    q=[None]*len(matrix)
    for i in range(12):
        que='question-'+str(i+1)
        q=int(request.POST.get(que))
        index_=int((i+1)/3)
        if i in [0,1,2]:
           if q==0:
               list_[index_]=list_[index_] +1
           elif q==1:    
               list_[index_]=list_[index_]-1
        # if i in [3,4,5]:
        #    if q==0:
        #        list_[1]=list_[1] +1
        #    elif q==1:    
        #        list_[1]=list_[1]-1
        # if i in [6,7,8]:
        #    if q==0:
        #        list_[2]=list_[2] +1
        #    elif q==1:    
        #        list_[2]=list_[2]-1
        # if i in [9,10,11]:
        #    if q==0:
        #        list_[3]=list_[3] +1
        #    elif q==1:    
        #        list_[3]=list_[3]-1
    for i in range(4):
        list_[i]          







    for i in range(10):
        lst = matrix[i][ans[i]]
        for j in range(4):
            Result[j] = Result[j]+lst[j]
    max_marks=max(Result)
    index=Result.index(max_marks)
    if index==0:
        return render(request,"quiz/driver.html",{
            "name" : name.capitalize()
        })        
    elif index==1:
        return render(request,"quiz/analytical.html",{
            "name" : name.capitalize()
        }) 
    elif index==2:
        return render(request,"quiz/amiable.html",{
            "name" : name.capitalize()
        }) 
    elif index==3:
        return render(request,"quiz/expressive.html",{
            "name" : name.capitalize()
        })         
    else:
        return HttpResponse("noooooooooooooooo :(")


"""def result(request):
    one=request.POST.get('question-1')
    if int(one)==0:
        return render(request,"quiz/result.html")
    else:
        return HttpResponse("nooooooooooooo")"""
