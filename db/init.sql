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

INSERT INTO malignant_data
  (chrom, pos, id, ref, alt, qual, filter, freq)
VALUES
  ('20',68303, 'rs112879285', 'A', 'G', 60085.42, 'PASS', 2.03468e-04),
  ('20',68303, 'rs112879285', 'A', 'T', 60085.42, 'PASS', 1.19687e-05),
  ('20',68311, 'rs753351060', 'G', 'A', 1531.28,  'PASS', 3.98476e-06),
  ('20',68311, 'rs753351060', 'G', 'C', 1531.28,  'PASS', 7.96952e-06),
  ('20',68312, 'rs760137416', 'A', 'G', 4189.39,  'PASS', 3.98464e-06),
  ('20',68319, 'rs200068921', 'C', 'A', 1185.36,  'PASS', 0.1);