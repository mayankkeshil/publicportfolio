from django.db import models

class Event(models.Model):
    EVENT_TYPES = [
        ("page_view", "Page View"),
        ("click", "Click")
    ] 
# Same as
#allowed_values = ["page_view", "click"]
#labels = {
#    "page_view": "Page View",
#    "click": "Click"
#}

    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    page = models.CharField(max_length=200)
    label = models.CharField(max_length=200, null=True, blank=True) # whats label
    session_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.event_type} - {self.page}"