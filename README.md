# customHashing


This solution makes use of locality sensitive hashing to solve the Record Linkage problem using the Python programming language. Locality sensitive hashing also the grouping of similar items to the same bucket, and dissimilar item to different buckets. This is computationally efficient for searching for similarity and prevent the pairwise comparison which can have higher order of polynomial (or even exponental) based on implementation.

The only software to be installed MurmurHash python module.

sudo pip install mmh3


There are many possible hashing function available. However, the murmurhashing is more computationally efficient and has less collision.
