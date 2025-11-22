-----------------------------
------Daniel-Fridman---------
--- System-Immunology-Lab --- 
------Haifa-University ------
-----------2024--------------
-----------------------------
-----------------------------
--- General-Information -----
This program aim is to prepare input table which can be used as input for the LPA analysis program. 
The program first pulls the datasets from ImmuneDB tables located in MySQL server (if different server is in use, may need to change connector),
then the datasets are divided by metadata, processed, merged and modified. The final output dataframe (exported as csv) that can be used as LPA input. 
-----------------------------
-----------------------------
-----------------------------
-----------------------------
--- Required-Python-Modules -
1.  natsort
2.  math
3.  seaborn
4.  matplotlib
5.  numpy
6.  sklearn
7.  scipy
8.  typing
9.  pathlib
10. itertools
11. copy
12. altair
-----------------------------
-----------------------------
-----------------------------
-----------------------------
--- Guide ---
1. Configure the config.ini file as needed (see config section below).
2. Verify that all the needed packages are installed.
3. Run lpa_preprocessing.ipynb via jupyter notebook.
-----------------------------
-----------------------------
-----------------------------
-----------------------------
--- config.ini --------------
1. [mysql]
  a. host = MySQL host ip address
  b. port = MySQL host port
  c. user = MySQL host username
  d. pass = MySQL host password
  e. db = MySQL host ImmuneDB database name
  f. tables = tables to export from ImmuneDB MySQL server. 
     [default: clone_stats,clones,sample_metadata]
  g. metadata_og = original metadata column name to use for dataset division and filtering.
     [Example: metadata1,metadata2,metadata3]
  h. metadata_new = change the original metadata column name.
     [Example: new1,new2,new3]
  i. clones_filter = clones number threshold for dataset in final heatmap output, smaller dataset will be dropped. 
     [default: 10]
  j. filter_trunk = filter mutation by presance in clone.
  k. trunk_threshold = Mutation need to be at this threshold across clones to pass the filtration.
  l. nclones_threshold = Minimum number of unique clones.
  m. order_change = Bool value - if wanting to change the metadata column order.
  n. order_newval = Change order of the metadata columns.
  o. remap = map new names of the metadata columns.
-----------------------------
-----------------------------
-----------------------------
-----------------------------
--- Subfolders --------------
1. tables_output – result output, tables to be used in the LPA program.
2. tables_processed – tables used for processing, contains the metadata tables. 
3. raw_tables – raw tables exported from the MySQL server.
-----------------------------
-----------------------------
-----------------------------
-----------------------------
---Outputs-------------------
2. tables_output\\{db}\\{db}.dataset_sizes.csv -> Document containing information about the number of unique clones which has the specific element.
3. tables_output\\{db}\\{db}.documents.csv -> Frequency of elements in defined documents -> used as input for LPA.
-----------------------------
-----------------------------