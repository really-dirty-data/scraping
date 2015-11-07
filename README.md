## Scraping (downloading)

The following code provides code to download the data files of the [National Health Interview Survey](http://www.cdc.gov/nchs/nhis/quest_data_related_1997_forward.htm) for the years 1997 until the present. 

At the moment, the process involves a couple of _for-loops_ that
1. Create a new directory *Data* and subdirectories for each year
2. Download the zipped files into the subdirectories and unzip them into .dat files
3. Download the accompanying .sas files 

Subsequently, the file *lower.py* can be called within the *Data* folder to rename the files that unzip to uppercase file names to lowercase. 

This is an initial attempt at the code, so expect updates that turn the hacky *for-loops* into proper functions and other improvements to the workflow. Stay tuned!
