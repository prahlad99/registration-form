# i have created this file -prahlad
# from django.http import HttpResponse
#
# def index(request):
#     sum = 0
#     for i in range(8):
#         sum = sum + i
#     return HttpResponse(
#         ''' <h1>hii</h1> <a href=https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7>django plylist</a>''')
#
#
# def about(request):
#     return HttpResponse("about bahi prahlad")
#
#
# def navigation(request):
#     u = '''<h2>my all miscllenious exercise</h2><br>
#        <a href=https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7> django playlist</a><br>
#
#        <a href =https://www.hackerrank.com/domains/algorithms?filters%5Bstatus%5D%5B%5D=unsolved&badge_type=problem-solving>hackerrank </a><br>
#        <a href =https://www.google.com/search?client=ubuntu&channel=fs&q=english+to+hindi&ie=utf-8&oe=utf-8>english to hindi </a><br>
#        <button onclick="goBack()">Go Back</button>
#        <script>
#        function goBack(){
#        window.history.back();
#        }
#       </script>
#        '''
#   return HttpResponse(u)
from django.http import HttpResponse
from django.shortcuts import render
def index(request):

    return render(request,'registration.html')# render have three argument one is necessary request and you put one for run server some any html file and third is filez
# def capital(request):
#     return HttpResponse("<h2>capital</h2> <a href='/'>back</a>")
def login(request):
    return render(request,'login.html')
def analyze(request):
    djtext=request.POST.get('text', 'default')
   # print(djtext)
  #  print(request.GET.get('removepunc','off'))
    removepunc=request.POST.get('removepunc','off')
    spaceremover=request.POST.get('extraspaceremover','off')

    fullcaps=request.POST.get('fullcaps','off')
    charto=request.POST.get('charcount','off')

    if removepunc=="on":
          removepun= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

          analyzetext=""
          for char in djtext:
               if char not in removepun:
                     analyzetext=analyzetext+char
          print(djtext)
          params={'progress':'progress','analyzed':analyzetext}

          djtext=analyzetext
         # return render(request,'analyze.html',params)
    if(fullcaps=="on"):
        analyzetext=""
        for i in djtext:
            analyzetext=analyzetext+i.upper()
        params = {'purpose':" on uppercase capitalize", 'analyzed': analyzetext}
        #return render(request, 'analyze.html', params)
        djtext=analyzetext
    if (spaceremover == "on"):
        analyzetext = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzetext = analyzetext +char
        params = {'purpose': " extraspace remover", 'analyzed': analyzetext}
        djtext=analyzetext
       # return render(request, 'analyze.html', params)
    if (charto == "on"):
        cout=0
        for i in djtext:
            if i!=' ':
                cout=cout+1
        params = {'purpose': " charcounter", 'analyzed': cout}

       # return render(request, 'analyze.html', params)

    return render(request, 'analyze.html', params)





# def backbutton(request):
#     return HttpResponse("hii prahlad <a href ='/'>back</a>")
def navigation(request):
    return render(request,'navigate.html')
def prac(request):
    return render(request,'practice.html')
def contactus(request):
    return render(request,'contact.html')