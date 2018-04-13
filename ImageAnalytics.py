from PIL import Image
import requests
from io import BytesIO

from .helpers.DataManager import DataManager
from .helpers.ImageHelper import prepare_for_bn_classif
from .BeautyClassificator import BeautyClassificator


class ImageAnalytics:
    def __init__(self):
        self.dm = DataManager()
        self.bc = BeautyClassificator(self.dm.bn_model)

    def beauty_score(self, img: Image):
        """
        Gives image a score according to its beauty. Higher score corresponds to more beautiful images.
        :param img: Image
        :return: score in range [0,1]
        """
        beautiful, prob = self.bc.is_beautiful(prepare_for_bn_classif(img))
        return int(beautiful) * prob
    
    def beauty_score_url(self, photo_link):
        return self.beauty_score(self._load_photo(photo_link))
    
    def _load_photo(self, photo_link):
        response = requests.get(photo_link)
        return Image.open(BytesIO(response.content))
        
    