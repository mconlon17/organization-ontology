
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    ontology-docs: from an ontology, generate docs in restructuredText suitable for
    inclusion in ontology ReadTheDocs style documentation
    
    table of classes
    table of annotation properties
    table object properties
    table of datatype properties
    
    Pages for each term
"""

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, XSD, SKOS, FOAF, DC, DCTERMS, TIME

__author__ = "Michael Conlon"
__copyright__ = "Copyright (c) 2021 Michael Conlon"
__license__ = "Apache-2"
__version__ = "0.0.1"

OBO= Namespace('http://purl.obolibrary.org/obo/')
OWL = Namespace('http://www.w3.org/2002/07/owl#')

g = Graph()

header = """
.. _Table {}:

.. table:: {}

    ===================  ========================  ================================================
    Property             Label                     Definition
    ===================  ========================  ================================================"""

trailer = "    ===================  ========================  ================================================"

toc_header ="""
.. toctree::
   :titlesonly:
   :caption: All
"""

def term_name(term_uri):

#  Given a term_uri, return a term_name that has a prefix
#
#  for example:  URIRef(http://purl.obolibrary.org/obo/BFO_0000001) returns 'obo:BFO_0000001'

   term_name_str = str(term_uri)
   term_name_str = term_name_str.replace(str(OBO), "obo:")
   term_name_str = term_name_str.replace(str(OWL), "owl:")
   term_name_str = term_name_str.replace(str(SKOS), "skos:")
   term_name_str = term_name_str.replace(str(RDF), "rdf:")
   term_name_str = term_name_str.replace(str(RDFS), "rdfs:")
   term_name_str = term_name_str.replace(str(FOAF), "foaf:")
   term_name_str = term_name_str.replace(str(TIME), "time:")
   term_name_str = term_name_str.replace(str(DC), "dc:")
   term_name_str = term_name_str.replace(str(DCTERMS), "dcterms:")
   
   return term_name_str
   
def write_term_page(term_uri):

	# give a term_uri in the graph g, write a page of documentation for the term_name
	
	term_name_str = term_name(term_uri)[term_name(term_uri).rfind(':')+1:]
	
	label = "None"
	for rlabel in g.objects(term_uri, RDFS.label):
		label = rlabel
		
	label_alt = "None"
	for rlabel_alt in g.objects(term_uri, OBO.IAO_0000118):
		label_alt = rlabel_alt
		
	definition = "None"
	for rdefinition in g.objects(term_uri, OBO.IAO_0000115):
		definition = rdefinition
		
	definition_source = "None"
	for rdefinition_source in g.objects(term_uri, OBO.IAO_0000119):
		definition_source = rdefinition_source
		
	example = "None"
	for rexample in g.objects(term_uri, OBO.IAO_0000112):
		example = rexample
		
	editors_note = "None"
	for reditors_note in g.objects(term_uri, OBO.IAO_0000116):
		editors_note = reditors_note
		
	term_editor = "None"
	for rterm_editor in g.objects(term_uri, OBO.IAO_0000117):
		term_editor = rterm_editor
	
	f = open('../source/doc-'+term_name_str+'.rst', "w")
	
	print("""
  .. _{}:
  .. _{}:
  .. index:: 
     single: {}; {}
     single: {}; {}

{} - {}
====================================================================================""".format(term_name_str, label, term_name_str, label, label, term_name_str, term_name_str, label), file=f)

	print("""
.. topic:: Alternate name for {}

    {}
""".format(label, label_alt), file =f)
	
	print("""
.. topic:: Definition

    {}
""".format(definition), file =f)

	print("""
.. topic:: Definition Source

    {}
""".format(definition_source), file =f)

	print("""
.. topic:: Example

    {}
""".format(example), file =f)

	print("""
.. topic:: Editor's Note

    {}
""".format(editors_note), file =f)

	print("""
.. topic:: Term Editor

    {}
""".format(term_editor), file =f)
	
	f.close()
	
	return

def main():
	g.parse("../../org.ttl", format="ttl")
	print(len(g))
    
# Iterate over all terms

	for term_type in [OWL.Class, OWL.AnnotationProperty, OWL.ObjectProperty, OWL.DatatypeProperty]:
	
		term_name_str = term_name(term_type)[term_name(term_type).rfind(':')+1:]
    
		f = open('../source/tab-' + term_name_str+'.rst', "w")
		
		toc = open('../source/toc-' + term_name_str + '.rst', 'w')
    	    
		print(header.format(term_name_str, term_name_str), file=f)
		
		print(toc_header, file=toc)
        
		for term_uri in sorted(g.subjects(RDF.type, term_type)):
			
			if str(term_uri)[0] != 'h':  # skip blank nodes
				continue
				
			write_term_page(term_uri)
			
			term_name_str = term_name(term_uri)[term_name(term_uri).rfind(':')+1:]
			print('   doc-' + term_name_str, file=toc)
				
			label = "None"
			for rlabel in g.objects(term_uri, RDFS.label):
				label = rlabel
				
			definition = "None"
			for rdefinition in g.objects(term_uri, OBO.IAO_0000115):
				definition = rdefinition
				
			term_name_str = '``'+term_name_str+'``'
			print('   ',term_name_str[0:19].ljust(20," "),label[0:24].ljust(25," "), definition[0:48], file=f)
			
		print(trailer, file=f)            
		f.close()
		toc.close()
	return

if __name__ == "__main__":
    main()