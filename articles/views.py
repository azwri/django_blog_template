from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Tag
from .forms import ArticleFormCreate, TagFormCreate


def index(request):
    articles = Article.objects.select_related('author', 'author__profile').prefetch_related('tags').all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk:int):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    form = ArticleFormCreate()
    if request.method == 'POST':
        form = ArticleFormCreate(request.POST or None, request.FILES or None)
        if form.is_valid():
            # title = form.cleaned_data['title']
            # body = form.cleaned_data['body']
            # author = form.cleaned_data['author']
            # tags = form.cleaned_data['tags']
            # image = request.FILES['image']
            # article = Article.objects.create(
            #     title=title, body=body, author=author, image=image
            # )
            # article.tags.set(tags)
            form.save()
            return redirect('articles:index')
    else:
        context = {'form': form}
        return render(request, 'articles/create.html', context)
    
def create_tag(request):
    if request.method == 'POST':
        form = TagFormCreate(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            name = form.cleaned_data['name']
            tag = Tag.objects.create(name=name)
            return redirect('articles:index')
        
    else:
        form = TagFormCreate()
        context = {
            'form': form
        }
        return render(request, 'articles/create_tag.html', context)
    
def update_article(request, pk:int):
    article = get_object_or_404(Article,pk=pk)
    form = ArticleFormCreate(instance=article)
    if request.method == 'POST':
        form = ArticleFormCreate(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    
    else:
        context = {"form": form}
        return render(request, 'articles/create.html', context)

def update_tag(request, pk:int):
    tag = get_object_or_404(Tag, pk=pk)
    form = TagFormCreate(instance=tag)
    if request.method == 'POST':
        form = TagFormCreate(request.POST or None, request.POST or None, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        context = {'form': form}
        return render(request, 'articles/create_tag.html', context)