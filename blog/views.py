from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from users.models import Follow, Profile
import sys
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from .forms import NewCommentForm
from django.http import HttpResponse, HttpResponseNotFound
import googlemaps
import json

def is_users(post_user, logged_user):
    return post_user == logged_user

def selectproblem(request):
    return render(request, 'blog/post_selectproblem.html', {})

# def about(request):
#     return render(request, 'blog/about.html', {})

PAGINATION_COUNT = 5


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = PAGINATION_COUNT

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        all_users = []
        data_counter = Post.objects.values('author')\
            .annotate(author_count=Count('author'))\
            .order_by('-author_count')[:5]

        for aux in data_counter:
            all_users.append(User.objects.filter(pk=aux['author']).first())

        data['all_users'] = all_users
        print(all_users, file=sys.stderr)
        return data

    # def get_queryset(self):
    #     user = self.request.user
    #     qs = Follow.objects.filter(user=user)
    #     follows = [user]
    #     for obj in qs:
    #         follows.append(obj.follow_user)
    #     return Post.objects.filter(author__in=follows).order_by('-date_posted')


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = PAGINATION_COUNT

    def visible_user(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        visible_user = self.visible_user()
        logged_user = self.request.user
        print(logged_user.username == '', file=sys.stderr)

        if logged_user.username == '' or logged_user is None:
            can_follow = False
        else:
            can_follow = (Follow.objects.filter(user=logged_user,
                                                follow_user=visible_user).count() == 0)
        data = super().get_context_data(**kwargs)

        data['user_profile'] = visible_user
        data['can_follow'] = can_follow
        return data

    def get_queryset(self):
        user = self.visible_user()
        return Post.objects.filter(author=user).order_by('-date_posted')

    def post(self, request, *args, **kwargs):
        if request.user.id is not None:
            follows_between = Follow.objects.filter(user=request.user,
                                                    follow_user=self.visible_user())

            if 'follow' in request.POST:
                    new_relation = Follow(user=request.user, follow_user=self.visible_user())
                    if follows_between.count() == 0:
                        new_relation.save()
            elif 'unfollow' in request.POST:
                    if follows_between.count() > 0:
                        follows_between.delete()

        return self.get(self, request, *args, **kwargs)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        comments_connected = Comment.objects.filter(post_connected=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected
        data['form'] = NewCommentForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(content=request.POST.get('content'),
                              author=self.request.user,
                              post_connected=self.get_object())
        new_comment.save()

        return self.get(self, request, *args, **kwargs)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'
    success_url = '/'

    def test_func(self):
        return is_users(self.get_object().author, self.request.user)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['catogery', 'content', 'street', 'city', 'state', 'zipcode', 'image', 'number_plate', 'model', 'make', 'color']
    template_name = 'blog/post_new.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tag_line'] = 'Report A New Issue'
        return data

    # def geocoding(self):
    #     gmaps = googlemaps.Client(key='AIzaSyCxEBXXZRjgKUczgQfr7LMGxWFZtgxZ5LQ')
    #
    #     # Geocoding an address
    #     geocode_result = gmaps.geocode('1261 SW 104th Passage, Miami, Florida 33174')
    #     print(geocode_result[0]['geometry']['location']['lat'])
    #     print(geocode_result[0]['geometry']['location']['lng'])
    #
    #     # Look up an address with reverse geocoding
    #     reverse_geocode_result = gmaps.reverse_geocode((25.7570684, -80.3658604))
    #     print(reverse_geocode_result[0]['address_components'][0]['long_name'] + ' ' +
    #           reverse_geocode_result[0]['address_components'][1]['long_name'] + ' ' +
    #           reverse_geocode_result[0]['address_components'][3]['long_name'])  # Street
    #     print(reverse_geocode_result[0]['address_components'][2]['long_name'])  # city
    #     print(reverse_geocode_result[0]['address_components'][4]['long_name'])  # State
    #     # print(reverse_geocode_result[0]['address_components'][5]['long_name']) #Country
    #     print(reverse_geocode_result[0]['address_components'][6]['long_name'])  # zipcode


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['catogery', 'content', 'street', 'city', 'state', 'zipcode', 'image', 'number_plate', 'model', 'make', 'color']
    template_name = 'blog/post_new.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return is_users(self.get_object().author, self.request.user)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tag_line'] = 'Edit a post'
        return data


class FollowsListView(ListView):
    model = Follow
    template_name = 'blog/follow.html'
    context_object_name = 'follows'

    def visible_user(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_queryset(self):
        user = self.visible_user()
        return Follow.objects.filter(user=user).order_by('-date')

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['follow'] = 'follows'
        return data


class FollowersListView(ListView):
    model = Follow
    template_name = 'blog/follow.html'
    context_object_name = 'follows'

    def visible_user(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_queryset(self):
        user = self.visible_user()
        return Follow.objects.filter(follow_user=user).order_by('-date')

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['follow'] = 'followers'
        return data


# class StatusPostListView(LoginRequiredMixin, ListView):
#     model = Post
#     template_name = 'blog/home.html'
#     context_object_name = 'status'
#     ordering = ['-date_posted']
#     paginate_by = PAGINATION_COUNT
#
#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#
#         all_users = []
#         data_counter = Post.objects.values('author')\
#             .annotate(author_count=Count('author'))\
#             .order_by('-author_count')[:5]
#
#         for aux in data_counter:
#             all_users.append(User.objects.filter(pk=aux['author']).first())
#
#         data['all_users'] = all_users
#         print(all_users, file=sys.stderr)
#         return data
#
#     def get_queryset(self):
#         user = self.request.user
#         qs = Follow.objects.filter(user=user)
#         follows = [user]
#         for obj in qs:
#             follows.append(obj.follow_user)
#         return Post.objects.filter(author__in=follows).order_by('-date_posted')


def my_view(request):
        x = request.GET.get('x','26.07081081728195')
        y = request.GET.get('y','-80.29719584921872')

        gmaps = googlemaps.Client(key='AIzaSyCxEBXXZRjgKUczgQfr7LMGxWFZtgxZ5LQ')
        # Geocoding an address
        geocode_result = gmaps.geocode('1261 SW 104th Passage, Miami, Florida 33174')
        print(geocode_result[0]['geometry']['location']['lat'])
        print(geocode_result[0]['geometry']['location']['lng'])

        # Look up an address with reverse geocoding
        reverse_geocode_result = gmaps.reverse_geocode((x, y))
        print(reverse_geocode_result[0]['address_components'][0]['long_name'] + ' ' +
              reverse_geocode_result[0]['address_components'][1]['long_name'] + ' ' +
              reverse_geocode_result[0]['address_components'][3]['long_name'])  # Street
        print(reverse_geocode_result[0]['address_components'][2]['long_name'])  # city
        print(reverse_geocode_result[0]['address_components'][4]['long_name'])  # State
        # print(reverse_geocode_result[0]['address_components'][5]['long_name']) #Country
        print(reverse_geocode_result[0]['address_components'][6]['long_name'])  # zipcode
        totalAddress = reverse_geocode_result[0]['address_components'][0]['long_name'] + ' ' +\
                        reverse_geocode_result[0]['address_components'][1]['long_name'] + ' ' +\
        reverse_geocode_result[0]['address_components'][3]['long_name']+ ' '+\
                        reverse_geocode_result[0]['address_components'][2]['long_name'] +' '+\
        reverse_geocode_result[0]['address_components'][4]['long_name']+' '+\
        reverse_geocode_result[0]['address_components'][6]['long_name']

        data = {}
        data['address1'] = reverse_geocode_result[0]['address_components'][0]['long_name']
        data['address2'] = reverse_geocode_result[0]['address_components'][1]['long_name']
        data['street'] = reverse_geocode_result[0]['address_components'][3]['long_name']
        data['city'] = reverse_geocode_result[0]['address_components'][2]['long_name']
        data['state'] = reverse_geocode_result[0]['address_components'][4]['long_name']
        data['country'] = reverse_geocode_result[0]['address_components'][5]['long_name']
        data['zipcode'] = reverse_geocode_result[0]['address_components'][6]['long_name']




        return HttpResponse(json.dumps(data))