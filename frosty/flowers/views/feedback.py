from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from ..models import User, Feedback
from ..forms import FeedbackForm


@csrf_exempt
@login_required
@user_passes_test(User.is_buyer)
def create_feedback(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    form = FeedbackForm(request.POST)
    if not form.is_valid():
        return JsonResponse(form.errors.get_json_data(), status=400)

    cd = form.cleaned_data
    Feedback.objects.create(author=request.user, **cd)
    return HttpResponse('Ok')
