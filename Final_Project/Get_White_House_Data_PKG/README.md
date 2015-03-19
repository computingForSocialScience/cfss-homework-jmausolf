# Welcome to the README for Get-White-House-Data PKG

# Overview

This package utilizes both Python and Shell scripts to create a unique text file for every speech and remark from the White House:

https://www.whitehouse.gov/briefing-room/speeches-and-remarks

This generates, logs, and sorts the unique URLs for every speech and remark by different parties, chiefly, the President, Vice President, First Lady, Second Lady, as well as other members of the executive staff.

To use, simply get pull this repository. Then use the terminal to naviage to Shell_Command folder. 

To collect every speech, in your terminal, simply type the following:

*	$bash RUN2.sh

The rest will be automated. 

Note: This package was written on a Mac OSX system using an Anaconda version of Python. 

# Self Cleanup

Running "bash RUN2.sh" will run the entire program, collecting all speeches from 2009-2015. Once all individual speeches are run, the program executes a self cleanup, reorganizing the files so that the result is a polished file system. 

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

* Run main_speechesurls.py to generate CSV's using the following. Example:
* $python __main_speech_urls_bearer.py "2011/01" "2011/12"


## THIRD_STAGE - Filter URLs ##

* Filter Speech URLs using $python __main_speech_urls_filter.py 

This creates the filtered CSVs for each speaker, The President, Vice President, First Lady, Second Lady, and Other

## FOURTH_STAGE - Sort Filtered URLs ##


* Move Auxiliary CSVs
* Copy All Speech CSVs to Speech Folders
* Move All CSVs




## FIFTH_STAGE - Parse All URLs ##

The speeches for each actor (The President, Vice President, First Lady, Second Lady, and Other) are all parsed using:

* $python __main_speech_parser.py 


## SIXTH_STAGE - Rename Bash Folders ##


* Bash CSVs and Speech Folders are renamed. For example:

mv bash_CSVs 2011_CSVs
mv bash_Speech 2011_Speeches

