from django.utils.text import slugify
import uuid

def generate_slug(title:str) -> str:
    from .models import Recipe
    base_slug = slugify(title)

    while Recipe.objects.filter(slug=base_slug).exists():
        base_slug = base_slug + '-' + str(uuid.uuid4())[0:4]
    return base_slug