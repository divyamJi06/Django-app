from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from stories.models import WebStory
from rest_framework.decorators import api_view
from .serializers import WebStorySerializer


def index(req):
    return render(req, 'index.html')
    return HttpResponse("HELLO TO INSED PAGE")
def about(req):
    return render(req, 'about.html')

    # return HttpResponse("HELLO TO ABOUT PAGE")
def contact(req):
    return render(req, 'contact.html')
    return HttpResponse("HELLO TO CONTACT PAGE")


def contact_submit(req):
    if(req.method=="POST"):
        name  = req.POST.get("name")
        print(name)
    return HttpResponse("Response Recorded.<br><br><a href='/'>Go to Home Page</a>")

def story(req, link):
    web_story = WebStory.objects.get(permalink=link)
    images = web_story.images.all()
    imagesData = []
    for image in images:
        newText = image.text
        if image.text=="some-text":
            newText = " "
        imagesData.append(
            {
                'image': image.image_url,
                'text': newText,
                'pos': image.pos,
                # 'extension': image.extension
            }
        )
    newText = web_story.cover_text
    if newText=="some-text":
        newText = " "
    data = {
        'cover': {
            'image': web_story.cover_url,
            'text': newText,
            'title': web_story.cover_title,
        },
        'images': imagesData
    }
    # data = {
    #     'cover': {
    #         'image': "https://picsum.photos/720/1080",
    #         'text': "TRIAll",
    #         'title': "Trail for Web Stories",
    #     },
    #     'images': [
    #         {
    #             'image': "https://picsum.photos/1080/1080",
    #             'text': "With $3.19 billion India's stock market slips to 6th position.",
    #             'pos': 1,
    #             'extension': 'jpg'
    #         },
    #         {
    #             'image': "https://picsum.photos/1080/1080",
    #             'text': "Indian business man Adani's companies shares crashed by 30% after Hinderburg report.",
    #             'pos': 2,
    #             'extension': 'jpg'
    #         },
    #     ],
    #     'permalink': "trail-for-web-stories",
    # }
    return render(req, 'story.html', data)

@api_view(['POST'])
def create_story(req):

    print(req.data)
    serializer = WebStorySerializer(data=req.data)
    if(serializer.is_valid()):
        serializer.save()
    else :
        print("Dgd")
        print(serializer.errors)
        return JsonResponse({'message': 'Some error while adding. Try again after some time '}, status=400)
        
    return JsonResponse({'data':serializer.data,"message":"Successfully Inserted"},status=200)

def robots(req):
    return render(req,'robots.txt', content_type='text/plain')

def google(req):
    return render(req,'googleb02030bfd53db826.html')

def handler404(request, exception,template_name= "404.html"):
    response = render(request,template_name)
    response.status_code = 404
    return response

# def handler500(request, exception,template_name= "500.html"):
#     response = render(request,template_name)
#     response.status_code = 500
#     return response
