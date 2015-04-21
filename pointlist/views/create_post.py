__author__ = 'ag'

from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from pointlist.forms.tools import DivErrorList
from pointlist.forms.post import PostForm
from pointlist.models import Post
from pointlist.views.homepage import bootstrap
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class CreatePostView(CreateView):
    """
    This the view for handling the user post page.
    """
    form_class = PostForm
    template_name = 'pointlist/post_form.html'
    success_url = "/"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreatePostView, self).dispatch(*args, **kwargs)

    def form_invalid(self, form):
        print 'in form invalid'
        # print 'UID: ' + str(form[''])
        post_form = PostForm(self.request.POST, error_class=DivErrorList)
        return super(CreatePostView, self).form_invalid(post_form)

    def form_valid(self, post_form):
        """
        This method is called when valid form data has been POSTed.
        It should return an HttpResponse.
        """
        print 'in form valid'
        cd = post_form.cleaned_data
        new_post = Post(uid=self.request.user,
                        date=cd['date'],
                        name=cd['name'],
                        description=cd['description'],
                        public_address=cd['public_address'],
                        type_of_post=cd['type_of_post'])
        new_post.save()
        print 'new post saved'
        return bootstrap(self.request)

