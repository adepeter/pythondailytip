from django.contrib import adminfrom ..models import PythonTipTweetUser@admin.register(PythonTipTweetUser)class PythonTipTweetUserAdmin(admin.ModelAdmin):    readonly_fields = [        'user_id'    ]    list_display = [        'username',        'display_name',        'user_id',    ]__all__ = [    'PythonTipTweetUserAdmin']