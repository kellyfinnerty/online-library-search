# Online Library Search


## Description

ebooks and audiobooks are often readily available on sites like Overdrive and Hoopla. Many people have access to multiple library systems. Each library has a different catalogue and sometimes copies aren't available at that time. Often a user must search multiple Overdrives to find an available copy, but this can be too time consuming and they may opt to buy or go on the wait list instead of continuing the search. Multiple library searches can be done at once with this python script. Users add the urls of their libraries to a csv file and can search through python command line prompts. Quickly click through the tabs until you find what you're looking for. 

## How it works
In terminal, run `python search.py`

The command line prompt will welcome you and give instructions on how to use it. Enter your search when prompted.

You provide the websites searched in a csv file the program reads from. (Instructions below)

You will have the option to search your preferred websites all at once or one at a time (so if you find what you are looking for you can end the search).

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
