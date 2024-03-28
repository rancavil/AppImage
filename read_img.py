# read image using OpenCV
import cv2
import numpy as np
from abc import ABC, abstractmethod
from typing import Tuple


class Image(ABC):
    @abstractmethod
    def read_image(self)->None:
        pass
    
    @abstractmethod
    def show_image(self)->None:
        pass
    
    @abstractmethod
    def resize_image(self, fx: int, fy:int)->None:
        pass
    
    @abstractmethod
    def crop_image(self, x:int, y:int, w:int, h:int)->None:
        pass


class OpenCVImage(Image):
    def __init__(self, path:str, name: str=None):
        self.path = path
        self.img = None
        self.name = name if name else "Image"
    
    def read_image(self)->None:
        self.img = cv2.imread(self.path)
    
    def show_image(self) -> None:
        if self.img is not None:
            cv2.imshow(self.name, self.img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
    def resize_image(self, fx: int, fy: int) -> None:
        if self.img is not None:
            self.img = cv2.resize(self.img, (0,0), fx=fx, fy=fx)
        
    def crop_image(
        self, x: int, y: int, w: int, h: int, resize: Tuple[int,int] = None,filter:bool=False
    ) -> np.ndarray:
        if self.img is not None:
            crop = self.img[x:x+w, y:y+h]
            if resize:
                fx, fy = resize
                crop = cv2.resize(crop, (0,0), fx=fx, fy=fy)
        
            if filter:
                rows, cols = crop.shape[:2]
                for i in range(rows*cols):
                    crop[i//cols][i%cols] = crop[i//cols][i%cols]*1.8
        
            return crop
        
        return

        
def app(image: Image)->None:
    image.read_image()
    image.resize_image(fx=1.5, fy=1.5)
    crop = image.crop_image(100,100,100,200, resize=(1.5,1.5), filter=True)
    crop = cv2.resize(crop, (0, 0), fx=2.5, fy=2.5)
    cv2.imshow("Crop-image", crop)
    image.show_image()

    
if __name__ == "__main__":
    img = OpenCVImage(path="aerial-landscape.png", name="Original-image")
    app(image=img)