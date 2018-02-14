from django.db import models
from django.contrib.auth.models import User
import hashlib


class Archer(models.Model):
    content = models.CharField(max_length=160)
    user = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            )
    creation_date = models.DateTimeField(auto_now=True, blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                )
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

    def gravatar_url(self):
        return "https://gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email).hexidigest()


User.profile =property(lambda u: UserProfile.objets.get_or_create(user=u)[0])
