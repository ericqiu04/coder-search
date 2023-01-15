from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import logging

logger = logging.getLogger('django')

from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt)
@csrf_exempt
def submit(request):
    if request.method == 'POST':
        print("work")
        input_data = request.POST.get('input_data')

        if input_data:
            print(input_data) # You should see the input data here
        else:
            print('input_data not found')
            # Do something with input_dataqw
        return JsonResponse({'data': input_data})
    return JsonResponse({'status': 'error'})

# Create your views here.

def front(request):
    context = { }
    print(10)
    return render(request, "index.html", context)