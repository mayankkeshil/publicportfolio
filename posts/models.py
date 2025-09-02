from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField # type: ignore #
from django.core.exceptions import ValidationError
from django.utils.text import slugify

class Post(models.Model): # The class post inherits features from the Model class from models module
    title = models.CharField(max_length=200) # Creates title column in database table
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Creates "author_id" column, its intelligent to add "_id" alone and links it to User. For example if User_id 1 creates a post, author_id 1 and user_id 1 are linked so now we know the user's full info. Second parameter means when user of the post is deleted, all posts from that user are deleted.
    created_at = models.DateTimeField(auto_now_add=True) # Creates created_at column, no _id as it is a normal field. "auto_now_add = True" means turn on the feature of automatically adding current time & date when object is created. "add" once at creation
    edited_at = models.DateTimeField(auto_now=True) # Every time the object is saved, update the field to current date & time
    featured_image = models.ImageField(upload_to='posts/', blank=True, null=True) # Creates featured_image column, uploads the image to "/posts/" on the website, "blank=True" means a picture is optional, "null=True" allows the database to store the field as null if there is no picture
    alt_text = models.CharField(max_length=30, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=False, null=False)
    
    def __str__(self): 
        return self.title # Allows us to identify an object more easily using its title rather than <Post object "1" etc
    
    def save(self, *args, **kwargs): # Creates gaps in between link words through slug function
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug=f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)