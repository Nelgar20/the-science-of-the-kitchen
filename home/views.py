from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Render the landing page without querying the database."""

    template_name = "home/home.html"
