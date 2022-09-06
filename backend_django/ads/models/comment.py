from django.db import models

from .ad import Ad


class Comment(models.Model):
    text = models.TextField(blank=True, max_length=4000)
    created_at = models.DateField(auto_now_add=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.title
