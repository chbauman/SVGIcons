
import numpy as np
import drawSvg as draw

from geom import *
from svg_util import *

def create_tria_svg():
    """
    Creates the fancy triangular shape and saves
    it as a .svg image.
    """

    # Parameters 
    d_0 = 0.3
    d_1 = 0.4
    f = 0.43
    alpha = 54
    s = 300
    bg_col = '#1248ff'
    fg_col = '#000000'
    name = 'fancy_tria'

    # Compute triangles
    main_tria = get_iso_tria(s)
    inner_tria = get_iso_tria(f * s, -alpha)

    # Draw
    sz = 800
    d = draw.Drawing(sz, sz, origin='center')

    # Background
    bg_rect = draw.Rectangle(-sz / 2, -sz / 2, sz, sz, fill=bg_col)
    d.append(bg_rect)

    p = draw.Path(stroke_width=0, 
                  stroke=fg_col,
                  fill=fg_col, 
                  fill_opacity=1.0)

    prev_corner = main_tria[:, -1]
    p.M(*prev_corner)
    for k in range(3):

        # Compute points
        curr_corner = main_tria[:, k]
        side_vec = curr_corner - prev_corner
        side_pt1 = prev_corner + d_0 * side_vec
        side_pt2 = prev_corner + (1 - d_1) * side_vec
        inner_pt = inner_tria[:, (k + 1) % 3]

        # Draw points
        p.L(*side_pt1)
        p.L(*inner_pt)
        p.L(*side_pt2)
        p.L(*curr_corner)

        prev_corner = curr_corner

    p.Z()
    d.append(p)

    # Save
    save_path = get_img_path(name)
    d.saveSvg(save_path)
