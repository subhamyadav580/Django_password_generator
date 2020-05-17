from django.shortcuts import render
from django.http import HttpResponse
import string
import random
# Create your views here.


def generate(request):
    if request.method == 'POST':
        gridCheck1 = request.POST.get('gridCheck1', 'off')
        gridCheck2 = request.POST.get('gridCheck2', 'off')
        gridCheck3 = request.POST.get('gridCheck3', 'off')
        gridCheck4 = request.POST.get('gridCheck4', 'off')
        size = request.POST['size']
        val = string.ascii_lowercase
        val1 = string.ascii_uppercase
        val2 = string.digits
        val3 = string.punctuation
        if gridCheck1 == 'on':
            if gridCheck2 == 'off':
                if gridCheck3 == 'off':
                    if gridCheck4 == 'off':
                        psw = lowercase(val,size)
                        return render(request, 'gen.html',{'Password':psw})
                    elif gridCheck4 == 'on':
                        psw = lower_pun(val,val3,size)
                        return render(request, 'gen.html',{'Password':psw})
                elif gridCheck3 == 'on':
                    if gridCheck4 == 'on':
                        psw = lower_dig_pun(val,val2,val3,size)
                        return render(request, 'gen.html',{'Password':psw})
                    elif gridCheck4 == 'off':
                        psw = lower_dig(val,val2,size)
                        return render(request, 'gen.html',{'Password':psw})
            elif gridCheck2 == 'on':
                if gridCheck3 == 'on':
                    if gridCheck4 == 'on':
                        psw = all(val,val1,val2,val3,size)
                        return render(request, 'gen.html',{'Password':psw})
                    elif gridCheck4 == 'off':
                        psw = lower_upper_dig(val,val1,val2,size)
                        return render(request, 'gen.html',{'Password':psw})
                elif gridCheck3 == 'off':
                    if gridCheck4 == 'on':
                        psw = lower_upper_pun(val,val1,val3,size)
                        return render(request, 'gen.html',{'Password':psw})
                    elif gridCheck4 == 'off':
                        psw = lower_upper(val,val1,size)
                        return render(request, 'gen.html',{'Password':psw})
        elif gridCheck1 == 'off':
                if gridCheck2 == 'on':
                    if gridCheck3 == 'off':
                        if gridCheck4 == 'off':
                            psw = uppercase(val1,size)
                            return render(request, 'gen.html',{'Password':psw})
                        elif gridCheck4 == 'on':
                            psw = upper_pun(val1,val3,size)
                    elif gridCheck3 == 'on':
                        if gridCheck4 == 'on':
                            psw = upper_dig_pun(val1,val2,val3,size)
                            return render(request, 'gen.html',{'Password':psw})
                        elif gridCheck4 == 'off':
                            psw = upper_dig(val1,val2,size)
                            return render(request, 'gen.html',{'Password':psw})
                elif gridCheck2 == 'off':
                    if gridCheck3 == 'on':
                        if gridCheck4 == 'off':
                            psw = digits(val2,size)
                            return render(request, 'gen.html',{'Password':psw})
                        elif gridCheck4 == 'on':
                            psw = dig_pun(val2,val3,size)
                            return render(request, 'gen.html',{'Password':psw})
                    elif gridCheck3 == 'off':
                        if gridCheck4 == 'on':
                            psw = punctuation(val3,size)
                            return render(request, 'gen.html',{'Password':psw})
                        elif gridCheck4 == 'off':
                            psw = all(val,val1,val2,val3,size)
                            return render(request, 'gen.html',{'Password':psw})

    return render(request, 'gen.html')


def history(request):
    return HttpResponse('hello')


def lowercase(val,size):
    val = list(val)
    return ("".join(random.sample(val,int(size))))


def uppercase(val1,size):
    val1 = list(val1)
    return ("".join(random.sample(val1,int(size))))

def digits(val2,size):
    val2 = list(val2)
    return ("".join(random.sample(val2,int(size))))

def punctuation(val3,size):
    val3 = list(val3)
    return ("".join(random.sample(val3,int(size))))

def all(val,val1,val2,val3,size):
    psw = []
    psw.extend(val)
    psw.extend(val1)
    psw.extend(val2)
    psw.extend(val3)
    return ("".join(random.sample(psw,int(size))))


def lower_upper_pun(val,val1,val3,size):
    psw = []
    psw.extend(val)
    psw.extend(val1)
    psw.extend(val3)
    return ("".join(random.sample(psw,int(size))))


def lower_upper_dig(val,val1,val2,size):
    psw = []
    psw.extend(val)
    psw.extend(val1)
    psw.extend(val2)
    return ("".join(random.sample(psw,int(size))))

def lower_upper(val,val1,size):
    psw = []
    psw.extend(val)
    psw.extend(val1)
    return ("".join(random.sample(psw,int(size))))

def lower_dig_pun(val,val2,val3,size):
    psw = []
    psw.extend(val)
    psw.extend(val2)
    psw.extend(val3)
    return ("".join(random.sample(psw,int(size))))

def upper_dig_pun(val1,val2,val3,size):
    psw = []
    psw.extend(val1)
    psw.extend(val2)
    psw.extend(val3)
    return ("".join(random.sample(psw,int(size))))

def upper_dig(val1,val2,size):
    psw = []
    psw.extend(val1)
    psw.extend(val2)
    random.shuffle(psw)
    return ("".join(random.sample(psw,int(size))))

def upper_pun(val1,val3,size):
    psw = []
    psw.extend(val1)
    psw.extend(val3)
    return ("".join(random.sample(psw,int(size))))

def lower_pun(val,val3,size):
    psw = []
    psw.extend(val)
    psw.extend(val3)
    return ("".join(random.sample(psw,int(size))))

def lower_dig(val,val2,size):
    psw = []
    psw.extend(val)
    psw.extend(val2)
    return ("".join(random.sample(psw,int(size))))

def dig_pun(val2,val3,size):
    psw = []
    psw.extend(val2)
    psw.extend(val3)
    return ("".join(random.sample(psw,int(size))))
