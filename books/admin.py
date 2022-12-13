from django.contrib import admin

from .models import Book, Edition, Testimonial

class EditionInline(admin.StackedInline):
    model = Edition
    extra = 0   # here extra: 0 means initially there will be no form for child model
    fields = ['publisher', 'year', 'pages'] # specifying fields to show in the inline form

class TestimonialInline(admin.StackedInline):
    model = Testimonial
    extra = 0


class BookAdmin(admin.ModelAdmin):
    inlines = [EditionInline, TestimonialInline] # list of inlines to show along with book form
    list_display = ['title', 'author','user'] # list of columns to display in list of books page
    readonly_fields = ['created_at', 'updated_at'] # these fields cannot be changed in the form
    raw_id_fields = ['user'] # search a user from list of users

admin.site.register(Book, BookAdmin)
