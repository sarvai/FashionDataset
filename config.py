from easydict import EasyDict as edict

class config :
    def _add_path( self, dataroot ):
        path = edict()

        path.TMP = edict()
        path.TMP.IMG = '%s/images/%s' % ( dataroot, '%s' )
        path.TMP.CSV = '%s/csv/%s.csv' % ( dataroot, '%s' )

        self._cfg.path = path

    def _add_data( self ):
        data = edict()
        data.CSV = edict()
        data.CSV.POINTS = [ 'Batch_Arms', 'Batch_shoulders_and_neck', 'Batch_Torso' ]
        data.CSV.FILES = 'file_list'

        self._cfg.data = data

    def _add_vis( self ):
        vis = edict()
        vis.SCALE = 0.5

        self._cfg.vis = vis

    def __init__( self, dataroot ):
        self._cfg = edict()

        self._add_path( dataroot )
        self._add_data()
        self._add_vis()

    @property
    def path( self ):
        return self._cfg.path

    @property
    def data( self ):
        return self._cfg.data

    @property
    def vis( self ):
        return self._cfg.vis
