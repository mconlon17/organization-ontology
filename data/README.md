# Data for Orgnizations
Here we have scripts for making organizational data (assertions about individuals) from ROR
data.  The goal is to have a command line script that can:

1. Take a ROR identifier
1. Get ROR JSON for the organization using the ROR API 
1. Convert to ORG ontology RDF resulting in a TTL file of assertions
    1. Convert the ROR JSON to RDF using `json2rdf`
    1. Convert the ROR RDF to ORG RDF using SPARQL CONSTRUCTS using `robot`

Eventually we hope to implement this command line script as an API written in JavaScript.

