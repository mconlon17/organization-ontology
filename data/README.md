# Data for Organizations

## Dates

See `template\dates.tsv` for a template for creating dates data.  The build script 
`build.sh` uses this template to create data in `data\dates.ttl`
  
## Locations

We plan a template to create continents and countries of the world.  The template should 
be easily
extensible to create populated places for countries.

## Organizations

Here we will have scripts for making organizational data (assertions about individuals) from ROR
data.  The goal is to have a command line script that can:

1. Take a ROR identifier
1. Get ROR JSON for the organization using the ROR API 
1. Convert to ORG ontology RDF resulting in a TTL file of assertions
    1. Convert the ROR JSON to RDF using `json2rdf`
    1. Convert the ROR RDF to ORG RDF using SPARQL CONSTRUCTS using `robot`

Eventually we hope to implement this command line script as an API written in JavaScript.

