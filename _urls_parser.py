#!/usr/bin/env python3
"""
-----
|   |
-----    -----   
|        |   |   |^^^^^   ^^^^    _____
|        |   |   |       ^       |
         -----~  |        ^^^^   |_____
                              ^  |
                         ^^^^^   |_____
                        """

"""
Created on Sat Nov  5 19:52:08 2016

@author: adonese
"""

import bs4
from urllib.request import Request
import urllib
import os
import argparse
from sortedcontainers import SortedSet
from urllib.parse import urlparse
headers = { 'User-Agent' : 'Mozilla/5.0' }


"""
$ python urls_parser.py YOUR_WEBSITE
# With optional arguments as follows:
    --html-tag: The default is the `a' html tag, however you may use any valid html.
    {a, p, h1s, div, etc}
    --output-file I highly suggest to name it with a name that you'll remember
    --unique-id: Pattern in your links. It's almost always the case that links 
                have something common like a pattern or so. I cannot do that 
                for you. You have to extract the pattern manually. 
Usage: I typically use it to extract hrefs from a website to basically
download them with youtube-dl, or wget, etc.

input:
    (str) url: address of the website you want to parse.
    (str) html_tag: Do you want to parse the whole website, or you just want to extract hrefs only?
    (str) output_file: the name of the output file you want to save your 
    results in. Generally we will make a new directory based on your provided
    url and we will save the parsed results there with an absolutely 
    descriptive name-output_file! LOL!
    (str) unique_identifier: It's very tricky. There are huge number of 
    hrefs in a single website page. But it's generally the case that you 
    are interested in a few of them. Because it's hard to make assumptions of 
    what would that identifier be, I suggest you to leave it blank, and then
    re-do the process by providing the unique_identifier from what you inferred
    from the downloaded links.

Output:
    You can either output it to the stdin, or stdout 
    (command line, or a file). If you didn't specify anything, we will see
    if the number of parsed urls is above a threshold (4) we will output it
    to a file, else to stdin.
"""

parser = argparse.ArgumentParser(description='Parsing links from a website.',
                             formatter_class=argparse.ArgumentDefaultsHelpFormatter)
add_arg = parser.add_argument
add_arg('url', nargs='*')
add_arg('--html-tag', default='a', type=str, help='html tag you want to parse')    
add_arg('--unique-id', default='', type=str, help='A common string in your links')
add_arg('--output-file', default='output_file.txt', type=str, help='A file to write to when stdout is activated')
args = parser.parse_args()




url = Request(*args.url, headers=headers)
bs4_data = bs4.BeautifulSoup(urllib.request.urlopen(url), "lxml")
urls_list = []

parsed_url = urlparse(*args.url)
domain = '{uri.netloc}'.format(uri=parsed_url)

if args.html_tag == 'a':
    href = 'href'
    for tag in bs4_data.find_all(args.html_tag):
        if args.unique_identifier and args.unique_identifier in str(tag):
            urls_list.append(tag[href])
else:
    for tag in bs4_data.find_all(args.html_tag):
        if args.unique_identifier in str(tag):
            urls_list.append(tag)

# We need to make sure there are no duplicate links, and I really hate to loose
# the order of them by using just Python's set.
urls_set = SortedSet(urls_list)
print(len(urls_list))
#if len(urls_set) < 3:
#    print(*urls_set, sep='\n')
#else:
#    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), domain)):
#        os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), domain))
#    
#    if len(os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), domain))) > 0:
#        filename, extension = os.path.splitext(args.output_file)
#        args.output_file = '%s_%s.%s' %(filename, len(os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), domain, args.output_file)) + 1, extension))
#    
#    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), domain, args.output_file), 'w') as output_file:
#        output_file.writelines('%s\n' % l for l in urls_set)
