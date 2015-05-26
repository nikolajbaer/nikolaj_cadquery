import sys,os
from cadquery import *
import optparse

sys.path.append('/Applications/FreeCAD.app/Contents/lib/')


def build_part(name):
    try:
        mod = __import__("myparts.%s"%name,fromlist=["Part"])
        Klass = getattr(mod,"Part")
        p = Klass()
        o = p.build()
        return o
    except ImportError as e:
        print e
        
    #from myparts.monitor_holder import MonitorHolder
    #a = MonitorHolder()
    #o = a.build() 

def export_part(o):
    o.exportSvg("out.svg")
    os.system("open out.svg")
    with open("out.stl","wb") as f:
        f.write(exporters.toString(o,'STL'))

    # option - stl

if __name__=="__main__":
    part = build_part(sys.argv[1])
    export_part(part)
