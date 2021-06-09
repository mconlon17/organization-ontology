
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    ontology-docs: from an ontology, generate docs in restructuredText suitable for
    inclusion in ontology ReadTheDocs style documentation
    
    1. table of contents for term types
    2. tables of term types and tables of dispositions
    3. pages for each term
    4. [Optional] A VIVO 1 cross ref table for ontologies that reference VIVO 1 terms

"""

from rdflib import Graph, Literal, Namespace, URIRef, BNode
from rdflib.namespace import RDF, RDFS, XSD, SKOS, FOAF, DC, DCTERMS, TIME
import argparse

__author__ = "Michael Conlon"
__copyright__ = "Copyright (c) 2021 Michael Conlon"
__license__ = "Apache-2"
__version__ = "0.0.3"

OBO = Namespace('http://purl.obolibrary.org/obo/')
OWL = Namespace('http://www.w3.org/2002/07/owl#')

table_number = 0

g = Graph()
output_directory = "."



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

	f = open(output_directory + '/doc-'+term_name_str+'.rst', "w")
	
	print("""
  .. index:: 
     single: {}; {}
     single: {}; {}

{} - {}
====================================================================================\n""".format(term_name_str, label, label, term_name_str, term_name_str, label), file=f)
		
	terms = {
		RDFS.label         : "Label",
		OBO.IAO_0000111    : "Editor preferred label",
		OBO.IAO_0000118    : "Alternate name",
		SKOS.prefLabel     : "SKOS preferred Label",
		RDFS.subPropertyOf : "Sub property of",
		RDFS.subClassOf    : "Sub class of",
		OBO.IAO_0000115    : "Definition",
		SKOS.definition    : "SKOS definition",
		OBO.IAO_0000119    : "Definition source",
		RDFS.domain        : "Domain",
		RDFS.range         : "Range",
		OWL.inverseOf      : "Inverse of",
		OBO.IAO_0000112    : "Example",
		SKOS.example       : "SKOS xxample", 
		OBO.IAO_0000116    : "Editor's note",
		OBO.ORG_1000001    : "Similar term in VIVO 1 Ontology",
		OBO.IAO_0000412    : "Imported from", 
		OBO.IAO_0000117    : "Term editor",
		RDFS.seeAlso       : "See also",
		}

	for (term, term_name_data) in terms.items():
		term_value_list = []
		
		for term_value in g.objects(term_uri, term):
			if isinstance(term_value, BNode):
				continue
				
			# If a URI is from OBO, convert it to a document reference within the
			# documentation, as referenced terms are included in the docs
			
			if isinstance(term_value, URIRef):
				if str(term_value).startswith("http://purl.obolibrary.org/obo/"):
				    term_value = ':doc:`doc-' + term_value.removeprefix("http://purl.obolibrary.org/obo/") + '`'
				    
			term_value = term_value.replace("\n", "\n    ")  # new lines in RDF values must generate indented values in RestructuredText
			term_value_list.append(term_value)
			
		if len(term_value_list) == 0:
			continue
				
		print(".. topic:: {}\n".format(term_name_data), file=f)
		
		for term_value in term_value_list:
			print("    {}\n".format(term_value), file = f)
	
	f.close()
	
	return
	
def term_table(file_name, term_label, predicate, object):

	# Given a file name, term label, term type, predicate and object, create a table of the terms matching
	# the predicate and object
	
	global table_number
	

	header = """

See `Table {}`_.

.. _Table {}:

.. table:: Table {} {}

    =============================  ==================================================
    Term ID - Label                Definition
    =============================  =================================================="""

	trailer = "    =============================  =================================================="
	
	f = open(output_directory + '/' + file_name, "w")
	table_number += 1	
	print(header.format(table_number, table_number, table_number, term_label), file=f)
	
	for term_uri in sorted(g.subjects(predicate, object)):
		
		if str(term_uri)[0] != 'h':  # skip blank nodes
			continue
		
		term_name_str = term_name(term_uri)[term_name(term_uri).rfind(':')+1:]
		term_name_str = ':doc:`doc-' + term_name_str+'`'
			
		definition = "None"
		for rdefinition in g.objects(term_uri, OBO.IAO_0000115):
			definition = rdefinition
			
		first = True
		while len(definition) > 0:
			def_words = definition.split(' ')
			def_line = ''
			while len(def_line) + len(def_words[0]) + 1 <= 50:
				def_line = (def_line + ' ' if len(def_line) > 0 else '') + def_words[0]
				if len(def_words) == 1:
					break
				else:
					def_words = def_words[1:]
			if first:
				print('   ',term_name_str[0:29].ljust(30," "), def_line, file=f)
				first = False
			else:
				print('\n'.ljust(35," "), def_line, file=f)
			definition = definition.removeprefix(def_line)
			if len(definition) > 0 and definition[0] == ' ':
				definition = definition[1:]	
		
	print(trailer, file=f)
	f.close()
	return
	
def toc_table(term_type):

	# Given term type, write a table of contents file of all the terms of the given type	
	
	toc_header ="""
.. toctree::
   :titlesonly:
   :caption: All
	"""
	
	term_name_str = term_name(term_type)[term_name(term_type).rfind(':')+1:]		
	toc = open(output_directory + '/toc-' + term_name_str + '.txt', 'w')		
	print(toc_header, file=toc)
	
	for term_uri in sorted(g.subjects(RDF.type, term_type)):
		if isinstance(term_uri, BNode):
			continue
		term_name_str = term_name(term_uri)[term_name(term_uri).rfind(':')+1:]
		print('   doc-' + term_name_str, file=toc)
		       		
	toc.close()
	
def vivo_xref_table():

	# Look for annotations org:1000001 and make a table
	
	global table_number
	

	header = """

See `Table {}`_.

.. _Table {}:

.. table:: Table {} VIVO 1 Cross Reference

    ============================================================  ==================================================
    VIVO 1 Term URI                                               See ontology term
    ============================================================  =================================================="""

	trailer = "    ============================================================  =================================================="
	
	f = open(output_directory + '/' + 'tab-vivoxref.txt', "w")
	table_number += 1	
	print(header.format(table_number, table_number, table_number), file=f)
	
	unique = []
	
	for vivo_uri in sorted(g.objects(None, OBO.ORG_1000001)):
		
		if isinstance(vivo_uri, BNode):
			continue
			
		if vivo_uri not in unique:
			unique.append(vivo_uri)
			
			for term_uri in sorted(g.subjects(OBO.ORG_1000001, vivo_uri)):
		
				if isinstance(term_uri, BNode):
					continue
				
				term_name_str = term_name(term_uri)[term_name(term_uri).rfind(':')+1:]
				print('    ' + str(vivo_uri).ljust(62) + ':doc:`doc-' + term_name_str + '`', file=f)
		
	print(trailer, file=f)
	f.close()
	return

def main():

	global output_directory

	#  Read command line arguments, read ontology into graph, then
	#
	#  1. For each term of each type, write a term page.
	#
	#  2. Write a table of contents for each type
	#  
	#  3. Write tables of interest

	import argparse
	parser = argparse.ArgumentParser(description="""
	Read an ontology file and write documentation pages in RestructuredText for
	each term, a table of contents page for each term type, and tables of term
	types.
	
	The format of your ontology will be guessed from the file extension.  If you
	would like to specify the format, use --format=fmt, where fmt is one of
	ttl, xml, rdfa, grddl
	""")
	parser.add_argument("ontology_filespec", help="file spec of ontology to be read")
	parser.add_argument("output_directory", help="path to output directory", default='.')
	parser.add_argument("-f", "--format", help="ontology input format", default='ttl')
	parser.add_argument("--vivoxref", help="table of VIVO 1 cross references", action="store_true")
	args = parser.parse_args()
	output_directory = args.output_directory
	
	g.parse(args.ontology_filespec, format=args.format)
	print(len(g), 'triples in', args.ontology_filespec)
	
	# Write term pages

	for term_type in [OWL.Class, OWL.AnnotationProperty, OWL.ObjectProperty, 
	    OWL.DatatypeProperty, OWL.NamedIndividual]:
	    
		for term_uri in sorted(g.subjects(RDF.type, term_type)):
			
			if isinstance(term_uri, BNode):   # skip blank nodes
				continue
				
			write_term_page(term_uri)
			
	# Write tables of contents
	
	toc_table(OWL.Class)
	toc_table(OWL.AnnotationProperty)
	toc_table(OWL.ObjectProperty)
	toc_table(OWL.DatatypeProperty)
	toc_table(OWL.NamedIndividual)
	
	# Write term tables
		
	term_table("tab-all-types.txt", "Types of Organizations", RDFS.subClassOf, OBO.ORG_0000001)
	term_table("tab-all-dispositions.txt", "Dispositions", RDFS.subClassOf, OBO.BFO_0000016) # Dispositions
	term_table("tab-all-qualities.txt", "Qualities", RDFS.subClassOf, OBO.BFO_0000019) # Qualities
	term_table("tab-all-identifiers.txt", "Identifiers", RDFS.subClassOf, OBO.IAO_0000578) # Identifiers
	term_table("tab-all-classes.txt", "Classes", RDF.type, OWL.Class)
	term_table("tab-all-annotation-properties.txt", "Annotation Properties", RDF.type, OWL.AnnotationProperty)
	term_table("tab-all-object-properties.txt", "Object Properties", RDF.type, OWL.ObjectProperty)
	term_table("tab-all-datatype-properties.txt", "Datatype Properties", RDF.type, OWL.DatatypeProperty)
	term_table("tab-all-named-individuals.txt", "Named Individuals", RDF.type, OWL.NamedIndividual)
	
	if args.vivoxref:
		vivo_xref_table()
	
	print(table_number, "tables written in", args.output_directory)
	
	return

if __name__ == "__main__":
    main()