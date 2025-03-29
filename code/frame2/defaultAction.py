from PIL import Image

class Rescale:
    fields:list = {"scale":{"default_value":1, "value":0, "hint":"rescale value"}}
    
    def __init__(self):
        ...
    def forward(self, image:Image.Image, scale) -> Image.Image:
        return 
    
    def __call__(self, *args, **kwds):
        self.forward