import numpy as np
from .point import point

class entry :
    def __init__( self, cfg, name ):
        self._name = name
        self._points = []

    def add_points( self, pgroup, pdata ):
        for p in pdata :
            pp = point( p['left'], p['top'], pgroup, p['label'] )
            self._points.append( pp )

    @property
    def name( self ):
        return self._name

    def __len__( self ):
        return len( self._points )

    def __getitem__( self, index ):
        return self._points[ index ]
