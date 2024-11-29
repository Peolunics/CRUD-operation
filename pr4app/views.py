from django.shortcuts import render
from .models import *
import re

# Create your views here.

def home(request):
    return render(request,'phonebook.html')

def add(request):
    responseDict={}

    try :
        viewName=request.POST['inputName']
        viewNumber=request.POST['inputNumber']

        if phonebook.objects.filter(name=viewName).exists():
            responseDict['key_Add']="Name Already Exists"

        else:
            inputList=phonebook(name=viewName,number=viewNumber)
            inputList.save()
            responseDict['key_Add']="Sucessfully Added"

        return render(request,'phonebook.html',responseDict)

    except Exception as exceptionObject:
        print(exceptionObject)
        responseDict['key_Add']="Add Failed"
        return render(request,'phonebook.html',responseDict)

def display(request):
    phnDisplay=phonebook.objects.all()
    return render(request,'phonebook.html',{'phn':phnDisplay})

def delete(request):
    try :
        viewName=request.POST['deleteName']

        temp1 = re.search(r'\d+', viewName)
        if temp1:
            viewId=temp1.group()
            viewDelete = phonebook.objects.filter(id=viewId)

        else:
            viewDelete = phonebook.objects.filter(name=viewName)
        

        if viewDelete.exists():  # Check if any records exist
            viewDelete.delete()
            return render(request, 'phonebook.html', {'key_Delete': 'Deleted Successfully'})
        
        else:
            return render(request, 'phonebook.html', {'key_Delete': 'No Record Found with the Given Name or ID'})   
             
    except Exception as exceptionObject:
        print(exceptionObject)
        return render(request,'phonebook.html',{'key_Delete':'Deletion Failed'})
  

def update(request):
    try :
        viewOldName=request.POST['inputOldName']
        viewNewName=request.POST['inputNewName']

        phonebook.objects.filter(name=viewOldName).update(name=viewNewName)
        return render(request,'phonebook.html',{'key_Update':'Updated'})
        
    except Exception as exceptionObject:
        print(exceptionObject)
        return render(request,'phonebook.html',{'key_Update':'Not Updated'})

