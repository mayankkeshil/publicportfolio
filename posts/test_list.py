import boto3
import os
from django.http import JsonResponse

def list_files(request):
    s3 = boto3.client(
        "s3",
        endpoint_url=f"{os.getenv('SUPABASE_URL')}/storage/v1/s3",
        aws_access_key_id=os.getenv("SUPABASE_S3_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("SUPABASE_S3_SECRET_KEY"),
        region_name="us-east-1"
    )

    files = s3.list_objects_v2(Bucket="media")

    if "Contents" not in files:
        return JsonResponse({"files": []})

    return JsonResponse({
        "files": [obj["Key"] for obj in files["Contents"]]
    })
