from django.shortcuts import render, get_object_or_404, redirect
from .models import Campaign
from .forms import CampaignForm

# List all campaigns
def campaign_list(request):
    campaigns = Campaign.objects.all()
    is_admin = request.user.is_staff  # True if the user is admin
    return render(request, 'organisms/campaign_list.html', {
        'campaigns': campaigns,
        'is_admin': is_admin
    })

# Campaign detail
def campaign_detail(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    is_admin = request.user.is_staff
    return render(request, 'organisms/campaign_detail.html', {
        'campaign': campaign,
        'is_admin': is_admin
    })

# Create a new campaign
def campaign_create(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            campaign = form.save()
            return redirect('campaigns:campaign_detail', pk=campaign.pk)
    else:
        form = CampaignForm()
    return render(request, 'organisms/campaign_form.html', {'form': form})

# Update an existing campaign
def campaign_update(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES, instance=campaign)
        if form.is_valid():
            form.save()
            return redirect('campaigns:campaign_detail', pk=campaign.pk)
    else:
        form = CampaignForm(instance=campaign)
    return render(request, 'organisms/campaign_form.html', {'form': form})

# Delete a campaign
def campaign_delete(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    if request.method == 'POST':
        campaign.delete()
        return redirect('campaigns:campaign_list')
    return render(request, 'organisms/campaign_confirm_delete.html', {'campaign': campaign})
