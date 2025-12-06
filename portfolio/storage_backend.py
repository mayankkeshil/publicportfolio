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

        # Upload to Supabase Storage (correct syntax)
        result = self.client.storage.from_(self.bucket).upload(
            path=name,
            file=data,
        )

        # If file already exists, you must delete then upload again
        if "error" in result and result["error"].get("status_code") == "409":
            # File exists → delete and retry upload
            self.client.storage.from_(self.bucket).remove([name])
            self.client.storage.from_(self.bucket).upload(
                path=name,
                file=data,
            )

        return name


    def url(self, name):
        return (
            f"{settings.SUPABASE_URL}/storage/v1/object/public/"
            f"{self.bucket}/{name}"
        )

    def exists(self, name):
        # Check if file exists in Supabase Storage
        try:
            resp = self.client.storage.from_(self.bucket).list(
                path=os.path.dirname(name) or "",
            )

            filenames = [item['name'] for item in resp]
            return os.path.basename(name) in filenames

        except Exception:
            return False
