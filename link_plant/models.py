from django.db import models

# each class is a table in our data base
# profiles, links associated with profiles

class Profile(models.Model):
    #name of profile, slug-url fiendly version of name, bg color

    BG_CHOICES = (
        ('blue','Blue'),
        ('green','Green'),
        ('yellow','Yellow')
    )

    name = models.CharField(max_length= 100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length =50, choices = BG_CHOICES)

    def __str__(self):
        return self.name


class Link(models.Model):
    # text that is displayed for the link, url, profile that it is associated with

    text = models.CharField(max_length = 100)
    url = models.URLField(max_length = 200)
    profile = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name='links')
    #when the profile is deleted, it would delete all links associated

    def __str__(self):
        return f" {self.text} | {self.url}"

# different databases to use
# many to many: many profiles would be associated with many links and vice vera
# one to one: each profile would be associated with only one link
# many to one: many links can be associated with one profile

