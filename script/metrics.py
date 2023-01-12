#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import pylab as plt
import seaborn as sns
from datetime import date
from scholarly import scholarly

__author__ = ['Nico Curti']
__email__ = ['nico.curti2@unibo.it']


# Retrieve the author's data, fill-in, and print
# Get an iterator for the author results
search_query = scholarly.search_author('Nico Curti')
# Retrieve the first result from the iterator
first_author_result = next(search_query)

# Retrieve all the details for the author
author = scholarly.fill(first_author_result)

hindex = author['hindex']
cited = author['citedby']
publications = len(author['publications'])
interests = author['interests']
cites_per_year = author['cites_per_year']
url = author['url_picture'].replace('view_op=medium_photo&', '')
pub_per_year = []

for x in author['publications']:
  try:
    year = int(x['bib']['pub_year'])
    cites = int(x['num_citations'])
    pub_per_year.append((year, cites))

  except KeyError:
    # these are the "useless" works
    pass

with sns.plotting_context('paper', font_scale=2):

  fig, ((ax1), (ax2)) = plt.subplots(nrows=2, ncols=1, figsize=(7, 10), sharex=True)

  cite = pd.DataFrame.from_dict(cites_per_year, orient='index', columns=['citations'], dtype=int)
  cite['year'] = cite.index

  pub = pd.DataFrame(pub_per_year, columns=['year', 'citations'], dtype=int)
  my, My = pub['year'].min(), cite['year'].max()

  sns.histplot(pub, x='year', ax=ax1, bins=len(cite['year'].unique()),
               discrete=True, shrink=.75,
               color='cornflowerblue', edgecolor='k',
              )
  _ = ax1.set_xticks(range(my, My+1))
  _ = ax1.set_xlabel('year')
  _ = ax1.set_ylabel('articles')
  _ = ax1.set_title('Articles per year')
  m, M = ax1.get_ylim()
  _ = ax1.set_yticks(range(0, int(M)+1, int(M)//2))
  _ = ax1.axhline(y=M//2, color='lightgray', linestyle='-', alpha=.5)
  _ = ax1.axhline(y=int(M),    color='lightgray', linestyle='-', alpha=.5)
  sns.despine(ax=ax1, offset=1, top=True, right=True, bottom=False, left=False)

  m, M = cite['citations'].min(), cite['citations'].max()

  _ = ax2.axhline(y=M//2, color='lightgray', linestyle='-', alpha=.5)
  _ = ax2.axhline(y=M,    color='lightgray', linestyle='-', alpha=.5)

  _ = ax2.bar(cite['year'], cite['citations'], align='center', width=0.75,
              edgecolor='darkgray', color='lightgray')
  _ = ax2.set_xticks(range(my, My+1))
  _ = ax2.set_xlabel('year')
  _ = ax2.set_ylabel('citations')
  _ = ax2.set_title('Citations per year')
  sns.despine(ax=ax2, offset=1, top=True, right=True, bottom=False, left=False)
  _ = ax2.set_yticks(range(0, M+1, M//2))

  ax1.text(-0.1, 1.25, 'Author:',
           horizontalalignment='left',
           verticalalignment='center',
           fontweight='bold',
           fontsize=12,
           rotation=0,
           transform=ax1.transAxes)
  ax1.text(0.04, 1.25, 'Nico Curti',
           horizontalalignment='left',
           verticalalignment='center',
           fontweight='normal',
           fontsize=12,
           rotation=0,
           transform=ax1.transAxes)
  ax1.text(0.6, 1.25, 'Update at:',
           horizontalalignment='left',
           verticalalignment='center',
           fontweight='bold',
           fontsize=12,
           rotation=0,
           transform=ax1.transAxes)
  ax1.text(0.8, 1.25, '{}'.format(date.today().strftime('%m/%d/%Y')),
           horizontalalignment='left',
           verticalalignment='center',
           fontweight='normal',
           fontsize=12,
           rotation=0,
           transform=ax1.transAxes)

  ax1.text(-0.1, 1.15, 'Interests:',
           horizontalalignment='left',
           verticalalignment='center',
           fontweight='bold',
           fontsize=12,
           rotation=0,
           transform=ax1.transAxes)
  ax1.text(0.08, 1.15, '{}'.format(', '.join(interests)),
           horizontalalignment='left',
           verticalalignment='center',
           fontweight='normal',
           fontsize=12,
           rotation=0,
           transform=ax1.transAxes)

  ax2.text(-0.1, -0.3, 'Citations:',
           horizontalalignment='left',
           verticalalignment='center',
           fontweight='bold',
           fontsize=12,
           rotation=0,
           transform=ax2.transAxes)
  ax2.text(0.075, -0.3, '{}'.format(cited),
           horizontalalignment='left',
           verticalalignment='center',
           fontweight='normal',
           fontsize=12,
           rotation=0,
           transform=ax2.transAxes)

  ax2.text(0.35, -0.3, 'Articles:',
           horizontalalignment='left',
           verticalalignment='center',
           fontweight='bold',
           fontsize=12,
           rotation=0,
           transform=ax2.transAxes)
  ax2.text(0.5, -0.3, '{}'.format(publications),
           horizontalalignment='left',
           verticalalignment='center',
           fontweight='normal',
           fontsize=12,
           rotation=0,
           transform=ax2.transAxes)

  ax2.text(0.8, -0.3, 'h-index:',
           horizontalalignment='left',
           verticalalignment='center',
           fontweight='bold',
           fontsize=12,
           rotation=0,
           transform=ax2.transAxes)
  ax2.text(0.95, -0.3, '{}'.format(hindex),
           horizontalalignment='left',
           verticalalignment='center',
           fontweight='normal',
           fontsize=12,
           rotation=0,
           transform=ax2.transAxes)

  ax2.text(-0.1, -0.45, '* This figure was automatically generated and could not perfectly reflect\n'
                        'the real metrics of the author',
           horizontalalignment='left',
           verticalalignment='center',
           fontweight='normal',
           color='gray',
           fontsize=12,
           rotation=0,
           transform=ax2.transAxes)

  fig.savefig('../img/metrics.png', dpi=200, bbox_inches='tight')