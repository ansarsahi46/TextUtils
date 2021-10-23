from django.http import HttpResponse
from django.shortcuts import render


def index(request):
     return render(request, 'index.html')



def analyze(request):
    #Get the text that entered
     djtext = request.GET.get('text', 'default')
    #Check the Checkbox of punctuation
     punctuationcheckbox = request.GET.get('punctuationcheckbox', 'off')
    # Get the value of uppercase checkbox
     uppercasecheckbox = request.GET.get('uppercasecheckbox', 'off')
    
    #Get the value of ExtraspaceRemover checkbox
     extraspaceremover = request.GET.get('extraspaceremover', 'off')
    #Get the value of newlineremover checkbox
     newlineremover = request.GET.get('newlineremover', 'off')

     analyzed_text= ''
     punctuation = ''';.[]!@#$%^&*()_+~":><|/.,';[\]-='''
     noofwords = ""
     nameword = ""
     namecharacter = ""
   
     if(punctuationcheckbox =="on" or uppercasecheckbox=="on" or extraspaceremover== "on" or newlineremover== "on"):
         # Check if punctuation checkbox is on or not

         if punctuationcheckbox == 'on':
             for char in djtext:
                if char not in punctuation:
                      analyzed_text = analyzed_text + char

             djtext = analyzed_text


         # Check the uppercase checkbox is on or not
         if uppercasecheckbox == "on":
            analyzed_text = ""
            for char in djtext:
                analyzed_text = analyzed_text + char.upper()
            djtext = analyzed_text

        # Check the extra space remover is on or not
         if extraspaceremover == "on":
             analyzed_text = ""
             for index, char in enumerate(djtext):
                 if not (djtext[index] == " " and djtext[index + 1] == " "):
                     analyzed_text = analyzed_text + char

             djtext= analyzed_text


          # Check the value of new line remover checkbox
         if newlineremover == "on":
              analyzed_text = ""
              for char in djtext:
                 if char != "\n" and char!="\r":
                     analyzed_text = analyzed_text + char
              djtext = analyzed_text


     # else statement
     else:
         return HttpResponse("Error")

     texts= "Texts are Analyzed"
     params = {'Purpose' : texts, 'analyzed' : djtext, 'word': nameword, 'words': noofwords,  'character': namecharacter}
     return render(request, 'analyze.html', params)
