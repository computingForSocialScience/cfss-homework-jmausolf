# Welcome to the README for Get-White-House-Data PKG

# Overview

This package utilizes both Python and Shell scripts to create a unique text file for every speech and remark from the White House:

https://www.whitehouse.gov/briefing-room/speeches-and-remarks

This generates, logs, and sorts the unique URLs for every speech and remark by different parties, chiefly, the President, Vice President, First Lady, Second Lady, as well as other members of the executive staff.

To use, simply get pull this repository. Then use the terminal to navigate to Shell_Command folder. 

To collect every speech, in your terminal, simply type the following:

*	$bash RUN2.sh

The rest will be automated. 

Note: This package was written on a Mac OSX system using an Anaconda version of Python. 

# Self Cleanup

Running "bash RUN2.sh" will run the entire program, collecting all speeches from 2009-2015. Once all individual speeches are run, the program executes a self-cleanup, reorganizing the files so that the result is a polished file system. 

* See Results section below.

Running other .sh functions will still execute but will not result in the overall file system cleanup. Alternate possible commands include:

* $bash 2009.sh
* $bash 2010.sh
* $bash 2011.sh
* $bash 2012.sh
* $bash 2013.sh
* $bash 2014.sh
* $bash 2015.sh
* $bash 2009-2015.sh

When "bash RUN2.sh" is executed, the above individual commands are run in sequence followed by approximately 200+ additional lines of post-code processing, which leads to the automatically generated cleaned file output as seen in the results section below.


# Results - Data

RESULTS:

The results of this output can be seen on GitHub:

* https://github.com/computingForSocialScience/cfss-homework-jmausolf/tree/master/Final_Project/White_House_Speeches

OR

* 	https://github.com/jmausolf/White_House_Speeches

NOTE: Although the GitHub repositories reflect the cleaned file system layout, GitHub truncates directories to 1,000 files. 


DATA:

If desired, all collected speech files are available for download on Dropbox:

* 	https://www.dropbox.com/sh/muru60po3ko7yk4/AADU04FgtifT2gqlVQ5qE54Pa?dl=0

An overview of these data files is available on Wix:

* 	http://jmausolf.wix.com/project---cfss#!data/cwve



# THE DETAILS - BASH LEVEL

For any given bash-level shell script, such as $bash 2011.sh, a combination of python and shell commands are executed. I divide these into the following stages:



## FIRST_STAGE - Make New Directories ##

* Make New Directories -- CSVs 
* Make New Directories -- Speeches



## SECOND_STAGE - Collect URLs ##

Run main_speechesurls.py to generate CSV's using the following. Example:
* $python __main_speech_urls_bearer.py "2011/01" "2011/12"


## THIRD_STAGE - Filter URLs ##

Create filtered CSVs for each speaker, namely, The President, Vice President, First Lady, Second Lady, and Other.

This is accomplished using:

* Filter Speech URLs using $python __main_speech_urls_filter.py 


## FOURTH_STAGE - Sort Filtered URLs ##

CSVs are Copied and/or Moved
* Move Auxiliary CSVs
* Copy All Speech CSVs to Speech Folders
* Move All CSVs to CSV folders




## FIFTH_STAGE - Parse All URLs ##

The speeches for each actor (The President, Vice President, First Lady, Second Lady, and Other) are all parsed using:

* $python __main_speech_parser.py 


## SIXTH_STAGE - Rename Bash Folders ##


Bash CSVs and Speech Folders are renamed. For example:

* mv bash_CSVs 2011_CSVs
* mv bash_Speech 2011_Speeches


# THE DETAILS - PYTHON LEVEL OVERVIEW

The python level functions can be basically broken down into three major tasks. Collecting the speech URLs, sorting the speech URLs, and parsing the speech URLs.

As described in the bash sequence, three main-level python functions are called that execute other python functions:

* GETTING SPEECH URLS: $python __main_speech_urls_bearer.py "2011/01" "2011/12"

* SORTING SPEECH URLS: $python __main_speech_urls_filter.py 

* PARSING SPEECH URLS: $python __main_speech_parser.py 


# THE DETAILS - Getting Speech URLS 

This task probably involves the most functions. In essence, I create a sequence of successive spreadsheets. First I create a list of all possible parent URLS. I use a self-made dictionary to translate requested date strings to specific lines in that parent CSV. This creates a new requested-parents CSV. For every line in the requested parents CSV, I scrape the number of pages and generate a CSV of subpages as a new CSV. For every line in the subpages CSV, I scrape all URLS and send these to a speech URLs CSV File. 

These steps are below


##1 FIRST: Getting All Parent URLS##

Generate Parent URLs CSV
* getparentURLs()

This function (and its sub-functions) generates a list of all 'parent' directories. The parent directories follow a basic pattern:

http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/YYYY/MM

This pattern is such that the URL string ends in YYYY/MM, beginning at 2009/01 and ending at the present year and month combination (future YYYY/MM result in a blank page).

Generating the parent URLs will be a multi-function process involving generating a list of URL strings with every valid permutation of YYYY/MM:

http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/2009/01 
		⋮
http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/2015/03

This is written to a CSV file of parent URLs for further use.

##2 SECOND: Getting Requested Parent URLS##

I created a function date(string) to translate a string to a specific line in the parents CSV:

* def date(string):
	"""Function to translate a date string into the 
	corresponding line item for the Parent URL CSV.
	List is indexed at 0, the header. URLs begin at 1.""" 


Then, I write a new CSV of requested parent URLS:

* def req_URLs(date1, date2):
	"""Returns the requested parent URL's for speeches and remarks in a 
	given date range. Date1 = "YYYY/MM" Date2 = "YYYY/MM"""



##3	THIRD: Scraping All "Pages" for a Given Parent URL and Making Subpages##

In the __main_speech_urls_bearer.py function, I then read the CSV of requested parent URLS.

For every requested parent URL, I invoke the function sub_pages_URLs(parent_url) in the pages.py file. 

This function does two things.

* It invokes pages(url), which """Returns the number of additional pages for a given parent URL"""

* It writes a CSV of subpages for every page found by pages(url)

Thus, for every requested parent URL, I scrape the number of pages and compile a list of X subpages, all of which write to a new subpages.csv file.


##4 FOURTH: Scraping All Speech URLS for Every Subpage##

Next, I read the number of subpages to define a loop range.

For the number of subpages in this range, I scrape the speech URL extensions and join these to the base URL for each speech. This uses the function speech_urls(subpage_url). 


Throughout this section and the others, I use various "reader" functions in the file CSVread.py. These are not very exciting functions, but prove useful for reading the many CSV's created in this package.


# THE DETAILS - Sorting Speech URLS 

Next, I sort the speech URLS for each speaker, namely, The President, Vice President, First Lady, Second Lady, and Other.

This is accomplished using:

* Filter Speech URLs using $python __main_speech_urls_filter.py 

Unlike the other __main functions, this python file only has one function filterSpeechURL(),  which is invoked in this outer .py file. 

This function runs through the speechurls.csv and creates five new speech URLs CSV's one for the President, Vice President, First Lady, Second Lady, and Other.

This occurs through a series of if, elif, and else statements which search for specific keyword strings in each URL. If this is found, that item is appended to the respective CSV. Otherwise, if there are no matches for the specific actors, the speech is put in the other CSV. In this way, all speeches are subdivided to new filtered CSV files.


# THE DETAILS - Parsing the Speech URLS

I then parse each speech URL for every speech actor. This is executed by either
*  $python __main_speech_parser.py.
OR
* $ python __main_speech_2009-2010_parser.py

Speeches 2009-2010 use the 2009-2010 speech parser. This is indicated in 2009.sh and 2010.sh. Otherwise, speeches rune on __main_speech_parser.py.

Each of these main files is set up approximately the same. For each agent, the main file first reads the respective CSV and then attempts to run a series of parsers at each URL, such as pre_WHT1(speechURL), pre_WHT2(speechURL), pre_WHT3(speechURL) or WHT1(speechURL) WHT2(speechURL), WHT3(speechURL).

For all of these files, the parsers save a unique text file. To ensure this, each parser checks for the existence of an existing file, and then if it exists, the parser picks a new name for the file.

The ideal file type follows:

"year_id+'-'+month_id+'-'+day_id+'_'ID<#>’.txt'"

Example: 2011-09-17_ID4.txt

Which would occur if 3 other speeches for that speaker had already been spoken that day. After ID5, the python function begins assigning random ID's such as 2011-09-17_ID2322_3820.

This file format works especially well after mid-2010. Prior to that, the White House's HTML is too unstable to generate a regular ID. This may require some clever series of regular expressions.





