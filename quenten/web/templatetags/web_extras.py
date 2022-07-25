from django import template
from web.models import Accessible, Adult, Carer, Child, Person, YoungCarer

register = template.Library()


@register.simple_tag()
def get_person_type(person: Person):
    person_type = None

    if isinstance(person, Adult):
        person_type = "adult"
    elif isinstance(person, Carer):
        person_type = "carer"
    elif isinstance(person, Child):
        person_type = "child"
    elif isinstance(person, YoungCarer):
        person_type = "young carer"
    elif isinstance(person, Accessible):
        person_type = "accessible"

    return person_type
