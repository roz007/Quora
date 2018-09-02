from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Questions

admin.site.register(Questions)
# class QuestionGroupsAdmin(admin.ModelAdmin):

#     class Meta:
#         QuestionGroups

# admin.site.register(Questions, QuestionsAdmin)
# admin.site.register(QuestionGroups, QuestionGroupsAdmin)