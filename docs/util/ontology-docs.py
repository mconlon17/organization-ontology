
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    ontology-docs: from an ontology, generate docs in restructuredText suitable for
    inclusion in ontology ReadTheDocs style documentation
    
    1. table of contents for term types
    2. tables of term types and tables of dispositions
    3. pages for each term
    
    TODO:  Table entries link to pages
           Table column width determined by contents
"""

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, XSD, SKOS, FOAF, DC, DCTERMS, TIME

__author__ = "Michael Conlon"
__copyright__ = "Copyright (c) 2021 Michael Conlon"
__license__ = "Apache-2"
__version__ = "0.0.1"

OBO = Namespace('http://purl.obolibrary.org/obo/')
OWL = Namespace('http://www.w3.org/2002/07/owl#')

table_number = 0

g = Graph()

header = """

See `Table {}`_.

.. _Table {}:

.. table:: Table {} {}

    ======================  ========================  ================================================
    Term ID                 Label                     Definition
    ======================  ========================  ================================================"""

trailer = "    ======================  ========================  ================================================"

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
		OBO.ORG_1000001 : "Similar term in VIVO 1 Ontology",
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
	
	global table_number
	
	f = open(file_name, "w")
	table_number += 1	
	print(header.format(table_number, table_number, table_number, term_label), file=f)
	
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
		print('   ',term_name_str[0:22].ljust(23," "),label[0:24].ljust(25," "), definition[0:48], file=f)
		
	print(trailer, file=f)
	f.close()
	return
	
def toc_table(term_type):

	# Given term type, write a toc file of all the terms of the given type
	
	term_name_str = term_name(term_type)[term_name(term_type).rfind(':')+1:]		
	toc = open('../source/toc-' + term_name_str + '.txt', 'w')		
	print(toc_header, file=toc)
	
	for term_uri in sorted(g.subjects(RDF.type, term_type)):
		if str(term_uri)[0] != 'h':  # skip blank nodes
			continue
		term_name_str = term_name(term_uri)[term_name(term_uri).rfind(':')+1:]
		print('   doc-' + term_name_str, file=toc)
		       		
	toc.close()

def main():
	ontology_path = "../../org.ttl"
	g.parse(ontology_path, format="ttl")
	print(len(g), 'triples in', ontology_path)
	
	# Write term pages

	for term_type in [OWL.Class, OWL.AnnotationProperty, OWL.ObjectProperty, 
	    OWL.DatatypeProperty, OWL.NamedIndividual]:
	    
		for term_uri in sorted(g.subjects(RDF.type, term_type)):
			
			if str(term_uri)[0] != 'h':  # skip blank nodes
				continue
				
			write_term_page(term_uri)
			
	# Write tables of contents
	
	toc_table(OWL.Class)
	toc_table(OWL.AnnotationProperty)
	toc_table(OWL.ObjectProperty)
	toc_table(OWL.DatatypeProperty)
	toc_table(OWL.NamedIndividual)
	
	# Write term tables
		
	term_table("../source/tab-all-types.txt", "Types of Organizations", RDFS.subClassOf, OBO.ORG_0000001)
	term_table("../source/tab-all-dispositions.txt", "Dispositions", RDFS.subClassOf, OBO.BFO_0000016) # Dispositions
	term_table("../source/tab-all-classes.txt", "Classes", RDF.type, OWL.Class)
	term_table("../source/tab-all-annotation-properties.txt", "Annotation Properties", RDF.type, OWL.AnnotationProperty)
	term_table("../source/tab-all-object-properties.txt", "Object Properties", RDF.type, OWL.ObjectProperty)
	term_table("../source/tab-all-datatype-properties.txt", "Datatype Properties", RDF.type, OWL.DatatypeProperty)
	term_table("../source/tab-all-named-individuals.txt", "Named Individuals", RDF.type, OWL.NamedIndividual)
	print(table_number, "tables written")
	
	return

if __name__ == "__main__":
    main()