from django.shortcuts import render

def home(request):
    """Homepage view"""
    try:
        from articles.models import Article
        from campaigns.models import Campaign
        
        featured_articles = Article.objects.filter(status='published', is_featured=True)[:3]
        featured_campaigns = Campaign.objects.filter(status='upcoming', is_featured=True)[:3]
        recent_articles = Article.objects.filter(status='published')[:6]
        
        context = {
            'featured_articles': featured_articles,
            'featured_campaigns': featured_campaigns,
            'recent_articles': recent_articles,
        }
    except:
        context = {
            'featured_articles': [],
            'featured_campaigns': [],
            'recent_articles': [],
        }
    
    return render(request, 'pages/home.html', context)

def about(request):
    """About page view"""
    return render(request, 'pages/about.html')  

def profile(request):
    """Profile page view"""
    return render(request, 'pages/profile.html')

def my_campaigns(request):
    """My Campaigns page view"""
    return render(request, 'pages/my_campaigns.html')
