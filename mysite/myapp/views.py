from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt




def loginPage(request):
    return render(request, 'login.html')


@csrf_exempt
def search(request):
    

    
    #from defusedxml.ElementTree import fromstring, tostring
    #doc = fromstring(request.body)
    #result = tostring(doc)

    from lxml import etree
    import xml.etree.ElementTree as XET
    parser = etree.XMLParser(no_network=False, dtd_validation=False, load_dtd=True)
    doc = etree.fromstring(request.body, parser)
    result = XET.tostring(doc)

    # payload2 = '''<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///c:/windows/win.ini"> ]><root><search_param>&xxe;</search_param></root>'''

    print(result)
    return HttpResponse(result)
