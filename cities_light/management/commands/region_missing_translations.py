from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        from cities_light.models import Region
        for item in Region.published.all():
            if not item.translations.all():
                obj = item.translate(item.default_language)
                obj.name = "no region name given"
                obj.display_name = "no region name given"
                print(f"Region id {item.id}")
                obj.save()
