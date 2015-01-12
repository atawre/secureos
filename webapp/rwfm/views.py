from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rwfm.models import Object
from rwfm.models import Subject
from rwfm.serializers import ObjectSerializer
from rwfm.serializers import SubjectSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def object_list(request, sub_id=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        objects = Object.objects.all()
        serializer = ObjectSerializer(objects, many=True)
        data = [{'title': u'', 'result': True, 'linenos': False, 'language': u'python', 'style': u'friendly'}]
        return JSONResponse(data)
        #return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ObjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def subject_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SubjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def home(request):
    """
    List all code snippets, or create a new snippet.
    """
    data = "Readers Writers Flow Model demo."
    return JSONResponse(data)


