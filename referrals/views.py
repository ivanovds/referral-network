from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def referral_view(request):
    """Displays links to all referral of current user and their amount."""
    ref_list = request.user.user_referrers.all()
    ref_count = ref_list.count()
    context = {
        'ref_count': ref_count,
        'ref_list': ref_list,
    }
    return render(request, "referrals.html", context)

