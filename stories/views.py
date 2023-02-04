from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from stories.models import WebStory
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import WebStorySerializer
import cv2
import requests
from io import BytesIO
from PIL import Image
import numpy as np

# Create your views here.


def index(req):
    return HttpResponse("HELLO TO INSED PAGE")

import os
def story(req, link):
    web_story = WebStory.objects.get(permalink=link)
    images = web_story.images.all()
    imagesData = []
    for image in images:
        # os.path.dirname(image.image)
        # print(web_story.cover_image.file[3])

        imagesData.append(
            {
                'image': image.image_url,
                'text': image.text,
                'pos': image.pos,
                # 'extension': image.extension
            }
        )
    data = {
        'cover': {
            'image': web_story.cover_url,
            'text': web_story.cover_text,
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
    # if (req.method == "POST"):
    #     print(req.POST.get('name'))
    # print("brsb")
    # print(req.GET.getlist('images'))
    # name = req.GET.get('name')
    print(req.data)
    serializer = WebStorySerializer(data=req.data)
    if(serializer.is_valid()):
        serializer.save()
    else :
        print("Dgd")
        print(serializer.errors)
        return JsonResponse({'message': 'Some error while adding. Try again after some time '}, status=400)
        
    return JsonResponse({'data':serializer.data,"message":"Successfully Inserted"},status=200)


# import numpy as np
# from PIL import Image

# from io import BytesIO
# import requests
# from rest_framework import viewsets
# from rest_framework.response import Response

# from .serializers import WebStorySerializer
# from .models import WebStory, Image
# from django.core.files.uploadedfile import SimpleUploadedFile

# class WebStoryViewSet(viewsets.ModelViewSet):
#     queryset = WebStory.objects.all()
#     serializer_class = WebStorySerializer

#     def create(self, request, *args, **kwargs):
#         cover_image = request.data.get("cover_image")
#         cover_text = request.data.get("cover_text")
#         cover_title = request.data.get("cover_title")
#         permalink = request.data.get("permalink")
#         images = request.data.get("images")

#         img = Image.open(BytesIO(requests.get(cover_image).content))
#         # img = Image.open(BytesIO(requests.get(cover_image).content))
#         height, width, _ = np.array(img).shape

#         for row in range(height):
#             for col in range(width):
#                 image[row, col, :] = image[row, col, :] * (1 - row / height)

#         cover_img = Image.fromarray(image)
#         cover_img_file = BytesIO()
#         cover_img.save(cover_img_file, 'JPEG')

#         cover = WebStory.objects.create(
#             cover_text=cover_text,
#             cover_title=cover_title,
#             permalink=permalink,
#             cover_image=SimpleUploadedFile(
#                 name='cover.jpeg', content=cover_img_file.getvalue(), content_type='image/jpeg')
#         )

#         for image_data in images:
#             image = image_data.get("image")
#             text = image_data.get("text")
#             pos = image_data.get("pos")
#             extension = image_data.get("extension")

#             img = Image.open(BytesIO(requests.get(image).content))
#             height, width, _ = np.array(img).shape

#             for row in range(height):
#                 for col in range(width):
#                     image[row, col, :] = image[row, col, :] * (1 - row / height)

#             image_obj = Image.fromarray(image)
#             image_file = BytesIO()
#             image_obj.save(image_file, extension.upper())

#             Image.objects.create(
#                 web_story=cover,
#                 text=text,
#                 pos=pos,
#                 extension=extension,
#                 image=SimpleUploadedFile(
#                     name=f'{pos}.{extension}', content=image_file.getvalue(), content_type=f'image/{extension}')
#             )

#         serializer = self.get_serializer(cover)
#         return Response(serializer.data)
import requests

def handle_images(req):
    data = {
        "cover_image": "https://picsum.photos/720/1080",
        "cover_text": "scs",
        "cover_title": "Ukraine to get Rafale",
        "permalink": "ukraine-to-get-rafale"
    }
    link = data['cover_image']
    print(link)
    img = Image.open(BytesIO(requests.get(link).content))
    image = np.array(img)
    height, width, _ = image.shape

    for row in range(height):
        for col in range(width):
            image[row, col, :] = image[row, col, :] * (1 - row / height)


    result = request.urlretrieve(link)
        # self.image_file.save(
      
        #         )
        # self.save()

    w = WebStory.objects.create(
        cover_title=data['cover_title'],
        cover_text=data['cover_text'],
        permalink=data['permalink'],
        cover_image=image)
    if(w.is_valid()):
        w.save()
    return JsonResponse({"link": link})
    pass


@api_view(['POST'])
def create_web_story(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        web_story_data = data.get('web_story')
        
        web_story = WebStory.objects.create(
            permalink=web_story_data.get('permalink'),
            cover_url=web_story_data.get('cover_url'),
            cover_text=web_story_data.get('cover_text'),
            cover_title=web_story_data.get('cover_title'),
            cover_extension=web_story_data.get('cover_extension')
        )
        
        for image_data in data.get('images'):
            Image.objects.create(
                web_story=web_story,
                text=image_data.get('text'),
                image_url=image_data.get('image_url'),
                pos=image_data.get('pos'),
                extension=image_data.get('extension')
            )
        
        return render(request, 'web_story_created.html', {'web_story': web_story})
    return render(request, 'create_web_story.html')


