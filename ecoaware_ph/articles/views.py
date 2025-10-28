from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm


# =========================================================
# LIST ALL ARTICLES
# =========================================================
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'organisms/article_list.html', {'articles': articles})


# =========================================================
# CREATE NEW ARTICLE
# =========================================================
@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)   # Don't save yet
            article.author = request.user       # Assign logged-in user
            article.save()                      # Save article
            form.save_m2m()                     # Save tags (ManyToMany)
            return redirect('articles:article_detail', slug=article.slug)
    else:
        form = ArticleForm()
    return render(request, 'organisms/article_form.html', {'form': form})


# =========================================================
# VIEW ARTICLE DETAIL
# =========================================================
def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.views += 1
    article.save(update_fields=['views'])
    return render(request, 'organisms/article_detail.html', {'article': article})


# =========================================================
# UPDATE ARTICLE
# =========================================================
@login_required
def article_update(request, slug):
    article = get_object_or_404(Article, slug=slug)

    # Optional: Restrict editing to the article’s author
    if article.author != request.user:
        return redirect('articles:article_detail', slug=article.slug)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:article_detail', slug=article.slug)
    else:
        form = ArticleForm(instance=article)

    return render(request, 'organisms/article_form.html', {'form': form})


# =========================================================
# DELETE ARTICLE
# =========================================================
@login_required
def article_delete(request, slug):
    article = get_object_or_404(Article, slug=slug)

    # Optional: Restrict deletion to the author
    if article.author != request.user:
        return redirect('articles:article_detail', slug=article.slug)

    if request.method == 'POST':
        article.delete()
        return redirect('articles:article_list')

    return render(request, 'organisms/article_confirm_delete.html', {'article': article})
