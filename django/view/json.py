from django.views.generic import View

class AjaxView(View):
    def post(self, request, *args, **kwargs):
        result = {'one': 1}

        return http.HttpResponse(
            json.dumps(result),
            content_type='application/json',
        )
