from import_export import resources
from .models import Palestrante

class PalestranteResource(resources.ModelResource):
    class Meta:
        model = Palestrante