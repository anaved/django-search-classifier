#-------------------------------------------------------------------------------
# Copyright (c) 2013 Findable.in
# All rights reserved. This program and the accompanying materials
# are property of Findable.in
# 
# Contributors:
#     naved - initial API and implementation
#-------------------------------------------------------------------------------
from abc import abstractmethod
from product.search_controller import DjSolr
from pysolr import Solr
import abc
import pysolr
'''
Created on Apr 27, 2012
 
@author: naved
 
'''

class BaseSolrIndexer(DjSolr):
    __metaclass__ = abc.ABCMeta
    @abstractmethod
    def get_id_prefix(self):
        '''
        prefix to be added with every id of different kind of data, this will be used while adding and deleting similar kind of data
        '''
        return
    
    
    
