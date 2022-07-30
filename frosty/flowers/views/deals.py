from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import JsonResponse
from ..models import DealLots, User


@login_required
@user_passes_test(User.is_seller)
def deal_lots_list(request):
    deals = DealLots.objects.all().values()
    return JsonResponse({'deals': list(deals)})
