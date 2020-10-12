from django.utils.text import slugify

def unique_slue_generator(model_instance, title, slug_field):

    slug = slugify(title)
    model_class = model_instance.__class__

    while model_class.default_manager.filter(slug=slug).exists():
        objects_pk = model_class.default_manager.latest('pk')
        object_pk = object_pk.pk + 1

        slug = f'{slug}-{object_pk}'

    return slug