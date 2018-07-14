from django.http import Http404
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404, redirect

from books.forms import ProfileForm
from .models import Profile

# Create your views here.

# def profile_page(request):
#     return render(request,"profiles/view.html", {})

# class CreateProfile():
def profileCreate(request):
    profile_obj, new_profile = Profile.profile_obj.new_or_get(request)
    return render(request, "profiles/view.html", {"profile": profile_obj})


class ProfileDetailSlugView(DetailView):
    queryset = Profile.profile_obj.all()
    template_name = "profiles/view.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug= self.kwargs.get('slug')

        try:
            instance = Profile.profile_obj.get(slug=slug)
        except Profile.DoesNotExist:
            raise Http404("Not found ...")
        except Profile.MultipleObjectsReturned:
            qs = Profile.profile_obj.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Something unexpected happened :(")
        return instance

class ProfileDetailView(DetailView):
    template_name = "profiles/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk= self.kwargs.get('pk')
        instance = Profile.profile_obj.get_by_id(pk)
        if instance is None:
            raise Http404("Profile does not exist")
        return instance

def profile_detail_view(request, pk=None, *args, **kwargs):

	instance = Profile.profile_obj.get_by_id(pk)
	if instance is None:
		raise Http404("Profile does not exist")

	context = {
		'object': instance
	}
	return render(request, "profiles/view.html", context)