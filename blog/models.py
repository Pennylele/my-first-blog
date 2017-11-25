from django.db import models
from django.utils import timezone

#Post is the name of the model. Always start a class name with an uppercase letter.
#models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.
class Post(models.Model): 
    author = models.ForeignKey('auth.User') # This is a link to another model.
    title = models.CharField(max_length=200) # This is how we define text with a limited number of chars.
    text = models.TextField() # This is for long text without a limit, like blog content.
    created_date = models.DateTimeField( # This is date and time
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # when we call the __str__ method, we will get a text(string) with a Post title
        return self.title
