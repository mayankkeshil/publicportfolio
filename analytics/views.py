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

def dashboard_view(request):
    page_views = Event.objects.filter(event_type="page_view").count()
    clicks = Event.objects.filter(event_type="click").count()

    context = {
        "page_views": page_views,
        "clicks": clicks,
    }
    return render(request, "analytics/dashboard.html", context)