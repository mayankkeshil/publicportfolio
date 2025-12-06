import os
from django.core.files.storage import Storage
from django.conf import settings
from supabase import create_client

class SupabaseStorage(Storage):

    def __init__(self):
        self.client = create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_SERVICE_KEY
        )
        self.bucket = "media"

    def _save(self, name, content):
        data = content.read()
        result = self.client.storage.from_(self.bucket).upload(
            path=name,
            file=data,
            upsert=True
        )
        return name

    def url(self, name):
        return (
            f"{settings.SUPABASE_URL}/storage/v1/object/public/"
            f"{self.bucket}/{name}"
        )
