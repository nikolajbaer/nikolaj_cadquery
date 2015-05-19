import sys,os
from cadquery import *

class MonitorHolder(object):
    def __init__(self,workplane):
        self.wp = workplane

    def _outline(self,cq):
        cq.lineTo(225.0,0)\
          .threePointArc((230.0,5.0),(225.0,10.0))\
          .lineTo(0.0,10.0)\
          .threePointArc((-5,5.0),(0,0))\
          .close()        
        return cq

    def _notch(self,cq):
        return cq.rect(70,10)

    def build(self):
        cq = self._outline(self.wp)\
            .extrude(20,True)
        cq = cq.faces(">Z").workplane()\
             .moveTo(-112.5 + 10,0)\
             .rect(20,10).cutThruAll()
        return cq


