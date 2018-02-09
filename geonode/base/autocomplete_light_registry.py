import autocomplete_light

from taggit.models import Tag
from models import ResourceBase, Region
from guardian.shortcuts import get_objects_for_user


class ResourceBaseAutocomplete(autocomplete_light.AutocompleteModelBase):
    model = ResourceBase

    def choices_for_request(self):
        permitted = get_objects_for_user(
            self.request.user,
            'base.view_resourcebase')
        self.choices = self.choices.filter(id__in=permitted)
        return super(ResourceBaseAutocomplete, self).choices_for_request()


autocomplete_light.register(Region,
                            search_fields=['name'],
                            autocomplete_js_attributes={'placeholder': 'Region/Country ..', },)

autocomplete_light.register(ResourceBase,
                            ResourceBaseAutocomplete,
                            search_fields=['title'],
                            order_by=['title'],
                            limit_choices=100,
                            autocomplete_js_attributes={'placeholder': 'Resource name..', },)

autocomplete_light.register(Tag,
                            search_fields=['name', 'slug'],
                            autocomplete_js_attributes={'placeholder':
                                                        'A space or comma-separated list of keywords', },)
