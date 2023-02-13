from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from stories.models import AllImage, WebStory
from rest_framework.decorators import api_view
from websstories.settings import TOKEN
from .serializers import WebStorySerializer


def index(req):
    data = {}
    storyList = []
    webstories = WebStory.objects.all()
    for story in webstories:
        storyList.append({
            'image' : story.images.first().image_url,
            'link' : story.permalink,
            'title' : story.cover_title,
        })
    data['webstories'] = storyList
    return render(req, 'index.html',data)

def about(req):
    return render(req, 'about.html')

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def uploadPosts(request):
    if request.method == 'POST':
        authorization_header = request.headers.get('Authorization')
        print(authorization_header)
        if authorization_header:
            token = authorization_header
            if token == TOKEN:
                image = request.FILES.get('image')
                image_title = request.POST.get('image_title')
                if image:
                    try:
                        all_image = AllImage(image=image, image_title=image_title)
                        all_image.save()
                        image_url = all_image.image.url
                        return JsonResponse({'success': True,'image_url': image_url})
                    except Exception as e:
                        return JsonResponse({'success': False, 'error': str(e)})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid Authorization Token'})
        else:
            return JsonResponse({'success': False, 'error': 'Authorization header not found'})
    return JsonResponse({'success': False, 'error': 'Bad Request'})


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
