import numpy as np
import pickle
import cv2
import os

class analytics :
    def __init__( self, cfg, dataset ):
        self._cfg = cfg
        self._dataset = dataset

    def validate( self, outfile ):
        cv2.namedWindow('Image')

        scale = self._cfg.vis.SCALE

        if os.path.isfile( outfile ):
            with open( outfile, 'rb' ) as ff :
                response_list = pickle.load( ff )[0]
        else :
            response_list = {}
            for e in self._dataset :
                response_list[ e.name ] = '_'

        for i, (key, item) in enumerate( response_list.items() ):
            if item == '_' :
                start = i
                break

        print( start )

        if start == -1 :
            print('All images are verified, nothing to be done')
            return

        for e in self._dataset[start:] :
            im_path = self._cfg.path.TMP.IMG % ( e.name )

            img = cv2.imread( im_path )
            if scale != 1.0 :
                img = cv2.resize( img, None, None, scale, scale, 0 )

            for p in e :
                x = int(p.x * scale)
                y = int(p.y * scale)

                cv2.circle( img, (x,y), 1, (0,0,255), 3 )

            #print( img.shape )

            cv2.imshow( "Image", img )
            ch = chr(cv2.waitKey())

            if ch != 'x' :
                response_list[ e.name ] = ch
            else :
                break

            #print( ch )

        cv2.destroyAllWindows()
        cv2.waitKey(1)

        with open( outfile, 'wb' ) as ff :
            pickle.dump( [ response_list ], ff )
        print( 'Updated %s' % ( outfile ) )
