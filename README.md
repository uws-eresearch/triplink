# Triplink

## What is this?

This is a set of (Alpha quality) tools for encoding RDF triples in URLs.

Eg:  

```http://ontologize.me/?tl_p=http://purl.org/dc/terms/creator&triplink=http://purl.org/triplink/v/0.1&tl_o=http://orcid.org/0000-0002-3545-944X```


For some simple examples see [Ontologize.me][ont].


## How to use
At the moment, the only working code is a [pandoc] filter.

To try it out, run this README through pandoc and see how this looks:

> [Peter Sefton][ptauth] is the author of this document.

This produces RDFa markup asserting authorship:
```
<p><span about="." property="http://purl.org/dc/terms/creator" href="http://orcid.org/0000-0002-3545-944X" title="The person or agent http://orcid.org/0000-0002-3545-944X is a creator of this resource: .">Peter Sefton</span> is the author of this document</p>

```

Which RDFaplay.info interprets thus:

```
@prefix dc: <http://purl.org/dc/terms/> .

<http://rdfa.info/play/>
   dc:creator <http://orcid.org/0000-0002-3545-944X> .
```



[ont]: http://ontologize.me
[pandoc]: http://johnmacfarlane.net/pandoc
[ptauth]:  http://ontologize.me/?tl_p=http://purl.org/dc/terms/creator&triplink=http://purl.org/triplink/v/0.1&tl_o=http://orcid.org/0000-0002-3545-944X

