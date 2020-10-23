from basic_transforms import *

class TrainAugmentation():
    def __init__(self, image_size, mean_val=0, std_val=1.0):
        #TODO: add self.augment, which contains
        # random scale, pad, random crop, random flip, convert data type, and normalize ops
        self.augment = Compose([RandomScale(), Pad(size=5), RandomCrop(crop_size=image_size), RandomFlip(), ConvertDataType(), Normalize(mean_val=0, std_val=1.0)])

    def __call__(self, image, label):
        return self.augment(image, label)


class InferAugmentation():
    def __init__(self, mean_val=0, std_val=1.0):
        self.augment = Compose([ConvertDataType(), Normalize(mean_val=0, std_val=1.0)])

    def __call__(self, image, label):
        return self.augment(image, label)