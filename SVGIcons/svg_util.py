
import os

import numpy as np
import drawSvg as draw

# Where to store all produced images
img_path = "./Imgs"

def get_img_path(name):
    """
    Returns the path given the desired image
    name.
    """
    return os.path.join(img_path, name + ".svg")

# The default keyword arguments to initialize a draw.Path
def_path_kwargs = {'stroke_width': 2, 
                   'stroke': '#ffffff', 
                   'fill': '#000000',
                   'fill_opacity': 1.0}

def draw_points(pts, name, bg_margin_ratio, 
                bg_col = '#1248ff', 
                path_kwargs = def_path_kwargs):
    """
    Draws a path connecting the points and saves
    it as a svg image.
    """

    n = pts.shape[1]
    p = draw.Path(**path_kwargs)
    p.M(*pts[:, -1])
    for k in range(n):
        p.L(*pts[:, k])
    p.Z()

    # Background
    sz_half = int(bg_margin_ratio * np.max(np.abs(pts)))
    sz = 2 * sz_half    
    bg_rect = draw.Rectangle(-sz_half, -sz_half, sz, sz, fill=bg_col)

    # Draw
    d = draw.Drawing(sz, sz, origin='center')
    d.append(bg_rect)
    d.append(p)

    # Save
    save_path = get_img_path(name)
    d.saveSvg(save_path)



