from django.http import HttpResponse

from django.template import RequestContext, loader

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from generation.models import Name
import json
import socket
import redis
import socket
import _thread
port = 8569
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def getRequest(request):
    n = Name(name_text=request.GET['name'],score=request.GET['score'])
    n.save()
    return HttpResponse("<p>Mission Accomplished<p>",n.id)
def show(request):
    Name.objects.order_by('score')
    myList = []
    # dic={}
    i=0
    for name in Name.objects.all():
        if(i==10):
            break
        # dic[name.name_text] = name.score
        dic = {name.name_text:name.score}
        myList.append(dic)
        i+=1
    alireza = json.dumps(myList)
    myDic = json.loads(alireza)
    return HttpResponse(myDic[1]['mohammad'])



def serverTest(request):
    counter=0
    s = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    port = 12345  # Reserve a port for your service.
    s.bind((host, port))  # Bind to the port

    s.listen(5)  # Now wait for client connection.
    while counter!=4:
        c, addr = s.accept()  # Establish connection with client.
        c.send("hello world")
        c.close()
        counter+=1
    return HttpResponse("goodbye")

def clientTest(request):
    s = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    port = 12345  # Reserve a port for your service.

    s.connect((host, port))
    alireza =  s.recv(1024)
    s.close  # Close the socket when done
    return HttpResponse(alireza)

try:
   _thread.start_new_thread( clientTest, ( ) )
   _thread.start_new_thread( clientTest, ( ) )
except:
   print ("Error: unable to start thread")