from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import BlogPost, BlogCategory
from .forms import BlogPostForm, SearchForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.db.models import Q
from django.db.models import Count


class BlogPostListView(ListView):
    template_name = "blog/blog.html"
    context_object_name = "posts"
    paginate_by = 12

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        self.paginator = Paginator(self.object_list, self.paginate_by)
        page_number = request.GET.get("page")
        self.page = self.paginator.get_page(page_number)
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_queryset(self):
        return BlogPost.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = BlogCategory.objects.annotate(num_items=Count("items"))
        categories_with_items = categories.filter(num_items__gt=0)
        context["page"] = self.page
        context[
            "title"
        ] = "SEO_Tech | Сборник новостей и статей о SEO, программировании и маркетинге"
        context["categories"] = categories_with_items
        return context


def BlogCategoryView(request, cat_slug):
    category = BlogCategory.objects.filter(slug=cat_slug).first()
    posts = BlogPost.objects.filter(category=category, is_active=True)
    context = {"category": category, "posts": posts}
    return render(request, "blog/blog.html", context)


class BlogPostDetailView(DetailView):
    model = BlogPost
    context_object_name = "post"
    template_name = "blog/blog_post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_post = self.object
        blog_post.add_view()
        blog_post.save()
        context["title"] = f"{blog_post.title} | SEO_Tech"
        same_articles = BlogPost.objects.filter(category=blog_post.category)
        same_articles = same_articles.exclude(pk=blog_post.pk)
        context["same_articles"] = same_articles

        return context


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = "blog/update.html"
    form_class = BlogPostForm

    def get_success_url(self):
        return reverse("blog:article", kwargs={"slug": self.kwargs["slug"]})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["slug"] = self.object.slug
        return context


def search(request):
    form = SearchForm()
    query = None

    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            posts = BlogPost.objects.filter(title__icontains=query)
            print(posts)
            context = {"posts": posts, "form": form}
            return render(request, "blog/blog.html", context)
