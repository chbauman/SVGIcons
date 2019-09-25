
import numpy as np
import drawSvg as draw

from geom import *
from svg_util import *

def create_random():
    """
    Creates the fancy triangular shape and saves
    it as a .svg image.
    """

    # Parameters 
    n = 31
    n_connect = 13
    s = 50.0
    bg_col = '#1248ff'
    fg_col = '#000000'
    line_col = '#ffffff'
    name = 'random_pat'
    bg_margin_ratio = 1.2

    # Compute polygon
    polyg = get_reg_polygon(n, s)

    p = draw.Path(stroke_width=2, 
                  stroke=line_col,
                  fill=fg_col, 
                  fill_opacity=1.0)    
    p.M(*polyg[:, -n_connect])
    for k in range(n):
        p.L(*polyg[:, (n_connect * k) % n])

    p.Z()

    # Background
    sz_half = int(bg_margin_ratio * np.max(np.abs(polyg)))
    sz = 2 * sz_half    
    bg_rect = draw.Rectangle(-sz_half, -sz_half, sz, sz, fill=bg_col)

    # Draw
    d = draw.Drawing(sz, sz, origin='center')
    d.append(bg_rect)
    d.append(p)

    # Save
    save_path = get_img_path(name)
    d.saveSvg(save_path)



