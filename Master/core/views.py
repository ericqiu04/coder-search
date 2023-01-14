from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

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
    return render(request, "index.html", context)