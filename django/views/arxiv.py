from django.http import HttpResponse
from arxiv import arxiv_api 
import json 

def index(request):
    results = arxiv_api.fetch_papers()
    return HttpResponse(json.dumps(results, indent=4))
    