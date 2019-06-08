# Introduction

Variants with a frequency (MAF) lower than 0.01 are considered to be malignant. For our course 11 project we were asked to build an API which returns information if a variant is considered malignant. We combined this with a snakemake workflow to retrieve additional info if the variant is indeed considered malignant. 

## Input 

For variant information we used exome data from gnomad [1]. We didn't store all the information due to lack of storage space.

Below you see which data we stored and some examples:


```
chrom	 pos	    id		ref	alt	  qual		filter	  freq
20	68303	rs112879285	A	G	60085.42	PASS	2.03468e-04
20	68303	rs112879285	A	T	60085.42	PASS	1.19687e-05
20	68311	rs753351060	G	A	1531.28		PASS	3.98476e-06

```

## Output

At the end of the snakemake workflow a html report is created. In this report all files with additional info about the variant are being displayed. 
In the end we've created five files:
	- variant_info.txt	
	- ensembl_application.json
	- SNP_info.json
	- workflow.svg
	- report.html
	

# Dependencies

* snakemake
* docker


# Versioning

* Version 1.0 - 12-06-2019

  
# Authors

* **Awan Al Koerdi** 
* **Melanie Opperman** 


# Acknowledgement

We would like to acknowledge Rogier Stegeman and Johannes Köster for their help with our project. 


