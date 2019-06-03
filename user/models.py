from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='姓名')
	realname = models.CharField(max_length=20)
	submited=models.BooleanField(default=False)

	def __stf__(self):
		return '<Profile: %s for %s>' % (self.realname, self.user.username)

	def save(self, *args, **kwargs):
		if not self.pk:
			try:
				p = Profile.objects.get(user=self.user)
				self.pk = p.pk
			except Profile.DoesNotExist:
				pass

		super(Profile, self).save(*args, **kwargs)


def create_user_profile(sender, instance, created, **kwargs):
	if created:
		profile = Profile()
		profile.user = instance
		profile.save()


post_save.connect(create_user_profile, sender=User)