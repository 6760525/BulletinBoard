from django.db import models
from datetime import datetime
from BulletinBoard.settings import AUTH_USER_MODEL
from django.urls import reverse


class Author(models.Model):
    name = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True, verbose_name='Автор')

    def __str__(self):
        return self.name.username

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Category(models.Model):
    tanks = 'tanks'
    hills = 'hills'
    dd = 'dd'
    Merchants = 'merchants'
    Guildmasters = 'guildmasters'
    Questgivers = 'questgivers'
    Blacksmiths = 'blacksmiths'
    Tanners = 'tanners'
    Zelievars = 'zelievars'
    SpellMasters = 'spellmasters'
    Categories = [(tanks, 'tanks'),
                  (hills, 'hills'),
                  (dd, 'dd'),
                  (Merchants, 'merchants'),
                  (Guildmasters, 'guildmasters'),
                  (Questgivers, 'questgivers'),
                  (Blacksmiths, 'blacksmiths'),
                  (Tanners, 'tanners'),
                  (Zelievars, 'zelievars'),
                  (SpellMasters, 'spellmasters')]

    name = models.CharField("Category", max_length=25, choices=Categories, default=tanks, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Declaration(models.Model):
    """Обявления"""
    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name='User', on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=50)
    text = models.TextField('Description')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    response = models.ManyToManyField(AUTH_USER_MODEL, related_name='post_response', )
    accepted_response = models.ManyToManyField(AUTH_USER_MODEL, related_name='post_accepted_response', )

    file = models.FileField('File', upload_to="bulletin_file/", blank=True, null=True)
    image = models.ImageField('Image', upload_to="image/", blank=True, null=True)

    def get_absolute_url(self):
        return reverse('DeclarationDetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    # def get_absolute_url(self):

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Reviews(models.Model):
    declaration = models.ForeignKey(Declaration, verbose_name='comment', related_name='review_declaration',
                                    on_delete=models.CASCADE, null=True)
    commentator = models.ForeignKey(AUTH_USER_MODEL, verbose_name='commenter', on_delete=models.CASCADE)
    review = models.TextField('Comment', max_length=3000)
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review

    def get_absolute_url(self):
        return f'/'

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"