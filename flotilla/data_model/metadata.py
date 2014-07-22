import sys

from .base import BaseData


# Any informational data goes here

class MetaData(BaseData):
    def __init__(self, data, celltype_order=None):
        super(MetaData, self).__init__(data, outliers=None)
        self.celltype_order = celltype_order

    def _get(self, sample_metadata_filename=None, gene_metadata_filename=None,
             event_metadata_filename=None):

        metadata = {'sample': None,
                    'gene': None,
                    'event': None}
        try:
            if sample_metadata_filename is not None:
                metadata['sample'] = self.load(*sample_metadata_filename)
            if event_metadata_filename is not None:
                metadata['event'] = self.load(*event_metadata_filename)
            if gene_metadata_filename is not None:
                metadata['gene'] = self.load(*gene_metadata_filename)

        except Exception as E:
            sys.stderr.write("error loading descriptors: %s, \n\n .... "
                             "entering pdb ... \n\n" % E)
            raise E

        return {'experiment_design_data': metadata['sample'],
                'feature_data': metadata['gene'],
                'event_metadata': metadata['event'],
                'expression_metadata': None}
