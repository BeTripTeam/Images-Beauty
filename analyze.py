from .ImageAnalytics import ImageAnalytics
from .helpers.ImageHelper import open_img


ia = ImageAnalytics()
im = open_img("../../instagram/1/1/1.jpg")
score = ia.beauty_score(im)
print(score)
