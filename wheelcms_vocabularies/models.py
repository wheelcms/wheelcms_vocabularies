from django.core.urlresolvers import reverse

from wheelcms_axle.models import Configuration as BaseConfiguration
from wheelcms_axle.configuration import BaseConfigurationHandler

from wheelcms_axle.registries.configuration import configuration_registry
from django.db import models
from django import forms


class Configuration(models.Model):
    main = models.ForeignKey(BaseConfiguration, related_name="vocabularies")

class Vocabulary(models.Model):
    conf = models.ForeignKey(Configuration, related_name="vocabularies")
    key = models.CharField(max_length=60, blank=False)
    raw = models.TextField(default="[]", blank=False)

class ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Configuration
        exclude = ['main']

class ConfigurationHandler(BaseConfigurationHandler):
    id = "vocabularies"
    label = "Vocabularies"
    model = Configuration
    form = ConfigurationForm

    def view(self, handler):
        handler.context['tabs'] = handler.construct_tabs(self.id)
        ## set redirect_to
        return handler.template("wheelcms_vocabularies/configure_vocabularies.html")

    def process(self, handler, instance):
        handler.context['form'] = form = \
                 self.form(handler.request.POST, instance=instance)
        
        if form.is_valid():
            form.save()
            for d in handler.request.POST.getlist('delete', []):
                try:
                    Vocabulary.objects.get(key=d).delete()
                except Vocabulary.DoesNotExist:
                    pass
            for i, k in enumerate(handler.request.POST.getlist('voc.id', [])):
                v, _ = Vocabulary.objects.get_or_create(key=k, conf=instance)
                v.data = handler.request.POST.get('voc.data')[i]

            ## include hash, open tab
            return handler.redirect(reverse('wheel_config'), config=self.id, success="Changes saved")
        handler.context['tabs'] = handler.construct_tabs(self.id)
        return handler.template("wheelcms_vocabularies/configure_vocabularies.html")

#configuration_registry.register("vocabularies", "Vocabularies", Configuration, ConfigurationForm)
configuration_registry.register(ConfigurationHandler)

