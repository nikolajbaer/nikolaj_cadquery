import sys,os
from cadquery import *

class MonitorHolder(object):
    def __init__(self,workplane_start="front"):
        self.wp = Workplane(workplane_start)

    def build(self):
        cq = self.wp.box(30,30,5)
        cq = cq.faces(">Z").rect(28,28).workplane(offset=72-5)\
                .rect(20,20).loft(combine=True)\
                .faces(">Z").center(0,-10)\
                .rect(10,20,False).extrude(5)
        print cq.all() 
        return cq



