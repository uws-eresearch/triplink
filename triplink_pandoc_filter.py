#!/usr/bin/env python
import triplink

"""
Pandoc filter to convert 'triplinks' to 'real' semantic markup
"""

from pandocfilters import toJSONFilter, Link

def links(key, value, format, meta):
  if key == 'Link':
    show = value[0]
    (url, title) = value[1]
    
    tl = triplink.Triplink(url)
    if tl.isValid:
        #TODO: Construct this more nicelier
        newval = {"t": "Span","c":[["",[],[["about", tl.subject],
                                           ["property", tl.predicate],
                                           ["href", tl.object],
                                           ["title",tl.render("statement")]]],show]}
        
        return Link([newval],[tl.object,title])
    

if __name__ == "__main__":
  toJSONFilter(links)
