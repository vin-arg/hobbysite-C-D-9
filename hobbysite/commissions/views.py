from django.db.models import Case, When, IntegerField, Sum
from django.shortcuts import render, get_object_or_404, redirect
from .models import Commission, Job, JobApplication
from .forms import JobApplicationForm, CommissionForm, JobFormSet
from django.contrib.auth.decorators import login_required

def commission_list(request):
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
            'user_commissions': Commission.objects.filter(author=profile),
            'applied_commissions': Commission.objects.filter(
                jobs__applications__applicant=profile
            ).distinct().order_by('-created_on')
        })
        
    return render(request, 'commission_list.html', ctx)

def commission_detail(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    
    total_manpower = commission.jobs.aggregate(
        total=Sum('manpower_required')
    )['total'] or 0
    
    accepted_applications = JobApplication.objects.filter(
        job__commission=commission,
        status='Accepted'
    ).count()
    
    jobs = []
    for job in commission.jobs.all():
        accepted_count = job.applications.filter(status='Accepted').count()
        jobs.append({
            'object': job,
            'can_apply': (
                request.user.is_authenticated and 
                not request.user.profile == commission.author and
                accepted_count < job.manpower_required
            ),
            'remaining_positions': job.manpower_required - accepted_count,
            'form': JobApplicationForm(initial={'job': job.id}) if request.user.is_authenticated else None
        })
    
    ctx = {
        'commission': commission,
        'jobs': jobs,
        'total_manpower': total_manpower,
        'open_manpower': total_manpower - accepted_applications,
        'can_edit': request.user.is_authenticated and request.user.profile == commission.author
    }
    
    return render(request, 'commission_detail.html', ctx)

@login_required
def commission_create(request):
    form = CommissionForm()
    
    if request.method == 'POST':
        form = CommissionForm(request.POST)
        formset = JobFormSet(request.POST, queryset=Job.objects.none())

        if form.is_valid():
            commission = form.save(commit=False)
            commission.author = request.user.profile
            commission.save()

            if formset.is_valid():
                for job_form in formset:
                    if job_form.cleaned_data:
                        job = job_form.save(commit=False)
                        job.commission = commission
                        job.save()

            return redirect('commissions:commissions_detail', pk=commission.pk)
    else:
        form = CommissionForm()
        formset = JobFormSet(queryset=Job.objects.none())

    return render(request, 'commission_form.html', {'form': form,'formset': formset})

@login_required
def commission_update(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    
    if commission.author != request.user.profile:
        return redirect('commissions:commissions_list')
    
    if request.method == 'POST':
        form = CommissionForm(request.POST, instance=commission)
        formset = JobFormSet(request.POST, instance=commission)

        if form.is_valid() and formset.is_valid():
            commission = form.save()
            formset.save()

            if commission.jobs.exclude(status='Full').count() == 0:
                commission.status = 'Full'
                commission.save()

            return redirect('commissions:commissions_detail', pk=commission.pk)
    else:
        form = CommissionForm(instance=commission)
        formset = JobFormSet(instance=commission)
    
    ctx = {
        'form': form,
        'formset': formset,
        'commission': commission,
        'editing': True
    }

    return render(request, 'commission_form.html', ctx)
    
@login_required
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    applications = JobApplication.objects.filter(job=job).select_related('applicant')

    is_owner = job.commission.author == request.user.profile

    if request.method == 'POST' and is_owner:
        for application in applications:
            status_key = f'status_{application.id}'
            new_status = request.POST.get(status_key)
            if new_status and new_status != application.status:
                application.status = new_status
                application.save()
        return redirect('commissions:job_detail', job_id=job.id)
    
    ctx = {'job': job,
           'applications': applications,
           'is_owner': is_owner,}

    return render(request, 'commissions:job_detail.html', ctx)