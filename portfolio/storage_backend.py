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

    def exists(self, name):
        try:
            files = self.client.storage.from_(self.bucket).list(path=name)
            return len(files) > 0
        except Exception:
            return False

    def _save(self, name, content):
        data = content.read()

        # Try upload
        resp = self.client.storage.from_(self.bucket).upload(
            path=name,
            file=data
        )

        # If file exists, Supabase returns an error description inside resp
        if hasattr(resp, "error") and resp.error:
            if resp.error.get("status_code") == "409":
                # Remove old file
                self.client.storage.from_(self.bucket).remove([name])

                # Upload again
                resp = self.client.storage.from_(self.bucket).upload(
                    path=name,
                    file=data
                )

        return name

    def url(self, name):
        return (
            f"{settings.SUPABASE_URL}/storage/v1/object/public/"
            f"{self.bucket}/{name}"
        )
