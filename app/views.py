from django.shortcuts import render

# Create your views here.
from app.models import LoginAdminModel, CreatePlotModel, CreateFlattModel, CreateEmployeeModel


def showIndex(request):
    return render(request,"index.html")


def login(request):
    u = request.POST.get("uname")
    p = request.POST.get("pwd")
    l=LoginAdminModel.objects.filter(uname=u,pwd=p)
    if l:
        return render(request, 'nextpage.html',{"msg":"WELCOME ADMIN"})
    else:
        return render(request,'index.html',{"message":"Invalid"})



def viewplot(request):
    return render(request,"viewplot.html")



def viewapart(request):
    return render(request,"viewapart.html")


def viewemp(request):
    return render(request,"viewemp.html")


def viewp(request):
    pno = request.POST.get("pno")
    try:
        p = CreatePlotModel.objects.filter(plotno=pno)
        return render(request, "viewp1.html", {"data": p})
    except:
        return render(request, "nextpage.html", {"data1": "plot doesn't exists"})


def viewa(request):
    ano = request.POST.get("ano")
    try:
        p = CreateFlattModel.objects.filter(flatno=ano)
        return render(request, "viewa1.html", {"data": p})
    except:
        return render(request, "nextpage.html", {"data1": "Apartment doesn't exists"})


def viewemp1(request):
    eno = request.POST.get("eno")
    try:
        p = CreateEmployeeModel.objects.filter(id=eno)
        return render(request, "viewe1.html", {"data": p})
    except:
        return render(request, "nextpage.html", {"data1": "plot doesn't exists"})


def newplot(request):
    return render(request,"newplot.html")


def newapart(request):
    return render(request,"newapart.html")


def createemp1(request):
    return render(request,"createemp.html")


def addplot(request):
    pno=request.POST.get("pno")
    rno=request.POST.get("rno")
    sno=request.POST.get("sno")
    csy=request.POST.get("csy")
    tsy=request.POST.get("tsy")
    exp=request.POST.get("expenses")
    b=request.POST.get("boundaries")
    f=request.POST.get("facing")
    s=request.POST.get("status")
    tc=request.POST.get("tcost")
    CreatePlotModel(plotno=pno,roadno=rno,surveyno=sno,cstpersqyd=csy,totalsqyd=tsy,expenses=exp,boundaries=b,facing=f,
                    status=s,totalcost=tc).save()
    return render(request,"nextpage.html",{"createplot":"Plot Added Successfully"})

def createemp(request):
    eno = request.POST.get("eid")
    n = request.POST.get("name")
    m = request.POST.get("mail")
    l = request.POST.get("loc")
    dj = request.POST.get("doj")
    r = request.POST.get("role")
    q = request.POST.get("qual")
    rm = request.POST.get("remarks")

    CreateEmployeeModel(id=eno,name=n,maillocation=m,locatio=l,doj=dj,role=r,qualification=q,remarks=rm).save()
    return render(request, "nextpage.html", {"createmp": "Employee Added Successfully"})

def addapart(request):
    ano = request.POST.get("ano")
    rno = request.POST.get("rno")
    sno = request.POST.get("sno")
    csy = request.POST.get("csy")
    tsy = request.POST.get("tsy")
    exp = request.POST.get("expenses")
    b = request.POST.get("boundaries")
    f = request.POST.get("facing")
    s = request.POST.get("status")
    tc = request.POST.get("tcost")
    CreateFlattModel(apartno=ano, roadno=rno, surveyno=sno, cstpersqyd=csy, totalsqyd=tsy, expenses=exp, boundaries=b,
                    facing=f,
                    status=s, totalcost=tc).save()
    return render(request, "nextpage.html", {"addapart": "Apartment Added Successfully"})


def changepwd(request):
    return render(request,"changepwd.html")


def cpwd(request):
    old=request.POST.get("opwd")
    new= request.POST.get("npwd")
    p=LoginAdminModel.objects.get(pwd=old)
    if p:
        LoginAdminModel(pwd=new).save()
        return render(request,"nextpage.html",{"cpwd":"Password Changed"})
    else:
        return render(request,"changepwd.html",{"msg":"Password Doesn't Match"})


def deluser(request):
    return render(request,"deleteuser.html")


def duser(request):
    uname=request.POST.get("uname")
    pwd=request.POST.get("pwd")
    l=LoginAdminModel.objects.filter(uname=uname,pwd=pwd)
    if l:
        LoginAdminModel.objects.filter(uname=uname,pwd=pwd).delete()
        return render(request,"nextpage.html",{"msg":"User is Deleted"})
    else:
        return render(request,"deleteuser.html",{"msg":"USER & Password Doesn't Exists"})


def adduser(request):
    return render(request,"adduser.html")


def adduser1(request):
    uname=request.POST.get("uname")
    pwd=request.POST.get("pwd")
    LoginAdminModel(uname=uname,pwd=pwd).save()
    return render(request,"nextpage.html",{"msg":"User is created"})


def viewuser(request):
    l=LoginAdminModel.objects.all()
    return render(request,"viewuser.html",{"data":l})


def editplot(request):
    pno=request.POST.get("pno")
    p=CreateFlattModel.objects.filter(plotno=pno)
    if p:
        return render(request,"editplot.html",{"data":p})
def edits(request):
    pno = request.POST.get("pno")
    rno = request.POST.get("rno")
    sno = request.POST.get("sno")
    csy = request.POST.get("csy")
    tsy = request.POST.get("tsy")
    exp = request.POST.get("expenses")
    b = request.POST.get("boundaries")
    f = request.POST.get("facing")
    s = request.POST.get("status")
    tc = request.POST.get("tcost")
    CreatePlotModel(roadno=rno, surveyno=sno, cstpersqyd=csy, totalsqyd=tsy, expenses=exp, boundaries=b,
                    facing=f,
                    status=s, totalcost=tc).save()

    return render(request,"nextpage.html",{"edits":"Plot is Updated successfully"})





def editapt1(request):
    x=CreateFlattModel.objects.all()
    return render(request,"editapt1.html",{"data":x})


def editaparts(request):
    ano = request.POST.get("ano")
    rno = request.POST.get("rno")
    sno = request.POST.get("sno")
    csy = request.POST.get("csy")
    tsy = request.POST.get("tsy")
    exp = request.POST.get("expenses")
    b = request.POST.get("boundaries")
    f = request.POST.get("facing")
    s = request.POST.get("status")
    tc = request.POST.get("tcost")
    CreateFlattModel(roadno=rno, surveyno=sno, cstpersqyd=csy, totalsqyd=tsy, expenses=exp, boundaries=b,
                    facing=f,
                    status=s, totalcost=tc).save()

    return render(request, "nextpage.html", {"aparts": "Apartment is Updated successfully"})


def editemp(request):
    return render(request,"editemp.html")


def editemp1(request):
    x=CreateEmployeeModel.objects.all()
    return render(request,"editemp1.html",{"data":x})


def editep(request):
    createemp(request)


def editpt(request):
    a=CreatePlotModel.objects.all()
    return render(request,"editpt.html",{"data":a})


def editaparts2(request):
    a=CreateFlattModel.objects.all()
    return render(request,"editaparts2.html",{"data":a})


def deleteplot(request):
    return render(request,"deleteplot.html")


def delpt(request):
    pno = request.POST.get("pno")
    k=CreatePlotModel.objects.get(plotno=pno).delete()
    if k:
            return render(request,"nextpage.html",{"message":"Plot id Deleted"})
    else:
            return render(request, "deleteplot.html", {"message1": "Plot Doesn't Exists"})
def deleteapart(request):
    return render(request,"deleteapart.html")


def delat(request):
    ano = request.POST.get("ano")
    k=CreateFlattModel.objects.get(flattno=ano).delete()
    if k:
            return render(request,"nextpage.html",{"message":"Apartment is Deleted"})
    else:
            return render(request, "deleteapart.html", {"message1": "Plot Doesn't Exists"})
def deleteemp(request):
    return render(request,"deleteplot.html")


def delep(request):
    pno = request.POST.get("eno")
    k=CreateEmployeeModel.objects.get(id=pno).delete()
    if k:
            return render(request,"nextpage.html",{"message":"Employee id Deleted"})
    else:
            return render(request, "deleteemp.html", {"message1": "Plot Doesn't Exists"})


def about(request):
    return render(request,"about.html")