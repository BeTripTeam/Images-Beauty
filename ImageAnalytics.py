from PIL import Image

from .helpers.DataManager import DataManager
from .helpers.ImageHelper import prepare_for_bn_classif
from .BeautyClassificator import BeautyClassificator


class ImageAnalytics:
    def __init__(self):
        self.dm = DataManager()
        self.bc = BeautyClassificator(self.dm.bn_model)

    def get_beauty_score(self, img: Image):
        """
        Gives image a score according to its beauty. Higher score corresponds to more beautiful images.
        :param img: Image
        :return: score in range [0,1]
        """
        beautiful, prob = self.bc.is_beautiful(prepare_for_bn_classif(img))
        return int(beautiful) * prob