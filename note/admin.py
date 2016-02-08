from django.contrib import admin
from .models import Post, Contact


class PostAdmin(admin.ModelAdmin):

    def was_published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=1)
        was_published_recently.admin_order_field = 'published_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'

    list_display = ('id', 'author', 'title', 'postcategory', 'created_date',)
    list_filter = ['published_date']
    search_fields = ['title']


class ContactAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'email', 'subject', 'message')
    search_filter = ['name']



admin.site.register(Post, PostAdmin, )
admin.site.register(Contact, ContactAdmin)

