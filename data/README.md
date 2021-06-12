# Data for Organizations

## Dates

The build script 
`./build.sh` uses a template and `robot` to create data in `data\dates.ttl`
  
## Locations

See `./build.sh` for a script to convert a TSV file of locations (`source\locations.tsv`)
into a ttl file of locations represented using the Organization Ontology.

## Organizations

The build script `./build.sh` also produces organization data from information
provided by ROR, the Research Organization Registry.  As delivered, the
script provides a demo, fetching data for the University of Florida and 
representing it using the Organization Ontology as RDF data in the build 
directory.  You can modify the script to change the ROR ID and the filename to 
fetch and build any of the nearly 100,000 organizations in ROR.
