from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from django.db.models.signals import post_save
# Create your models here.

class UserProfileManager(models.Manager):
    use_for_related_fields = True
    def all(self):
        qs = self.get_queryset().all()
        try:
            if self.instance:
                qs = qs.exclude(user=self.instance)
        except:
            pass
        return qs
    def toggle_follow(self, user, to_toggle_user):
        user_profile, created  = UserProfile.objects.get_or_create(user=user)
        if to_toggle_user in user_profile.following.all():
            user_profile.following.remove(to_toggle_user)
            added = False
        else:
            user_profile.following.add(to_toggle_user)
            added = True
        return added
        
    def is_following(self, user, followed_by_user):
        user_profile, created  = UserProfile.objects.get_or_create(user=user)
        if created: 
            return False
        if followed_by_user in user_profile.following.all():
            return True

        return False

    def recommended(self, user, limit_to=10):
        profile = user.profile
        following = profile.following.all()
        following = profile.get_following()
        qs = self.get_queryset().exclude(user__in=following).exclude(id=profile.id).order_by("?")[:limit_to]
        return qs

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')

    objects = UserProfileManager()
    def __str__(self):
        return str(self.following.all().count())

    def get_following(self):
        users = self.following.all()
        return users.exclude(username=self.user.username)

    def get_follow_url(self):
        return reverse_lazy("profiles:follow", kwargs={"username":self.user.username})

    def get_absolute_url(self):
        return reverse_lazy("profiles:detail", kwargs={"username":self.user.username})


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        new_profike = UserProfile.objects.get_or_create(user=instance)
    print(instance)


post_save.connect(post_save_user_receiver, sender=settings.AUTH_USER_MODEL)