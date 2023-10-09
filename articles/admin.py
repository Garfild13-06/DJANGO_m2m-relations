from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить

            if len(form.cleaned_data) > 0:
                if form.cleaned_data["is_main"] == True:
                    main_count += 1
                    if main_count > 1:
                        raise ValidationError('Главным может быть только один Тэг')
            # form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
    extra = 3


@admin.register(Article)
class Article_Admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ScopeInline]


@admin.register(Tag)
class Tag_Admin(admin.ModelAdmin):
    list_display = ['id', 'name']
    # list_display = ['id']
