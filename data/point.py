import numpy as np

class point :
    def __init__( self, x, y, g, l ):
        self._x = x
        self._y = y
        self._group = g
        self._label = l

    @property
    def x( self ):
        return self._x

    @property
    def y( self ):
        return self._y

    @property
    def group( self ):
        return self._group

    @property
    def label( self ):
        return self._label
