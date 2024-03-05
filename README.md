
## Dependencies
The script requires the following dependencies:

* pandas
* pubchempy
* requests
* argparse

These dependencies can be installed using pip, as follows:
```
pip install pandas pubchempy requests argparse
```

## Usage
To use the script, simply run it from the command line, passing the path to the CSV file containing the compound names. The CSV file must have a column named "compound_name" containing the names of the compounds to download.
```
python pubchem_3d_downloader.py path/to/compounds.csv
```

## Functionality
The script performs the following tasks:

1. Load table data into Pandas DataFrame
2. Loop through DataFrame and search PubChem for each compound
3. Loop through DataFrame and download the 3D structure of each compound
4. Save the SDF file for each compound in the same directory as the script


## Documentation
The script consists of the following functions:


None.

## Error Handling
The script includes error handling to handle the following errors:

* If the CSV file is not found, the script prints an error message and returns.
* If the compound is not found in PubChem, the script prints an error message and continues to the next compound.
* If the download of the SDF file fails, the script prints an error message and continues to the next compound.
* If there is an error saving the SDF file, the script prints an error message and continues to the next compound.

### Future Improvements
Some possible future improvements for this script include:

* Adding support for downloading the 2D structure of compounds in various file formats.
* Adding support for downloading other types of data from PubChem, such as properties, spectra, and bioactivity data.
* Adding support for downloading compounds in bulk, rather than one at a time.

