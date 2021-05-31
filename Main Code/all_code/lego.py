import cv2 as cv
import numpy as np

class lego:
    def __init__(self,ratio = None ,color= None, contour= None, rect_non_rect = None):
        self.ratio = ratio
        self.contour = contour
        self.color = color
        self.rect = rect_non_rect # True or false

    def get_corners(self):
        '''
        Returns the coordinates of the corners
        '''
        if self.rect:
            x,y,w,h = cv.boundingBox(self.approx)
            top_right_corner =(x+w,y)
            bottom_left_corner = (x,y+h)
            bottom_right_corner = (x+w,y+h)
            top_left_corner = (x,y)

            corners = [top_left_corner, top_right_corner, bottom_left_corner, bottom_right_corner]

        else:
            corners = self.contour

        return corners

