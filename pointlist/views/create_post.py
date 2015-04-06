__author__ = 'ag'

from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from pointlist.forms.tools import DivErrorList
from pointlist.forms.post import PostForm
from django.contrib.auth.decorators import login_required

# @login_required
class CreatePostView(CreateView):
    """
    This the view for handling the user sign up page.
    """
    form_class = PostForm
    template_name = 'pointlist/post_form.html'
    success_url = "/"

    # def request(self):
    #     self.form_class = PostForm(uid=self.request.user)
    # @login_required
    # def dispatch(self):
    # def dispatch(self, *args, **kwargs):
    #     return super(CreatePostView, self).dispatch(*args, **kwargs)

    def form_invalid(self, form):
        print 'in form invalid'
        post_form = PostForm(self.request.POST, error_class=DivErrorList)
        return super(CreatePostView, self).form_invalid(post_form)

    def form_valid(self, post_form):
        """
        This method is called when valid form data has been POSTed.
        It should return an HttpResponse.
        """
        print 'in form valid'
        obj = post_form.save(commit=False)
        obj.uid = self.request.user
        obj.save()
        print 'user id: ' + str(obj.uid)
        # post_form.instance.uid = self.request.user
        # print 'user id: ' + str(post_form.instance.uid)
        # post_form.save()
        return super(CreatePostView, self).form_valid(post_form)


