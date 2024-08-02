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
    
    def get_obj(self, profile_id):
        return self.model.objects.get(id=profile_id)


class UserRepository(BaseRepository):
    @property
    def model(self) -> type[models.CustomUser]:
        return models.CustomUser
    
    def get_user_obj(self, user_id):
        return self.model.objects.get(id=user_id)


class AddressRepository(BaseRepository):
    @property
    def model(self) -> type[models.Address]:
        return models.Address

    def get_obj(self, address_id):
        return self.model.objects.get(id=address_id)
