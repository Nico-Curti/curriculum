#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from habanero import Crossref
from scholarly import scholarly

__author__ = ['Nico Curti']
__email__ = ['nico.curti2@unibo.it']


name, surname = ('Nico', 'Curti')

# Retrieve the author's data, fill-in, and print
# Get an iterator for the author results
search_query = scholarly.search_author(' '.join((name, surname)))
# Retrieve the first result from the iterator
first_author_result = next(search_query)

# Retrieve all the details for the author
author = scholarly.fill(first_author_result)

titles = [x['bib']['title'] for x in author['publications']]

cr = Crossref()
bib = []

def add_if_possible (x, name):
  if name in x:
    return {name: x[name]}
  else:
    return ()
    
for title in titles:
  result = cr.works(query=title)
  res = result['message']['items']

  for x in res:

    try:
      authors = ' and '.join([', '.join([i['family'],
                                         i['given']])
                              for i in x['author']])
      assert surname in authors and name in authors
    except Exception as e:
      continue # Invalid article found

    try:
      bibtex = {
          'author': authors,
          'title': x['title'][0],
          'journal': x['container-title'][0],
          'doi': x['DOI'],
      }
    except:
      continue # These are mandatory fields so we must skip

    # These are possible extra fields
    bibtex.update(add_if_possible(x, 'ISNN'))
    bibtex.update(add_if_possible(x, 'publisher'))
    bibtex.update(add_if_possible(x, 'page'))
    bibtex.update(add_if_possible(x, 'volume'))
    bibtex.update(add_if_possible(x, 'url'))

    try:
      year, month, *day = x['published']['date-parts'][0]
      bibtex.update({'year': year})
      bibtex.update({'month': month})
      if day:
        bibtex.update({'day': day[0]})
    except Exception as e:
      assert False

    bib.append(bibtex)
    print('\rFound {:d} valid articles'.format(len(bib)), end='',
          flush=True, file=sys.stderr)
    break

bibtex = ''

for x in bib:
  doi = x['doi']
  bibtex += f'@article{{{doi},\n'
  bibtex += '\n'.join((f'  {k}={{{field}}},' for k, field in x.items()))
  bibtex += '\n}'
  bibtex += '\n\n'

print('\n', end='\n', flush=True, file=sys.stderr)
print(bibtex, end='\n', flush=True, file=sys.stdout)
