# project/app/models/tortoise.py

from tortoise.models import Model
from tortoise import fields

class TextSummary(Model):
    url = fields.TextField()    
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url