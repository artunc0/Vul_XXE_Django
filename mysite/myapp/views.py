from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from lxml import etree
# import xml.etree.ElementTree as XET
from defusedxml.ElementTree import fromstring, tostring
def loginPage(request):
    return render(request, 'index.html')


@csrf_exempt
def search(request):
    # parser = etree.XMLParser(no_network=False, dtd_validation=False, load_dtd=True)
    # doc = etree.fromstring(request.body, parser)

    doc = fromstring(request.body)
    result = tostring(doc)

    # request.body.encode()
    # payload2 = '''<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///c:/windows/win.ini"> ]><root><search_param>&xxe;</search_param></root>'''
    #result = XET.tostring(doc)
    print(result)
    # now in the object cd, you have the form as a dictionary.
    return HttpResponse(result)
