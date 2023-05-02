from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, View
from django.core.paginator import Paginator
from videos.models import Video, Comment, Like, Notification
from hitcount.views import HitCountDetailView

# Home
class Home(ListView):
    model = Video
    ordering = ['-user', ]
    paginate_by = 6
    template_name = "home/home.html"

# list video and paginate
def VideoList(request):
    videos = Video.objects.all()
    page_number = request.GET.get("page")
    paginate = Paginator(videos, 6)
    object = paginate.get_page(page_number)
    context = {'object_list': object}
    return render(request, "home/video-list.html", context)

# view count
class HitCount(HitCountDetailView):
    model = Video
    template_name = 'home/video-detail.html'
    context_object_name = 'video'
    slug_field = 'slug'
    count_hit = True

# search
def Search(request):
    q = request.GET.get("q")
    videos = Video.objects.filter(slug__icontains=q)
    page_number = request.GET.get("page")
    paginate = Paginator(videos, 2)
    object = paginate.get_page(page_number)
    context = {'object_list': object}
    return render(request, "home/video-list.html", context)


# system like and view and comment
def VideoDetail(request, pk, slug):
    video = get_object_or_404(Video, id=pk, slug=slug)

    if request.method == "POST":
        parent_id = request.POST.get("parent_id")
        body = request.POST.get('body')
        Comment.objects.create(body=body, video=video, user=request.user, parent=parent_id)

    context = {'video': video}

    if request.user.is_authenticated:
        if request.user.likes.filter(video_id=pk, user_id=request.user.id).exists():
            context['is_liked'] = True
        else:
            context['is_liked'] = False
    else:
        return redirect('account:register_login')

    return render(request, 'home/video-detail.html', context)


# system like
def likeDetail(request, id, pk):
    if request.user.is_authenticated:
        try:
            like = Like.objects.get(video__id=id, user_id=request.user.id)
            like.delete()
        except:
            Like.objects.create(video_id=pk, user_id=request.user.id)
        return redirect('home:video_all')

    return redirect("account:register_login")

# Notification users
class NotificationView(View):
    def get(self, pk):
        notification = Notification.objects.get(id=pk)
        urls = notification.active.get_absulot_url()
        notification.delete()
        return redirect(urls)
