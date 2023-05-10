from django.db import models
from account.models import User
from django.shortcuts import reverse
from django.utils.html import format_html
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount


class Category(models.Model):
    title = models.CharField(verbose_name='عنوان', max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created", ]
        verbose_name = "دست بندی"
        verbose_name_plural = "دست بندی ها"

    def __str__(self):
        return self.title


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos', verbose_name='اسم', default=True)
    body = models.TextField(verbose_name='متن')
    slug = models.SlugField(unique=True, null=True, blank=True, allow_unicode=True, verbose_name="عنوان")
    about_video = models.TextField(verbose_name="درباره فیلم")
    video = models.FileField(upload_to="video/", verbose_name='ویدیو')
    image = models.ImageField(upload_to="image/", verbose_name='عکس')
    hit_count = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic')
    category = models.ManyToManyField(Category, related_name='categorise', verbose_name='دسته بندی ها')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان')
    time = models.TimeField(auto_now_add=True, verbose_name="ساعت")
    status = models.BooleanField(null=True, blank=True, verbose_name="وضیعت")

    class Meta:
        ordering = ["-created", ]
        verbose_name = "ویدیو ها"
        verbose_name_plural = "ویدیو"

    def __str__(self):
        return f'{self.time} - {self.status}'

    def shoe_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" height="50px" width="60px">')
        return format_html('<h3 style="color: red">تصویر موجود نیست</h3>')

    shoe_image.short_description = "عکس بند انگشتی"

    def get_absolute_url(self):
        return reverse("account:panel_user")


class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="parents")
    body = models.TextField()
    comment_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"

    def __str__(self):
        return f"{self.user.username} - {self.body[:10]}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes", verbose_name="لایک")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="likes", verbose_name="لایک کاربر")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "لیک"
        verbose_name_plural = "لایک ها"
        ordering = ("created_at",)

    def __str__(self):
        return f'{self.user.username} - {self.video.slug}'


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notification", verbose_name="نام کاربری",
                             default=True)
    body = models.TextField(verbose_name="متن اعلان")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    is_admin = models.BooleanField(default=True)
    active = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="notification", null=True, blank=True,
                               verbose_name="فعال هست یا خیر", default=True)

    class Meta:
        ordering = ("-active",)
        verbose_name = "اطلاع رسانی"
        verbose_name_plural = "اطلاع رسانی ها"

    def get_absulot_url(self):
        return reverse("account:panel_user")

    def __str__(self):
        return f'{self.is_admin} - {self.active}'
