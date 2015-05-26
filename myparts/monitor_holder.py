import sys,os
import FreeCAD
from cadquery import *

class Part(object):
    def __init__(self,workplane_start="front"):
        self.wp = Workplane(workplane_start)

    def build(self):
        cq = self.wp.box(30,30,5)
        cq = cq.faces(">Z").rect(15,15)\
                .workplane(offset=72-5-20).rect(8,8)\
                .workplane(offset=20).rect(16,16)
        cq = cq.loft(combine=True)\
                .faces(">Z").center(0,-8)\
                .rect(8,16,False).extrude(8)
        return cq



