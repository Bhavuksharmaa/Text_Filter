#This view is created by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index2.html')
    # return HttpResponse("this is home <a href='/about'>about</a>")

def analyze(request):
    djstring = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    print(removepunc)
    capitalization =request.POST.get('captilize','off')
    extraspace=request.POST.get('removeextspace','off')
    countchar = request.POST.get('countchar', 'off')
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    string=""

    if removepunc=="on":
        for char in djstring:
            if char not in punctuations:
                string = string + char
        djstring=string

    if capitalization=='on':
        djstring = djstring.upper()

    if extraspace=='on':
        string=""
        for index,char in enumerate(djstring):
            if not (djstring[index] == ' ' and djstring[index+1] == ' '):
                if (djstring[index] != "\r" and djstring[index] != "\n"):
                    string = string + char
        djstring=string

    if countchar=='on':
        i=0
        for index,char in enumerate(djstring):
            i = i + 1

    if removepunc=='off'and capitalization=='off'and extraspace=='off'and countchar=='off' :
        param = {'purpose': 'None', 'removedpunc': djstring}
        return render(request,'analyze2.html',param)
    else:
        if countchar=='on':
            param = {'purpose': 'Analyze', 'removedpunc':f"{djstring}({i})"}
            return render(request, 'analyze2.html', param)
        else:
            param = {'purpose': 'Analyze', 'removedpunc': djstring}
            return render(request, 'analyze2.html', param)

def about(request):
    return render(request,'about.html')
