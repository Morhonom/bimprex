from PIL import Image
from PIL.ImageOps import scale

class Rescale:
    fields:list = {"re_scale":{"default_value":"1", "hint":"масштаб:"}}
    def __init__(self):
        ...
    def forward(self, image:Image.Image, re_scale) -> Image.Image:
        image = scale(image, float(re_scale))
        return image
    
    def __call__(self, *args, **kwds):
        self.forward
        
class Grayscale:
    fields:list = {}
    def __init__(self):
        ...
    def forward(self, image:Image.Image) -> Image.Image:
        return image.convert('L')
    
    def __call__(self, *args, **kwds):
        self.forward
        