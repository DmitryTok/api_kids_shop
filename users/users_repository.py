from kids_shop.base.base_repository import BaseRepository
from users import models


class ProfileRepository(BaseRepository):

    @property
    def model(self) -> type[models.Profile]:
        return models.Profile

    def get_all_objects_order_by_id(self):
        return self.model.objects.select_related(
            'user',
            'address',
        ).prefetch_related('kids')
