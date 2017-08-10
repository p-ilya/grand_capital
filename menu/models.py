from django.db import models

# Create your models here.


class MenuNode(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True)
    level = models.IntegerField(blank=True)
    belongs_to = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.parent:
            self.level = self.parent.level + 1
        else:
            self.level = 0
        super(MenuNode, self).save(*args, **kwargs)

    def find_child_nodes(self):
        return MenuNode.objects.filter(parent=self.id)

    children = property(find_child_nodes)
