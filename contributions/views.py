from django.shortcuts import render
from contributions.models import Contributions
# Create your views here.

def contribution_detail(request, pk):
    contribution = Contributions.objects.get(pk=pk)
    context = {
        "contributions": contribution
    }
    return render(request, "contributions/contribution_detail.html", context)