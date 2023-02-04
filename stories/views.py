from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from stories.models import WebStory
from rest_framework.decorators import api_view
from .serializers import WebStorySerializer


def index(req):
    return HttpResponse("HELLO TO INSED PAGE")

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


# @api_view(['POST'])
# def create_web_story(request):
#     if request.method == 'POST':
#         data = request.POST.get('data')
#         web_story_data = data.get('web_story')
        
#         web_story = WebStory.objects.create(
#             permalink=web_story_data.get('permalink'),
#             cover_url=web_story_data.get('cover_url'),
#             cover_text=web_story_data.get('cover_text'),
#             cover_title=web_story_data.get('cover_title'),
#             cover_extension=web_story_data.get('cover_extension')
#         )
        
#         for image_data in data.get('images'):
#             Image.objects.create(
#                 web_story=web_story,
#                 text=image_data.get('text'),
#                 image_url=image_data.get('image_url'),
#                 pos=image_data.get('pos'),
#                 extension=image_data.get('extension')
#             )
        
#         return render(request, 'web_story_created.html', {'web_story': web_story})
#     return render(request, 'create_web_story.html')


