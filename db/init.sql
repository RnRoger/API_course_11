create database vcfData;
use vcfData;

CREATE TABLE malignant_data (
    chrom    VARCHAR(5),
    pos      INTEGER,
    id       VARCHAR(25),
    REF      VARCHAR(5),
    alt      VARCHAR(5),
    qual     FLOAT(50),
    filter   VARCHAR(20),
    freq     FLOAT(50)
);