# PhFree (phfree.info)

Funded UK PhD opportunities are tough to find. PhFree makes it (pretty) quick and easy, without having to trail through ads.

## Project Summary

Our final project is a live website which scrapes 'findaphd' to return funded PhD opportunities in the UK. Both of us completed our undergraduate degrees and in the UK, and whilst we are currently graduate students in the US, we see fewer US students studying for their PhDs in the UK, possibly due to lack of knowledge of the available projects and confusion around the funding structure. The website 'findaphd' is currently the most comprehensive database for projects offered by various UK universities and supervisors, but there are a number of issues with the website. Firstly, it does not filter out funded versus unfunded opportunities; we believe in an equitable PhD process where students should be paid for their work, and only want to advertise funded opportunities. There is a small exception to this - some projects are advertised whilst still awaiting funding, but these are noted in the search results which we returned.

## Usage

### *Optional:* Update to database and recreate homepage (or not!)

Running the jupiter notebook scraping can take a bit of time. But don’t worry, we have included a recently scraped output.csv and already generated a homepage.html.

If you decide you **do** want to rebuild everything to have the most recent results, here’s what you should do:

**1. Run all chunks in scrape.ipynb (feel free to cook dinner, go for a walk, or have a nap while you wait!)**

Note: ensure you have beautifulsoup and pandas downloaded prior to starting.

```pip install beautifulsoup```

```pip install pandas```

**2. Once this is done, run generate_homepage.py**

Run the following in your terminal:

```python generate_homepage.py```

This python code will delete the old homepage.html and create a new one in its place. It should take about 20 seconds.

### Run Flask

Run the following in your terminal:

```run flask```

Have fun searching for your PhD!

## License

N/A – All data belongs to its owners.
