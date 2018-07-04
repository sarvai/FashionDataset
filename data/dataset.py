import numpy as np
import json
from .csvdata import csvdata
from .entry import entry

class dataset :
    def __init__( self, cfg ):
        self._cfg = cfg
        fnames = csvdata( self._cfg.path.TMP.CSV % ( self._cfg.data.CSV.FILES ) )

        points = {}
        for name in self._cfg.data.CSV.POINTS :
            fname =  self._cfg.path.TMP.CSV % ( name )
            d = csvdata( fname )
            assert len(d) == len(fnames)
            points[ name ] = d

        self._entries = []

        for i in range( len(fnames) ):
            fname = fnames.get( i, 'image_url' )

            e = entry( self._cfg, fname )

            for n,p in points.items():
                assert p.get(i,'Input.image_url') == fname
                annot = p.get(i,'Answer.annotation_data')
                annot = json.loads( annot )
                e.add_points( n, annot )

            self._entries.append( e )

            #e = entry( fnames.get(i, 'image_url') )
            #self._entries.append( e )

    def __len__( self ):
        return len( self._entries )

    def __getitem__( self, index ):
        return self._entries[ index ]
