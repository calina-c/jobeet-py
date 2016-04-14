from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class Job(models.Model):
    ttype = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    how_to_apply = models.TextField()
    token = models.CharField(max_length=255, unique=True)
    is_public = models.NullBooleanField(null=True)
    is_activated = models.NullBooleanField(null=True)
    email = models.CharField(max_length=255)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='jobs')


class Affiliate(models.Model):
    url = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class CategoryAffiliate(models.Model):
    category = models.ForeignKey(Category, related_name='category_affiliates')
    affiliate = models.ForeignKey(
        Affiliate,
        related_name='category_affiliates'
    )
