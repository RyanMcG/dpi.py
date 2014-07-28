#!/usr/bin/env python
import math
from sys import argv, exit


def dimensions_of_ratio_and_diagonal(ratio, diagonal):
    r = ratio[0] / ratio[1]
    x = diagonal / math.sqrt(1 + r ** 2)
    return (r * x, x)


def dpis_from_pixel_dimensions_and_physical_dimensions(pix_ds, phys_ds):
    dpih = pix_ds[0] / phys_ds[0]
    dpiv = pix_ds[1] / phys_ds[1]
    return (dpih, dpiv)


def dpis(ratio, px_ds, diagonal):
    phys_ds = dimensions_of_ratio_and_diagonal(ratio, diagonal)
    return dpis_from_pixel_dimensions_and_physical_dimensions(px_ds, phys_ds)

def _avg(coll):
    return round(sum(coll) / len(coll))

def dpi(ratio, px_ds, diagonal):
    return _avg(dpis(ratio, px_ds, diagonal))


def _tuple_from_arg_split_on(arg_index, split_on):
    return tuple([float(y) for y in argv[arg_index].split(split_on)])

def summary(dps):
    return """\
            Dots per X
horizontal  {hdpi}
vertical    {vdpi}
average     {adpi}\
""".format(hdpi=dps[0], vdpi=dps[1], adpi=_avg(dps))

def _main():
    if len(argv) != 4:
        print("Must be given three arguments like:\n")
        print("  dpi.py 21:9 2550x1080 25")
        exit(1)
    ratio = _tuple_from_arg_split_on(1, ":")
    pixel_ds = _tuple_from_arg_split_on(2, "x")
    diagonal = float(argv[3])
    print(summary(dpis(ratio, pixel_ds, diagonal)))


if __name__ == "__main__":
    _main()
