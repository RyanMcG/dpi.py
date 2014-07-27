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


def dpi(ratio, px_ds, diagonal):
    phys_ds = dimensions_of_ratio_and_diagonal(ratio, diagonal)
    dpis = dpis_from_pixel_dimensions_and_physical_dimensions(px_ds, phys_ds)
    return int(round(sum(dpis) / len(dpis)))


def __tuple_from_arg_split_on(arg_index, split_on):
    return tuple([int(y) for y in argv[arg_index].split(split_on)])


def __main():
    if len(argv) != 4:
        print("Must be given three arguments like:\n")
        print("  dpi.py 21:9 2550x1080 25")
        exit(1)
    ratio = __tuple_from_arg_split_on(1, ":")
    pixel_ds = __tuple_from_arg_split_on(2, "x")
    diagonal = int(argv[3])
    print(dpi(ratio, pixel_ds, diagonal))


if __name__ == "__main__":
    __main()
