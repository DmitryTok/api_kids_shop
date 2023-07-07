from abc import ABC, abstractmethod

from django.db import models


class BaseRepository(ABC):

    @property
    @abstractmethod
    def model(self) -> models.Model:
        pass

    def get_all_objects_order_by_id(self):
        return self.model.objects.all().order_by('id')
