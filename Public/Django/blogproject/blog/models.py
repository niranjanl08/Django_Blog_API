from django.db import models
class Post(models.Model):
    title_blog = models.CharField(max_length=255)
    content_of_blog= models.TextField()
    author_of_blog = models.CharField(max_length=100)
    created_dateandtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_blog


class Comment(models.Model):
    post_name = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name_of_person = models.CharField(max_length=100)
    email_id = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name_of_person}"