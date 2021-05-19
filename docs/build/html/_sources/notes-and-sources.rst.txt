Notes and Sources
=================

For early work on the Organization Ontology and thoughts behind what might be needed 
and how things might be addressed, we relied on "Early Thoughts on Representing 
Organizations in VIVO" by the VIVO Ontology Interest Group [VOIG2021]_.  While not 
everything there 
has been implemented here, and not everything here is implemented as described there, 
the general outline of representing organizations using |BFO|_ according to |OBOP|_ was
first described there.

We use [Wikipedia]_, [Wiktionary]_, and [Wikidata]_ often.  Term definitions, 
references, fact-checking, and identifiers may come from these sources.

We use Ontobee [Ong2017]_ for looking up terms in OBO Foundry ontologies.

We use Protege [Musen2015]_ for modeling ``org-header.ttl`` and the MIREOT plug-in for 
Protege [mireot]_ for
adding terms from other ontologies to ``org-header.ttl``  We use robot [robot]_ for
processing templates of properties, merging them and ``org-header.ttl`` together to
produce ``org.ttl`` and then to run reports against ``org.ttl`` for validation.

References
----------

.. [Wikipedia] Wikipedia (2021) we site.  http://wikipedia.org

.. [Wiktionary] Wiktionary (2021) web site. http://wiktionary.org

.. [Wikidata] Wikidata (2021) web site. http://wikidata.org

.. [Ong2017] Ong E, Xiang Z, Zhao B, Liu Y, Lin Y, Zheng J, Mungall C, Courtot M, 
   Ruttenberg A, He Y. Ontobee: A linked ontology data server to support ontology term 
   dereferencing, linkage, query, and integration. Nucleic Acid Research. 2017 
   Jan 4;45(D1):D347-D352. PMID: 27733503. PMCID: PMC5210626.

.. [VOIG2021] VIVO Ontology Interest Group (2021) Early Thoughts on the representation
   of organizations in VIVO.  on-line.  http://bit.ly/2EhMdPq
   
.. [Musen2015] Musen, M.A. The Protégé project: A look back and a look forward. AI Matters. 
   Association of Computing Machinery Specific Interest Group in Artificial Intelligence, 
   1(4), June 2015. https://doi.org/10.1145/2757001.2757003.

.. [mireot]
   
.. [robot]