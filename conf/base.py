from django.db import models
from datetime import datetime

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True)
    is_deleted = models.BooleanField(default=False)


    class Meta:
        abstract = True
    


    def delete(self, using=None, Keep_parents=False):
        self.is_deleted = True
        self.deleted = datetime.now()
        self.save()