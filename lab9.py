# This task is based on the example from the "Practical Introduction to
# Web Scraping in Python" tutorial, available at:
# https://realpython.com/python-web-scraping-practical-introduction/

# The task is to write a Python program (script) that among the
# hundred greatest mathematicians of the past
# (http://www.fabpedigree.com/james/greatmm.htm)
# finds and prints 10 currently most popular mathematicians based
# on the level of attention they are receiving by the Web users.
# The popularity is approximated by the number of page views that
# the mathematicians' Wikipedia pages have received in the last 60 days;
# these (and many other) stats about Wikipedia pages can be obtained
# from the Wikipedia’s XTools (https://xtools.wmflabs.org/).


import requests
from bs4 import BeautifulSoup
from contextlib import closing

def get_content_from_url(url):
    '''
    Returns the content of the web page with the given URL
    '''

    def response_ok(r):
        '''
        Checks the status code of the response and
        also if the response contains html content
        '''
        content_type = r.headers['Content-Type']
        return (r.status_code == 200) and \
               (content_type is not None) and \
               (content_type.find('html') >= 0)

    try:
        with closing(requests.get(url)) as resp:
            return resp.text if response_ok(resp) else None
    except requests.RequestException as req_err:
        print('The following error occured when requesting content from {}:\n{}'.format(url, req_err))
        return None


def get_mathematicians_names():
    '''
    Retrieves the web page with a list of well known mathematicians
    and returns a list of the mathematicians' names
    '''

    url = 'https://fabpedigree.com/james/greatmm.htm'
    raw_txt = get_content_from_url(url)

    if raw_txt is not None:
        soup = BeautifulSoup(raw_txt, 'html.parser')

        all_names = []
        ol_tags = soup.find_all('ol')
        for ol in ol_tags:
            a_tags = ol.find_all('a')
            names = [tag.text.strip() for tag in a_tags]
            all_names.extend(names)

        return sorted(all_names)

    # if we failed to get any data from the url
    print("Failed to collect mathematicians' names from {}".format(url))
    return list()


def get_pageview_counts(name):
    '''
    Receives the name of a mathematician (in general, of any person).
    Returns the number of hits (page views) that the
    mathematician's Wikipedia page received in the last 60 days,
    as an int value.
    '''

    url_template = 'https://xtools.wmflabs.org/articleinfo/en.wikipedia.org/{}'
    page_content = get_content_from_url(url_template.format(name))

    def a_with_latest60(tag):
        return (tag.name == 'a') and tag.has_attr('href') and (tag['href'].find('latest-60') >= 0)

    if page_content:
        soup = BeautifulSoup(page_content, 'html.parser')
        a_tag = soup.find(a_with_latest60)
        if a_tag:
            pageviews = a_tag.text.strip().replace(',', '')
            try:
                return int(pageviews)
            except ValueError as val_err:
                print('Error occured when transforming the page views count ({}) into int:\n{}'.format(pageviews, val_err))
                return None

    print('Not able to get page views for mathematician {}'.format(name))
    return None


def clean_names(names):
    """
    The function is intended for dealing with the diversity of name formats
    (e.g. Hermann G. Grassmann, Hermann K. H. Weyl, M. E. Camille Jordan),
    that is, name formats that cannot be directly used for collecting page
    view stats. The names are 'cleaned' so that they consists of only
    name and surname.
    """
    cleaned_names = []

    for name in names:
        name_parts = name.split()
        if len(name_parts) > 1:
            name_parts = [np.strip() for np in name_parts if np.strip().find('.') < 0]
            cleaned_names.append(" ".join(name_parts))
        else:
            cleaned_names.append(name)

    return cleaned_names



def find_most_popular_mathematicians():
    '''
    The function puts all parts together; namely, it
    - obtains a list of mathematicians' names
    - iterates over the list to get the number of 'hits'
    for each name
    - cleans the names that didn't get through and tries
    once again to obtain 'hits' for them
    - sorts the names by 'popularity' (hits)
    - prints top 10 based on the popularity
    - prints names for which hits could not have been pulled
    '''

    print('Putting together a list of names...')
    names = get_mathematicians_names()
    print('... done.')

    print('Getting page views for each name...\n')

    results = []
    not_found = []

    for name in names:
        pageviews = get_pageview_counts(name)
        if pageviews is not None:
            results.append((name, pageviews))
        else:
            not_found.append(name)


    cleaned_names = clean_names(not_found)
    for name in cleaned_names:
        pageviews = get_pageview_counts(name)
        if pageviews is None:
            pageviews = -1
        results.append((name, pageviews))


    print('...done.')

    results = sorted(results, key=lambda result: result[1], reverse=True)

    top_mathematicians = results[:10] if len(results) > 10 else results

    print('\nThe most popular mathematicians based on the number of page views ("hits") in last 60 days:\n')
    for index, mathematician, pageviews in enumerate(top_mathematicians):
        print('{}. {} with {} hits'.format((index + 1), mathematician, pageviews))

    no_results = [res for res in results if res[1] < 0]
    print('\nNot able to find pageviews for the following {} mathematicans:'.format(len(no_results)))
    print("\n".join([item[0] for item in no_results]))




if __name__ == '__main__':

    find_most_popular_mathematicians()

