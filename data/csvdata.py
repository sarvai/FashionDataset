import numpy as np
import csv
import json

class csvdata :
    def _load( self ):
        with open( self._fname, 'r' ) as csvfile :
            rows = csv.reader( csvfile, delimiter=',' )

            self._headers = None
            self._data = []

            for i,r in enumerate( rows ):
                if i == 0 :
                    self._headers = r
                else :
                    self._data.append( r )

    def __init__( self, fname ):
        self._fname = fname
        self._headers = None
        self._data = []

        self._load()

    @property
    def ndata( self ):
        return len( self._data )

    @property
    def headers( self ):
        return self._headers

    def data_for_header( self, h ):
        index = self.headers.index( h )

        data = []
        for d in self._data :
            data.append( d[index] )

        return data

    def __len__( self ):
        return len( self._data )

    def get( self, index, header ):
        hindex = self.headers.index( header )
        return self._data[index][hindex]
