import os
from django.core.files.storage import Storage
from django.conf import settings
from supabase import create_client

class SupabaseStorage(Storage):

    def __init__(self):
        self.client = create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_SERVICE_KEY  # service key = full access
        )
        self.bucket = "media"

    def _save(self, name, content):
        # Upload file to supabase bucket
        data = content.read()

        result = self.client.storage.from_(self.bucket).upload(
            file=data,
            path=name,
            file_options={"content_type": content.content_type},
            upsert=True,
        )

        if "error" in result and result["error"]:
            raise Exception(f"Supabase upload failed: {result['error']['message']}")

        return name

    def url(self, name):
        # Public URL (your bucket must be public, which yours already is)
        return f"{settings.SUPABASE_URL}/storage/v1/object/public/{self.bucket}/{name}"
