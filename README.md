# braxfr | Brute Force DNS Zone Transfer
`braxfr` attempts to simulate a zone transfer for DOMAIN without use of AXFR. 
It uses dig and a brute force dictionary to discover resource records and 
construct a zone file. Although accuracy is not 100% guaranteed, braxfr will
generally discover a significant number of resource records associated with
DOMAIN. braxfr performance is dependent on network capacity where it is run,
concurrency, and resolve response time. An attempt will be made to discover and
exclude wildcard records (listed as a single record * IN A...)

## Usage
For usage instructions, check `./braxfr -h`
