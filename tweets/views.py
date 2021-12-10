from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Tweet
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)

def tweet_list_view(request, *args, **kwargs):
    """REST API View
    consume by Javascript or swift/Java/ios/android
    return json data
    """
    qs= Tweet.objects.all()
    tweets_list = [{"id": x.id,"content":x.content} for x in qs]
    data = {"response":tweets_list}
    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """REST API View
    consume by Javascript or swift/Java/ios/android
    return json data
    """
    data = {
        "id": tweet_id,
        # "image_path": obj.image.url 
    }
    status=200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status) # json.dumps content_type='app
    #return HttpResponse(f"<h1>Hello {tweet_id} - {obj.content} </h1>")

