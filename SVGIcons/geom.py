

import numpy as np

def to_rad(degs):
    """
    Converts from degrees to radians.
    """
    return degs / 180 * np.pi

def to_deg(rads):
    """
    Converts from radians to degrees.
    """
    return rads * 180 / np.pi

def get_rot_mat(degs):
    """
    Returns a 2D rotation matrix.
    """

    rads = to_rad(degs)

    rot_mat =  np.array([[np.cos(rads), -np.sin(rads)], 
                        [np.sin(rads), np.cos(rads)]])

    return rot_mat

def get_iso_tria(side_len, rot = None):
    """
    Returns an isosceles triangle rotated by angle rot
    with a side length of 'side_len'.
    """

    # Compute distances
    cor_to_center_dist = 0.5 / np.cos(to_rad(30))
    tria_heigth = np.sqrt(0.75)
    offset_below = tria_heigth - cor_to_center_dist

    # Define the upright triangle
    tria_arr = side_len * np.array([[-0.5, -offset_below],
                                    [0.5, -offset_below],
                                    [0.0, cor_to_center_dist]] )
    tria_arr_trp = np.transpose(tria_arr)

    # Rotate
    if rot is not None:
        r_mat = get_rot_mat(rot)
        tria_arr_trp = np.matmul(r_mat, tria_arr_trp)

    # Return
    return tria_arr_trp
