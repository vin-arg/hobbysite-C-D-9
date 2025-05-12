from django.db.models import Case, When, IntegerField
from django.shortcuts import render
from .models import Commission

def commissions_list(request):
    commissions = Commission.objects.order_by(
        Case(
            When(status='Open', then=0),
            When(status='Full', then=1),
            When(status='Completed', then=2),
            When(status='Discontinued', then=3),
            output_field=IntegerField()
        ),
        '-created_on'
    )
    ctx = {
        'commissions': commissions
    }
    
    if request.user.is_authenticated:
        profile = request.user.profile
        ctx.update({
            'user_commissions': profile.commissions.all().order_by('-created_on'),
            'applied_commissions': Commission.objects.filter(
                jobs__applications__applicant=profile
            ).distinct().order_by('-created_on')
        })
        
    return render(request, 'commission_content.html', ctx)

def commissions_detail(request, pk):
    commission_info = Commission.objects.get(pk=pk)
    ctx = {
        'comments': commission_info.comments.all(),
        'commission': commission_info
    }
    return render(request, 'commission_comments.html', ctx)