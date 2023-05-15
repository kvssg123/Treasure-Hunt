from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Player

# Create your views here.
def index(request):
    return render(request,"login.html")

def logincheck(request):
    if request.method == 'POST':
        button = request.POST.get('button')
        if button == 'login':
            email=request.POST.get('email')
            password=request.POST.get('password')
            context={}
            try:
                player=Player.objects.get(email=email,password=password)
                id=player.id
                if(player.curr_level==1):
                    player.start_time=timezone.now()   
                    player.save()
                    return render(request,"emoji.html",{'id':id})
                else:
                    curr=player.curr_level-1
                    print(curr)
                    s='level'+str(curr)+'gift'
                    print(s)
                    return redirect('/%s/%s' %(str(id),s))
                    
            except Player.DoesNotExist: return render(request,'accessdenied.html')
            
        elif button=="register":
            return render(request,'register.html')
    else: return render(request,"emoji.html")


def register(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            Player.objects.get(email=email)
            return render(request,'register.html')
        except Player.DoesNotExist:
            username=request.POST.get('username')
            Player.objects.create(email=email,username=username,password=password)
            return redirect("index")
    return render(request,'register.html')
    
def level1(request,id):
    player= Player.objects.get(id=id)
    if request.method=='POST':
        corrow=request.POST.get('rownum')
        corcol=request.POST.get('colnum')
        row=request.POST.get('row')
        col=request.POST.get('col')
        if(str(row)==str(corrow) and str(corcol)==str(col)): 
            player.curr_level=2
            player.save()
            return render(request,"gift1.html",{'id':id})
    return render(request,"emoji.html",{'id':id})


def level1gift(request,id):
    player= Player.objects.get(id=id)
    if player.curr_level!=2:
        return render(request,'accessdenied.html')
    if request.method=='POST':
        return render(request,'level2.html',{'id':id})
    return render(request,"gift1.html",{'id':id})


def level2(request,id):
    player= Player.objects.get(id=id)
    if player.curr_level!=2:
        return render(request,'accessdenied.html')
    if request.method=="POST":
        sport=request.POST.get('sport')
        if sport.lower()=='oinawas' or sport.lower()=='oina':
            player.curr_level=3
            player.save()
            return render(request,"gift2.html",{'id':id})
    return render(request,"level2.html",{'id':id})


def level2gift(request,id):
    player= Player.objects.get(id=id)
    if player.curr_level!=3:
       return render(request,'accessdenied.html')
    if request.method=='POST':
        return render(request,'level3.html',{'id':id})
    # return redirect('/%s/level2/'%str(id))
    return render(request,'gift2.html',{'id':id})


def level3(request,id):
    player= Player.objects.get(id=id)
    if player.curr_level!=3:
        return render(request,'accessdenied.html')
    if request.method=="POST":
        q1=request.POST.get('q1')
        q2=request.POST.get('q2')
        q3=request.POST.get('q3')
        ans1='dictionary'
        ans2='cryptosystem'
        ans3='indigo'
        if(q1.lower()==ans1 and q2.lower()==ans2 and q3.lower()==ans3):
            player.curr_level=4
            player.save()
            return render(request,'gift3.html',{'id':id})
    return render(request,"level3.html",{'id':id})


def level3gift(request,id):
    player= Player.objects.get(id=id)
    if player.curr_level!=4:
        return render(request,'accessdenied.html')
    if request.method=='POST':
        return render(request,'level4.html',{'id':id})
    # return redirect('/%s/level3/'%str(id))
    return render(request,'gift3.html',{'id':id})



def level4(request,id):
    player= Player.objects.get(id=id)
    if player.curr_level!=4:
        return render(request,'accessdenied.html')
    if request.method=='POST':
        answer=request.POST.get('sequence')
        if answer.lower()=='gfbed':
            player.curr_level=5
            player.save()
            return render(request,'gift4.html',{'id':id})
    return render(request,"level4.html",{'id':id})



def level4gift(request,id):
    player= Player.objects.get(id=id)
    if player.curr_level!=5:
        return render(request,'accessdenied.html')
    if request.method=='POST':
        return render(request,'level5.html',{'id':id})
    return render(request,'gift4.html',{'id':id})

def level5(request,id):
    player= Player.objects.get(id=id)
    if player.curr_level!=5:
        return render(request,'accessdenied.html')
    if request.method=='POST':
        cipher=request.POST.get('cipher')
        s='congratualtionsonclearingthelastroundyoucanseetheresultsinnextpage'
        if cipher.lower()==s:
            player.curr_level=1
            player.save()
            player= Player.objects.get(id=id)
            start_datetime =  player.start_time
            end_datetime =timezone.now()
            player.end_time=end_datetime
            time_diff = end_datetime - start_datetime
            total_seconds=time_diff.total_seconds()
            player.best_time=min(player.best_time,total_seconds)
            player.save()
            username=player.username
            best_time=player.best_time
            email=player.email
            qs=Player.objects.filter(best_time__lt=player.best_time)
            if qs.filter(id=player.id).exists(): position  = qs.count() 
            else : position=qs.count()+1
            
            return render(request,'congrats.html',{'id':id,'best_time':best_time,'username':username,'position':position,'email':email,'totalseconds':total_seconds})
    return render(request,'level5.html',{'id':id})










            
    