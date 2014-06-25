#!/usr/bin/env python
import triplink

"""
Pandoc filter to convert 'triplinks' to 'real' semantic markup
"""

from pandocfilters import toJSONFilter, Str

def links(key, value, format, meta):
  if key == 'Link':
    show = value[0]
    url = value[1][0]
    tl = triplink.Triplink(url)
    if tl.isValid:
        #TODO: Construct this more nicelier
        newval = {"t": "Span","c":[["",[],[["about", tl.subject],
                                           ["property", tl.predicate],
                                           ["href", tl.object],
                                           ["title",tl.render("statement")]]],show]}
        return newval
    

if __name__ == "__main__":
  toJSONFilter(links)
