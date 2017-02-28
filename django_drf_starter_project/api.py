rom tastypie.resources import Resource

from .models import Post

class AjaxSearchResource(Resource):

    class Meta:
        resource_name = 'ajaxsearch'
        allowed_methods = ['post']

    def diveshop_list(self, request, **kwargs):
        phrase = request.POST.get('q')
        if phrase:
            diveshops = list(Post.objects.filter(location__icontains=phrase).values('id', 'location'))
            return self.create_response(request, {'diveshops': diveshops})
