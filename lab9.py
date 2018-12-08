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
from sys import stderr


def get_content_from_url(url):
    '''
    Returns the content of the web page with the given URL
    '''

    def response_ok(response):
        resp_content_type = response.headers['Content-Type']
        return (response.status_code == 200) and \
               (resp_content_type is not None) and \
               (resp_content_type.find('html') >= 0)

    try:
        with closing(requests.get(url)) as resp:
            return resp.text if response_ok(resp) else None
    except requests.RequestException as exc:
        stderr.write("Error when trying to pull content from {}:\n{}".format(url, exc))
        return None



def get_mathematicians_names(url):
    '''
    Retrieves the web page with a list of well known mathematicians
    and returns a list of the mathematicians' names
    '''

    names = []
    page_content = get_content_from_url(url)

    if page_content:
        page_soup = BeautifulSoup(page_content, 'html.parser')
        ol_tags = page_soup.find_all('ol')
        for ol_item in ol_tags:
            a_tags = ol_item.find_all('a')
            a_text = [a_tag.text.strip() for a_tag in a_tags]
            names.extend(a_text)

    else:
        stderr.write("Failed to retrieve a list of mathematicians from {}".format(url))

    return names



def get_pageview_counts(name):
    '''
    Receives the name of a mathematician (or, in general, of any person).
    Returns the number of hits (page views) that the
    mathematician's Wikipedia page received in the last 60 days,
    as an int value.
    '''

    def last_60_days_tag(tag):
        return (tag.name == 'a') and tag.has_attr('href') and (tag['href'].find('latest-60') > 0)

    url = "https://xtools.wmflabs.org/articleinfo/en.wikipedia.org/{}".format(name)
    stats_page = get_content_from_url(url)

    if stats_page:
        page_soup = BeautifulSoup(stats_page, 'html.parser')
        last_60_days_views = page_soup.find(last_60_days_tag)
        if last_60_days_views:
            views_count = last_60_days_views.text.strip().replace(",","")
            try:
                return int(views_count)
            except ValueError as val_err:
                stderr("Error occurred when trying to parse page views ({}) "
                       "into an int:\n{}".format(views_count, val_err))
                return None

    stderr.write("Could not retrieve stats for mathematician {}\n".format(name))
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
        name_parts = [n_part for n_part in name.split() if '.' not in n_part]
        cleaned_names.append(" ".join(name_parts))

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
    mathematicians_url = 'http://www.fabpedigree.com/james/greatmm.htm'
    mathematicians_names = get_mathematicians_names(mathematicians_url)
    print('...done')

    print('Collecting page views stats for each mathematician from the list...')
    names_views_list = []
    no_results = []
    for name in mathematicians_names:
        page_views = get_pageview_counts(name)
        if page_views:
            names_views_list.append((name, page_views))
        else:
            no_results.append(name)

    cleaned_names = clean_names(no_results)
    no_results = []
    for name in cleaned_names:
        page_views = get_pageview_counts(name)
        if page_views:
            names_views_list.append((name, page_views))
        else:
            no_results.append(name)
    print('...done')

    names_views_list = sorted(names_views_list, key=lambda item: item[1], reverse=True)
    top_10 = names_views_list[:10] if len(names_views_list) > 10 else names_views_list

    print("Top mathematicians based on the Wikipedia page views")
    for num, mathematician in enumerate(top_10):
        print("{}. {} with {} page views".format((num+1), *mathematician))

    print()
    print("Could not find page view stats for the following {} mathematicians:".format(len(no_results)))
    print(", ".join(no_results))




if __name__ == '__main__':

    find_most_popular_mathematicians()

