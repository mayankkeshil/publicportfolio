import boto3
import os
from django.http import JsonResponse

def test_upload(request):
    try:
        s3 = boto3.client(
            "s3",
            endpoint_url=f"{os.getenv('SUPABASE_URL')}/storage/v1/s3",
            aws_access_key_id=os.getenv("SUPABASE_S3_ACCESS_KEY"),
            aws_secret_access_key=os.getenv("SUPABASE_S3_SECRET_KEY"),
            region_name="us-east-1"
        )

        # Try uploading a tiny fake file
        s3.put_object(
            Bucket="media",
            Key="test_upload.txt",
            Body=b"hello world"
        )

        return JsonResponse({"success": True, "message": "Upload worked"})

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})
