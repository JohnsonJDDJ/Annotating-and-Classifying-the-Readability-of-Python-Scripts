from django.db import models
from django.contrib.auth.models import User
from io import BytesIO
import sys
print(sys.path)
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


# Create your models here.

class Blog_Post(models.Model, object):
    image = models.ImageField(blank= True, upload_to='get_upload_file_name')
    title = models.CharField(blank=True, max_length = 100)
    summary = models.TextField(blank= True, max_length =30)
    body = models.TextField(blank=True)
    slug = models.SlugField( unique=True)
    writer = models.ForeignKey(User,on_delete= models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    def save(self):
        # Opening the uploaded image
        im = Image.open(self.image)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((1024, 720))

        # after modifications, save it to the output
        im.save(output, format='png', quality=300)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.webp" % self.image.name.split('.')[0], 'image/webp',
                                        sys.getsizeof(output), None)

        super(Blog_Post, self).save()

class Comment(models.Model):
        commenter = models.CharField(max_length=15)
        body = models.TextField(max_length=30, blank=True)
        post = models.ForeignKey(Blog_Post, on_delete=models.CASCADE, related_name='comments')
        date = models.DateField(auto_now_add=True)
        like = models.BooleanField(default=True)
        def __str__(self) -> str:
             return self.commenter



class Meta:
    ordering = ('-created_at',)

   