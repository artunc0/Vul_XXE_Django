from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from lxml import etree
import xml.etree.ElementTree as XET
#from defusedxml import pulldom

def index(request):
    return render(request, 'insecure_website.html')

@csrf_exempt
def search(request):
    #parser = etree.XMLParser(no_network=False, dtd_validation=False, load_dtd=True)  # to enable network entity. see xmlparser-info.txt
    parser = etree.XMLParser(no_network=False, dtd_validation=True, load_dtd=True)  # to enable network entity. see xmlparser-info.txt
    # request.body.encode()
    #payload2 = '''<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///c:/windows/win.ini"> ]><root><search_param>&xxe;</search_param></root>'''
    doc = etree.fromstring(request.body, parser)
    result = XET.tostring(doc)
    print(result)
    # now in the object cd, you have the form as a dictionary.
    return HttpResponse(f"Results:{result}")
