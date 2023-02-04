# # # from rest_framework import serializers
from .models import WebStory, Image
# # # import numpy as np
# # # import requests
# # # from io import BytesIO
# # # import cv2
# # # from PIL import Image as pil_image

# # # class ImageSerializer(serializers.ModelSerializer):
# # #     class Meta:
# # #         model = Image
# # #         fields = ['image', 'text', 'pos', 'extension']

# # # class WebStorySerializer(serializers.ModelSerializer):
# # #     images = ImageSerializer(many=True)

# # #     class Meta:
# # #         model = WebStory
# # #         fields = ['cover_image', 'cover_text', 'cover_title', 'images']

# # #     def create(self, validated_data):
# # #         images_data = validated_data.pop('images')
# # #         cover_image_url = validated_data.pop('cover_image')
# # #         response = requests.get(cover_image_url)
# # #         img = pil_image.open(BytesIO(response.content))
# # #         image = np.array(img)
# # #         print("Vdv")
# # #         height, width, _ = image.shape
# # #         for row in range(height):
# # #             for col in range(width):
# # #                 image[row, col, :] = image[row, col, :] * (1 - row / height)
# # #         cover_image = self.save_cover_image(image)
# # #         web_story = WebStory.objects.create(cover_image=cover_image, **validated_data)
# # #         print("Vdvadaa")
# # #         for image_data in images_data:
# # #             response = requests.get(image_data['image'])
# # #             img = pil_image.open(BytesIO(response.content))
# # #             image = np.array(img)
# # #             height, width, _ = image.shape
# # #             for row in range(height):
# # #                 for col in range(width):
# # #                     image[row, col, :] = image[row, col, :] * (1 - row / height)
# # #             image = self.save_image(image)
# # #             Image.objects.create(web_story=web_story, image=image, **image_data)
# # #         return web_story

# # #     def save_cover_image(self, image):
# # #         cover_image_path = "static/cover/cover_image.jpg"
# # #         cv2.imshow(image)
# # #         pil_image.fromarray(image).save(cover_image_path)
# # #         return cover_image_path

# # #     def save_image(self, image):
# # #         image_path = "static/images/image.jpg"
# # #         pil_image.fromarray(image).save(image_path)
# # #         return image_path


# # from rest_framework import serializers
# # from .models import WebStory, Image

# # class ImageSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Image
        # fields = ('image_url',  'text', 'pos', 'extension')


# # class WebStorySerializer(serializers.ModelSerializer):
# #     images = ImageSerializer(many=True)

# #     class Meta:
# #         model = WebStory
# #         fields = ('permalink', 'cover_url', 'cover_text', 'cover_title', 'cover_extension', 'images')

# #     def create(self, validated_data):
# #         images_data = validated_data.pop('images')
# #         web_story = WebStory.objects.create(**validated_data)
# #         for image_data in images_data:
# #             Image.objects.create(web_story=web_story, **image_data)
# #         return web_story
# from rest_framework import serializers
# from .models import WebStory, Image

# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = ('image_url',  'text', 'pos', 'extension')

# class WebStorySerializer(serializers.ModelSerializer):
#     images = ImageSerializer(many=True, required=False)

#     class Meta:
#         model = WebStory
#         # fields = ['cover_url', 'cover_text', 'cover_title', 'cover_extension','permalink','images']
#         fields = '__all__'
#     def create(self, validated_data):
#         images_data = validated_data.pop('images', [])
#         webstory = WebStory.objects.create(**validated_data)
#         for image_data in images_data:
#             Image.objects.create(web_story=webstory, **image_data)
#         return webstory

#     def update(self, instance, validated_data):
#         images_data = validated_data.pop('images', [])
#         instance.permalink = validated_data.get('permalink', instance.permalink)
#         # instance.cover_image = validated_data.get('cover_image', instance.cover_image)
#         instance.cover_url = validated_data.get('cover_url', instance.cover_url)
#         instance.cover_text = validated_data.get('cover_text', instance.cover_text)
#         instance.cover_title = validated_data.get('cover_title', instance.cover_title)
#         instance.cover_extension = validated_data.get('cover_extension', instance.cover_extension)
#         instance.save()

#         existing_images = Image.objects.filter(web_story=instance)
#         existing_image_ids = {image.id for image in existing_images}

#         for image_data in images_data:
#             image_id = image_data.get('id')
#             if image_id:
#                 existing_image_ids.remove(image_id)
#                 image = Image.objects.get(id=image_id)
#                 image.text = image_data.get('text', image.text)
#                 # image.image = image_data.get('image', image.image)
#                 image.image_url = image_data.get('image_url', image.image_url)
#                 image.pos = image_data.get('pos', image.pos)
#                 image.extension = image_data.get('extension', image.extension)
#                 image.save()
#             else:
#                 Image.objects.create(web_story=instance, **image_data)

#         for existing_image_id in existing_image_ids:
#             Image.objects.get(id=existing_image_id).delete()

#         return instance


from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image_url',  'text', 'pos')

class WebStorySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = WebStory
        fields = '__all__'

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        web_story = WebStory.objects.create(**validated_data)
        for image_data in images_data:
            Image.objects.create(web_story=web_story, **image_data)
        return web_story


