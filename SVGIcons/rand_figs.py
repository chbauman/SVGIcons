
import numpy as np
import drawSvg as draw

from geom import *
from svg_util import *

def create_random():
    """
    Creates some shape and saves
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
    star = poly_to_star(polyg, n, n_connect)

    # Draw and save
    draw_points(star, name, bg_margin_ratio)

    return



