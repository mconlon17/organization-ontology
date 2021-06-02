For Documentation Authors
=========================

We are learning about Sphinx and ReadTheDocs, and considering their use
for creating documentation for the VIVO Ontology and related ontologies.

One need is to provide search and index capability at the term level. A
user should be able to find the documentation for `date` or `person` or
`publication` without difficulty.  

Sphinx is *semantic* -- it fully separates document content and structure from 
document presentation.  Writers deal only with structure.  Themes deal with presentation.

Some things we should be able to do:

#. Create pages for each term using python scripts -- scripts would use annotation
   property values to automatically write pages of documentation.
   
#. Scripts should update the table of contents, glossary and index to keep everything
   complete and consistent.
   
#. No need for formatting examples -- use "View Page Source" on any page to see how it 
   was written
   
#. No need to write about the tools.  Each tool has outstanding documentation.

#. See `Sphinx <https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html>`_ to get
   started with the documentation.

#. Use `RestructuredText <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`_ to 
   write the documentation.  RestructuredText is a mark-up language originally developed to document python.
   
#. Use Github for collaboration, issue tracking, versional control, and release management for
   the documentation.  No need for Github wiki.  Put documentation in a ``docs`` folder of
   the ontology repository.
   
#. Use `ReadTheDocs <https://docs.readthedocs.io/en/stable/index.html>`_ for presenting 
   the documentation via HTML, PDF, or ePub.


