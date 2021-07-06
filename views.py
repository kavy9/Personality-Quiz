from django.shortcuts import render
from django import forms
from django.http import HttpResponse 
#class Loginform():
#    name = forms.CharField(label="name")
#    email = forms.CharField(label="email")
#    result = forms.IntegerField(label="result")

mtrx=[]
name=""
q1=[
    [31,12,9,96],
    [93,10,7,33],
    [20,90,14,11],
    [13,25,97,12]
]
q2=[
    [90,15,10,33],
    [10,80,40,20],
    [15,40,85,16],
    [30,16,20,91]
]
q3=[
    [80,13,25,30],
    [30,12,15,90],
    [20,95,11,10],
    [13,20,99,9]
]
q4=[
    [30,95,15,13],
    [93,30,21,15],
    [25,14,19,96],
    [15,13,93,30]
]
q5=[
    [10,20,15,90],
    [11,40,80,20],
    [95,40,19,17],
    [40,90,15,19]
]
q6=[
    [20,13,12,93],
    [12,95,19,30],
    [30,10,95,20],
    [95,35,13,19]
]
q7=[
    [50,81,30,20],
    [30,20,85,41],
    [45,14,16,83],
    [87,43,25,30]
]
q8=[
    [27,95,17,35],
    [19,13,25,96],
    [15,35,91,23],
    [95,29,17,19]
]
q9=[
    [0,50,50,0],
    [50,0,0,50]
]
q10=[
    [0,0,50,50],
    [50,50,0,0]
]
Result=[0,0,0,0]     #this a the list in which the marks will be added in order Driver,Analytical,Amiable and Expressive 
matrix=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
def index(request):
    return render(request,"quiz/index.html")

#    name = request.POST.get('name')
      
def main_page(request):
    global name
    name = request.POST.get('name')
    return render(request,"quiz/quiz.html")

def result(request):
    ans=[None]*len(matrix)
    ans[0]=int(request.POST.get('question-1'))
    ans[1]=int(request.POST.get('question-2'))
    ans[2]=int(request.POST.get('question-3'))
    ans[3]=int(request.POST.get('question-4'))
    ans[4]=int(request.POST.get('question-5'))
    ans[5]=int(request.POST.get('question-6'))
    ans[6]=int(request.POST.get('question-7'))
    ans[7]=int(request.POST.get('question-8'))
    ans[8]=int(request.POST.get('question-9'))
    ans[9]=int(request.POST.get('question-10'))
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
