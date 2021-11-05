from django.contrib import admin
from .models import Post, Category, Tag
from django.db import models
from django import forms
from blogproject.settings import TXT_PATH
import pypinyin
import mdeditor
from mdeditor import widgets

def py(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s

class PostForm(forms.ModelForm):
    #content  = forms.CharField(widget=forms.Textarea,initial='12')#initial=open(TXT_PATH + '/' + Post.url_path,'r').read())
    content = forms.CharField(widget=mdeditor.widgets.MDEditorWidget,)
    class Meta:
        model = Post
        exclude = ['url_path']
    #def content(self):
    #    return self.cleaned_data['content']

    def __init__(self, *args, **kwargs):
        self.content = kwargs.pop('content',None)
        super().__init__(*args, **kwargs)
        #self.fields['content'].initial = 125


class PostAdmin(admin.ModelAdmin):
    #exclude = ('url_path',)
    form = PostForm
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author','content',]

    #def initial_value(self,db_field,**kwargs):
    #    field = super(PostAdmin,self).formfield_for_dbfield(db_field,**kwargs)
    #    if db_field.name == 'content':
    #        field.initial = '123'
    #    return field

    #def get_changeform_initial_data(self, request):
    #    return {'content': 'custom_initial_value'}

    #def get_form(self, request, obj=None, change=False, **kwargs):
        #if obj:
        #    obj.content = '123'
        #obj.content = open(TXT_PATH+'/'+obj.url_path).read()
        #return super().get_form(request, obj, change, **kwargs)


    def change_view(self, request, object_id, form_url='', extra_context=None):
        #self.fields = ['title', 'created_time', 'modified_time', 'category', 'author','content',]
        obj = Post.objects.get(pk=object_id)
        #self.form()['content'].prepare_value('123')
        #content = open(TXT_PATH + '/' + obj.url_path).read()
        content = obj.content
        #self.form().fields['content'] = '123'
        #extra_context = {'content':'123'}
        #return super(PostAdmin,self).change_view(
        #    request, object_id, form_url, extra_context=extra_context,
        #)
        ret = super().change_view(request, object_id, form_url, extra_context=extra_context,)
        form =  ret.context_data['adminform'].form
        form.fields['content'].initial = content
        return ret

    #def get_fields(self,request,obj):
    #    if obj is None:
    #        content = '123'
    #        return [content]
    #    else:
    #        content = '124'
    #        return [content]


    def save_model(self, request, obj, form, change):
        fd = open(TXT_PATH + '/' + obj.url_path,'w')
        fd.write(form.cleaned_data['content'])
        fd.close()
        super(PostAdmin, self).save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
