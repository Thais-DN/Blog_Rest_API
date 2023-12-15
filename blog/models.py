from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def user_directory_paty(instance, filename):
    return 'blog/{0}/{1}'.format(instance.title, filename)

class Post(models.Model):

    class PostObjects(models.Model):
        def get_queryset(self):
            return super().get_query() .filter(status= 'piblished')
        
    options = (

        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to=user_directory_paty, blank=True, null=True)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published', null=False, unique=True)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_user')

    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()
    postObjects = PostObjects()

    class Meta:
        ordering = ('published',)

    def __str__(self):
        return self.title

