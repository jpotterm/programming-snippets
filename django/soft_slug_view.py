# URLs
    url(r'^(?P<pk>\d+)(?:/(?P<slug>[^/]+))?/$', CategoryDetailView.as_view(), name='category_detail'),

# Views
    from dwaiter.dwaiter_django.views import SoftSlugDetailView

    class CategoryDetailView(SoftSlugDetailView):
        context_object_name = 'category'
        model = Category
        template_name = 'category_detail.html'
