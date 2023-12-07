# PhFree (phfree.info)

Funded UK PhD opportunities are tough to find. PhFree makes it (pretty) quick and easy, without having to trail through ads.

## Design Summary

PhFree has 2 primary technical components.

1. Scraping and cleaning data from www.findaphd.com

2. Allowing users to search the resultant data frame in an easy and visually appealing manner

This document explains the thought process behind these two components.

## Obtaining data from www.findaphd.com

FindAPhD is not an especially well-designed website. Their div classes and entries are messy. Moreover, and despite this messiness, they have taken some steps to avoid scraping.

### scrape.ipynb

We decided to use Jupiter Notebook to help highlight and manage errors throughout the data scraping process. **beautifulsoup** is the main library we used to achieve this.

Here's a chunk-by-chunk breakdown of how it all works, and some of the decisions we made along the way:

1. Import libraries

2. Establish the URL (all funded UK PhDs) and set up **beautifulsoup**

3. Define a function to scrape data from one search results page into dictionary:

      *To achieve this, we inspected FindAPhD's html to identify the div classes for each search result ("w-100 card shadow-sm p-4") and then each characteristic.*

      *For example, supervisors were in the div class: "a.phd-result__key-info.super". In this case we had to clean some of the supervisors which started with the artefact '\xa0'.*

      *We then placed all the scraped data into a dictionary, called result_dict, and appended it to a list called data. This list became a list of dictionaries.*

4. Define a function to loop through all pages:

      *As FindAPhD only displays 15 search results at a time, we had to cycle through each of the pages for our initial search.*

      *FindAPhD has a limit on the rate at which you can make requests. We found that adding a 1 second delay between searches helped avoid triggering this limit.*

5. Find last page number so we loop through the right amount

6. Append all pages from website together in a list of thirty pages at a time (to make it more manageable)

7. Scrape the data using previously defined functions!

8. Convert the scraped data into a Pandas DataFrame and then a CSV file called **output.csv**

9. (Optional:) Inspect the dataframe

The idea is that, if this were a live website, this would be run once or twice a day before generating a new homepage. This would ensure that the website features up-to-date information.

## Setting up the search and website

In addition to incorporating bootstrap to make the more static pages (which we think look pretty good!), we figured the main other challenge would be establishing a search engine with this data.

We had several aims for this search engine:

1. To allow for searches across all parameters

2. To be responsive to user input

3. To be hidden when there is no user input


Before we got to these, however, we needed to connect whatever the latest version of our **output.csv** into our html.


### generate_homepage.py

This is the heart of the project. It uses the **os** and **pandas** libraries to delete the existing **homepage.html** and replace it with updated data from the most recent **output.csv**.

Rather than walk through every single step of the code, here is a brief summary of how it works and the decision we made along the way.

1. Delete existing **homepage.html**

2. Load up **output.csv** and configure it to be inserted into the html.

3. Specify JavaScript functions for search engine (and hide results when there is no input)

      *This is python code being used to create an html page. As such, we ran into a few errors where javascript was being misinterpreted as python code in our html below. To solve this, we established all of the javascript before hand, such that it could be inserted into the html.*

      *Crucially, to fulfil our goal of allowing to search across parameters, the search works on a concatenated version of the each search entry. This way any entered search terms would be scanned across all aspects of each item.*

4. Write html and use **os** to save it to the templates folder

## Note on contact.html

To our knowledge, php does not work very nicely in the flask environment. Consequently the contact form does not work as intended, but we believe this code would work if hosted live. However, we have not been able to test this. 
