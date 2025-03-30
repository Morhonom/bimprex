from PIL import Image
from PIL.ImageOps import scale

class Rescale:
    fields:list = {"scale":{"default_value":"1", "value":"0", "hint":"rescale value"}}
    name:str = "Rescale"
    def __init__(self):
        ...
    def forward(self, image:Image.Image, re_scale) -> Image.Image:
        image = scale(image, float(re_scale))
        return image
    
    def __call__(self, *args, **kwds):
        self.forward