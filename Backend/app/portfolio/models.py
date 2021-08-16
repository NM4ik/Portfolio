from django.db import models


# Create your models here.

class Person(models.Model):
    """Site owner"""

    title = models.CharField(max_length=100, verbose_name="title on main page")
    github = models.CharField(max_length=50, verbose_name="github leftbar link")
    telegram = models.CharField(max_length=50, verbose_name="github leftbar link")
    vkontakte = models.CharField(max_length=50, verbose_name="github leftbar link")
    instagram = models.CharField(max_length=50, verbose_name="github leftbar link")
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Work(models.Model):
    """Work Cards"""

    slug = models.SlugField()
    title = models.CharField(max_length=20, verbose_name="bold card title")
    subtitle = models.CharField(max_length=50, verbose_name="light card subtitle")
    backside_subtitle = models.CharField(max_length=100, verbose_name="light card-backside subtitle")
    backside_stack = models.CharField(max_length=50, verbose_name="light card-backside stack")
    github_link = models.CharField(max_length=100, verbose_name="github link")
    direct_link = models.CharField(max_length=100, verbose_name="direct link")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Work Card"
        verbose_name_plural = "Work Cards"


class Skill(models.Model):
    """Skill direction"""

    skill_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Technology(models.Model):
    """Technology direction"""

    name = models.CharField(max_length=30, verbose_name="short name of technology", default="techName")
    description = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True, related_name='Skill_id_fk',
                           verbose_name='Skill')

    def __str__(self):
        return self.name
