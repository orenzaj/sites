import json

from django.utils.safestring import mark_safe
from django.views.generic import TemplateView


class ChatAppView(TemplateView):
    template_name = "apps/chat/index.html"


class RoomView(TemplateView):
    template_name = "apps/chat/room.html"

    def get_context_data(self, room_name, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Add to context
        context["room_name"] = mark_safe(json.dumps(room_name))
        return context
