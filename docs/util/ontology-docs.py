
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    ontology-docs: from an ontology, generate docs in restructuredText suitable for
    inclusion in ontology ReadTheDocs style documentation
    
    1. table of contents for term types
    2. tables of term types and tables of dispositions
    3. pages for each term
    
    TODO:  All tables made by one function
           Table entries link to pages
           Table column width determined by contents
           Clarify three functions -- write pages, generate tables, generate TOC
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
    Term ID              Label                     Definition
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
	
	label = "No label"
	for rlabel in g.objects(term_uri, RDFS.label):
		label = rlabel

	f = open('../source/doc-'+term_name_str+'.rst', "w")
	
	print("""
  .. _{}:
  .. _{}:
  .. index:: 
     single: {}; {}
     single: {}; {}

{} - {}
====================================================================================\n""".format(term_name_str, label, term_name_str, label, label, term_name_str, term_name_str, label), file=f)
		
	terms = {
		RDFS.label : "Label",
		OBO.IAO_0000118 : "Alternate name",
		SKOS.prefLabel  : "SKOS Preferred Label",
		DC.identifier   : "DC identifier",
		OBO.IAO_0000115 : "Definition",
		SKOS.definition : "SKOS Definition",
		OBO.IAO_0000119 : "Definition source",
		OBO.IAO_0000112 : "Example",
		SKOS.example    : "SKOS Example", 
		OBO.IAO_0000116 : "Editor's note",
		OBO.IAO_0000412 : "Imported From", 
		OBO.IAO_0000117 : "Term editor",
		RDFS.seeAlso    : "See also",
		}

	for (term, term_name_data) in terms.items():
		term_value_list = []
		
		for term_value in g.objects(term_uri, term):
			term_value = term_value.replace("\n", "\n    ")  # new lines in RDF values must generate indented values in RestructuredText
			term_value_list.append(term_value)
			
		if len(term_value_list) == 0:
			continue
				
		print(".. topic:: {}\n".format(term_name_data), file=f)
		
		if len(term_value_list) == 0:
			print("    No value\n", file = f)
		else:
			for term_value in term_value_list:
				print("    {}\n".format(term_value), file = f)
	
	f.close()
	
	return
	
def term_table(file_name, term_label, predicate, object):

	# Given a file name, term label, term type, predicate and object, create a table of the terms matching
	# the predicate and object
	
	f = open(file_name, "w")	
	print(header.format(term_label, term_label), file=f)
	
	for term_uri in sorted(g.subjects(predicate, object)):
		
		if str(term_uri)[0] != 'h':  # skip blank nodes
			continue
		
		term_name_str = term_name(term_uri)[term_name(term_uri).rfind(':')+1:]
			
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
	return

def main():
	g.parse("../../org.ttl", format="ttl")
	print(len(g))

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
		
	term_table("../source/tab-dispositions.rst", "Dispositions", RDFS.subClassOf, OBO.BFO_0000016) # Dispositions
	return

if __name__ == "__main__":
    main()