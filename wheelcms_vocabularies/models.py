from wheelcms_axle.models import Configuration as BaseConfiguration
from wheelcms_axle.configuration import BaseConfigurationHandler

from wheelcms_axle.registries.configuration import configuration_registry
from django.db import models
from django import forms

class Vocabulary(models.Model):
    key = models.CharField(max_length=60, blank=False)
    raw = models.TextField(default="[]", blank=False)

class Configuration(models.Model):
    main = models.ForeignKey(BaseConfiguration, related_name="vocabularies")
    vocabs = models.ManyToManyField(Vocabulary, related_name="configuration")

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
#configuration_registry.register("vocabularies", "Vocabularies", Configuration, ConfigurationForm)
configuration_registry.register(ConfigurationHandler)

