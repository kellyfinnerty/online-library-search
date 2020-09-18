# Online Library Search


## Description
This python script searches a title and/or author on all the user's available online book resources - Overdrive, Hoopla, library catalogue, etc. 


## How it works
In terminal, run `python search.py`

The command line prompt will welcome you and give instructions on how to use it. Enter your search when prompted.

You provide the websites searched in a csv file the program reads from. (Instructions below)

You will have the option to search your preferred websites all at once or one at a time, so if you find what you are looking for you can end the search.

### CSV File Instructions

The file `urls.csv` will contain your websites.

Open the doc in excel or your preferred text editor. In the first column, fill in the name of the website and in the second enter the url you use to search with the search term replaced with curly brackets {}.

#### Example
1. Search as you normal would, ex. The Undocumented Americans
	https://www.hoopladigital.com/search?page=1&q=The+Undocumented+Americans&scope=everything&type=direct
2. Copy the url to excel 
3. Replace your search term (The Undocumented Americans) with {} brackets
	https://www.hoopladigital.com/search?page=1&q={}&scope=everything&type=direct

You can add, remove, and edit links as much as you like and the program will always draw from your latest version.


## Bye
Happy reading!
