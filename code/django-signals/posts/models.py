from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# signals imports
from django.dispatch import receiver
from django.db.models.signals import (
    pre_save,
    post_save,
    pre_delete,
    post_delete,
    m2m_changed,
)

User = settings.AUTH_USER_MODEL



@receiver(pre_save, sender=User)
def user_pre_save_receiver(sender, instance, *args, **kwargs):
    """
    before saved in the database
    """
    print(instance.username, instance.id) # None
    # trigger pre_save
    # DONT DO THIS -> instance.save()
    # trigger post_save

# pre_save.connect(user_created_handler, sender=User)


@receiver(post_save, sender=User)
def user_post_save_receiver(sender, instance, created, *args, **kwargs):
    """
    after saved in the database
    """
    if created:
        print("Send email to", instance.username)
        # trigger pre_save
        # instance.save()
        # trigger post_save
    else:
        print(instance.username, "was just saved")

# post_save.connect(user_created_handler, sender=User)









class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    liked = models.ManyToManyField(User, blank=True)
    notify_users = models.BooleanField(default=False)
    notify_users_timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    active = models.BooleanField(default=True)


@receiver(pre_save, sender=BlogPost)
def blog_post_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

@receiver(post_save, sender=BlogPost)
def blog_post_post_save(sender, instance, created, *args, **kwargs):
    if instance.notify_users:
        print("notify users")
        instance.notify_users = False
        # celery worker task -> offload -> Time & Tasks 2 cfe.sh
        instance.notify_users_timestamp = timezone.now()
        instance.save()


@receiver(pre_delete, sender=BlogPost)
def blog_post_pre_delete(sender, instance, *args, **kwargs):
    # move or make a backup of this data
    print(f"{instance.id} will be removed")

# pre_delete.connect(blog_post_pre_delete, sender=BlogPost)


@receiver(post_delete, sender=BlogPost)
def blog_post_post_delete(sender, instance, *args, **kwargs):
    #  celery worker task -> offload -> Time & Tasks 2 cfe.sh
    print(f"{instance.id} has removed")


# post_delete.connect(blog_post_post_delete, sender=BlogPost)


@receiver(m2m_changed, sender=BlogPost.liked.through)
def blog_post_liked_changed(sender, instance, action, *args, **kwargs):
    # print(args, kwargs)
    # print(action)
    if action == 'pre_add':
        print("was added")
        qs = kwargs.get("model").objects.filter(pk__in=kwargs.get('pk_set'))
        print(qs.count())
