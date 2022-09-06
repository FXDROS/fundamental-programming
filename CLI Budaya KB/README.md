# CSV Input and Output

## About
This program is a simple database-like application of Indonesian traditional culture. The behaviour of this program imitates database queries. There are several things to be aware of. First, this program requires a csv file with the same directory as the code. There is a sample csv file called `kb1.csv` that you can use. The format for each row of the csv file is : <br> 
`<culture_name>, <type>, <province_origin>, <reference_url>` <br>

Another thing to be aware of is there must not exist any empty lines or else the code will not be able to read it. Here are some example of the correct csv file. <br>
![](./Screenshots/csv%20details.png)

## How To Use
This program consists of several commands:<br>
Import/Exporting CSV File:
- `IMPOR $filename.csv`<br>
To import a csv file. The `$filename` will be the name of the csv file.
- `EKSPOR $filename.csv`<br>
To export a csv file. The `$filename` will be the name of the csv file.

<br>
Search Queries:

- `CARINAMA $culture_name` <br>
To search for a specific culture by its **name**. The `$culture_name` will be the **name** of the culture.
- `CARITIPE $culture_type`<br>
To search for cultures by their **type**. The `$culture_type` will be the **type** of the culture.
- `CARIPROV $province_origin`<br>
To search for cultures by their **province**. The `$province_origin` will be the **province** of the culture.

<br>
Edit Queries:

- `TAMBAH $<culture_name>;;;<type>;;;<province_origin>;;;<reference_url>`<br>
Add new data to the csv file.
- `UPDATE $<culture_name>;;;<type>;;;<province_origin>;;;<reference_url>`<br>
Edit existing data in the csv file.
- `HAPUS $culture_name`<br>
Delete existing data from the csv file

<br>
Statistics Queries:

- `STAT`<br>
To count total rows in the csv file.
- `STATTIPE`<br>
To count total rows for each **culture type** in the csv file.
- `STATPROV`<br>
To count total rows for each **province** in the csv file.

<br>
Exiting the Program:

- `KELUAR`

<br>
Here are some example of the command used in this program: <br>

![](./Screenshots/execution%20sample.png)