from inspect import isclass
from django.conf import settings
from django.utils.importlib import import_module
from django.core.exceptions import ImproperlyConfigured

from tastypie.resources import Resource, ModelResource

from tastypie.api import Api

RESOURCE_MODULES = getattr(settings, 'REDACTION_RESOURCE_MODULES', ())


class RedactionApi(Api):

    def collect_resources(self):

        resource_mods = []

        # get resources from installed apps first
        for app in settings.INSTALLED_APPS:
            try:
                mod = import_module('%s.api_resources' % app)
                resource_mods.append(mod)
            except ImportError:
                pass

        # get resources from user defined modules
        for module in RESOURCE_MODULES:
            try:
                mod = import_module(module)
                resource_mods.append(mod)
            except ImportError, e:
                raise ImproperlyConfigured(
                    'Error importing resource module %s,'
                    'check REDACTION_RESOURCE_MODULES '
                    'in your settings: "%s"' % (module, e))

        # register resources
        # FIXME: developer wants to define which resources are to be registered!
        for module in resource_mods:
            for attr in module.__dict__:

                resource = getattr(module, attr)
                if isclass(resource) and issubclass(resource, Resource) \
                                            and not resource == ModelResource:
                    self.register(resource())
