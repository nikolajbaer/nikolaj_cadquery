import sys,os
from cadquery import *
import optparse

sys.path.append('/Applications/FreeCAD.app/Contents/lib/')

if __name__=="__main__":
    from myparts.monitor_holder import MonitorHolder
    a = MonitorHolder(Workplane("bottom"))
    
    o = a.build() 

    o.exportSvg("out.svg")
    os.system("open out.svg")

    # option - stl

