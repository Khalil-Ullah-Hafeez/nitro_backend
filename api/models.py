from django.db import models

import PIL.Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile

from .image_manipulation import shadowDetection, computeResult


# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to='images')
    processed_photo = models.ImageField(upload_to='processed_images')

    def detectshadow(self):
        pil_image = PIL.Image.open(self.photo)
        cv_image = np.array(pil_image)
        
        
        processed_img = shadowDetection(cv_image)

        img_pil = PIL.Image.fromarray(processed_img)

        buffer = BytesIO()
        img_pil.save(buffer, format='png')
        image_png = buffer.getvalue()


        self.processed_photo.save(str(self.processed_photo), ContentFile(image_png))


    def compute(self, days):
        pil_image = PIL.Image.open(self.photo)
        return computeResult(pil_image, days)
