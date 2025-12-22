from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Event

print("LOADED ANALYTICS VIEWS")

@csrf_exempt
def track_event(request):
    if request.method == "POST":
        data = json.loads(request.body)

        Event.objects.create(
            event_type=data["event_type"],
            page=data.get("page", ""),
            label=data.get("label"),
            session_id=request.session.session_key or "anon"
        )

        return JsonResponse({"status": "ok"})

    return JsonResponse({"error": "POST only"}, status=400)

