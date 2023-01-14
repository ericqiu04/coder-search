from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import logging

logger = logging.getLogger('django')

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
class InputView(View):
   def submit(request):
    if request.method == 'POST':
        input_data = request.POST.get('input_data')
        # Do something with input_data
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})


# Create your views here.
def front(request):
    context = { }
    print(10)
    return render(request, "index.html", context)