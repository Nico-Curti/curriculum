#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scholarly import scholarly

__author__ = ['Nico Curti']
__email__ = ['nico.curti2@unibo.it']

search_query = scholarly.search_author('Nico Curti')
me = next(search_query)
me = scholarly.fill(me)

print(len(me['publications']), me['citedby'], me['hindex'])
