# dpi.py

A very simple python script/library for determining
the pixel density (dots per inch) of a monitor given
its aspect ratio, pixel dimensions and the size of
the diagonal.

## Some examples

```bash
$ ./dpi.py 21:9 2560x1080 25
110
$ ./dpi.py 16:9 1920x1080 23
96
$ ./dpi.py 16:9 1920x1080 27
82
```
