# models.py
from django.db import models

class ImportedHTML(models.Model):
    name = models.CharField(max_length=255)
    html_file = models.FileField(upload_to='htmls/')  # Uploads to media/htmls/
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name