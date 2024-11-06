__author__ = "730822380"


def get_coords(xs: str, ys: str) -> None:
    indexX = 0
    indexY = 0
    x = ""
    y = ""
    while indexX < len(xs):
        x = xs[indexX]
        while indexY < len(ys):
            y = ys[indexY]
            print("(" + x + y + ")")
            indexY += 1
        indexY = 0
        indexX += 1
