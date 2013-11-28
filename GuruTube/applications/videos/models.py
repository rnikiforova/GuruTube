from django.db import models

class Tag(models.Model):
    content = models.CharField(max_length=15)
    
    def __str__(self):
        '''Returns the tag content'''
        return self.content
    
class Channel(models.Model):
    username = models.CharField(max_length=20)
    avatar = models.CharField(max_length=255)
    subscribers_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        '''Returns the channel username'''
        return self.username

class Video(models.Model):
    youtube_id = models.CharField(db_index=True, max_length=12)
    date_published = models.DateTimeField("Published on")
    date_uploaded = models.DateTimeField("Uploaded on")
    description = models.CharField(max_length=5000)
    title = models.CharField(db_index=True, max_length=100)
    channel = models.ForeignKey(Channel)
    view_count = models.PositiveIntegerField(default=0)
    like_dislike_ratio = models.FloatField(default=0)
    category = models.CharField(max_length=100)
    priority_coefficient = models.FloatField(db_index=True, default=0)
    state = models.PositiveIntegerField(choices=(
        (1, 'For review'),
        (2, 'Being reviewed'),
        (4, 'Approved'),
        (8, 'Disapproved'),
    ))
    tags = models.ManyToManyField(Tag)
    products = models.ManyToManyField('products.Product')
    
    class Meta:
        ordering = ['priority_coefficient']
    
    def __str__(self):
        '''Returns the title of the video'''
        return self.title
    
    def get_url(self):
        '''Returns the url of the video'''
        return str.join('https://www.youtube.com/watch?v=', self.youtube_id)