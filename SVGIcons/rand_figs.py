
import numpy as np
import drawSvg as draw

from geom import *


def create_random():
    """
    Creates the fancy triangular shape and saves
    it as a .svg image.
    """

    # Parameters 
    n = 7
    s = 100.0
    bg_col = '#1248ff'
    fg_col = '#000000'
    name = 'random_pat'

    # Draw
    sz = 400
    d = draw.Drawing(sz, sz, origin='center')

    # Background
    bg_rect = draw.Rectangle(-sz / 2, -sz / 2, sz, sz, fill=bg_col)
    d.append(bg_rect)

    p = draw.Path(stroke_width=0, 
                  stroke=fg_col,
                  fill=fg_col, 
                  fill_opacity=1.0)

    n = 7
    polyg = get_reg_polygon(n, s)

    p.M(*polyg[:, -1])
    for k in range(n):
        p.L(*polyg[:, k])

    p.Z()
    d.append(p)

    # Save
    d.saveSvg(name + '.svg')
    pass



