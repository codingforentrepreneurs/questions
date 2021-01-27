from django.contrib.auth import get_user_model

User = get_user_model()

# pre_save -> instance  -> my_handler
instance = User.objects.create() # save User data in the database
# post_save -> instance, created=True -> my_handler

# pre_save -> instance  -> my_handler
instance.save()
# post_save -> instance, created=False  -> my_handler

# pre_delete -> instance  -> my_handler
instance.delete()
# post_delete -> instance  -> my_handler