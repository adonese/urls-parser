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
#
# Copyright (c) 2016, Mohamed Yousif
#
# Urls Parser is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General
# Public License version 3. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#

import bs4
from urllib.request import Request
import urllib
import os
import argparse
from sortedcontainers import SortedSet
from urllib.parse import urlparse
headers = { 'User-Agent' : 'Mozilla/5.0' }

parser = argparse.ArgumentParser(description='Parsing links from a website.',
                             formatter_class=argparse.ArgumentDefaultsHelpFormatter)
add_arg = parser.add_argument
add_arg('url', nargs='*')
add_arg('--html-tag', default='a', type=str, help='html tag you want to parse')    
add_arg('--unique-id', default='', type=str, help='A common string in your links')
add_arg('--output-file', default='output_file.txt', type=str, help='A file to write to when stdout is activated')
args = parser.parse_args()

parsed_url = urlparse(*args.url)
domain = '{uri.netloc}'.format(uri=parsed_url)


url = Request(*args.url, headers=headers)
bs4_data = bs4.BeautifulSoup(urllib.request.urlopen(url), "lxml")
urls_list = []


if args.html_tag == 'a':
    href = 'href'
    for tag in bs4_data.find_all(args.html_tag):
        if args.unique_id:
            if args.unique_id == str(tag):
                urls_list.append(str(tag['href']))
        else:
            urls_list.append(str(tag['href']))

else:
    for tag in bs4_data.find_all(args.html_tag):
        if args.unique_id in str(tag):
            urls_list.append(str(tag))
            
urls_set = SortedSet(urls_list)

if len(urls_set) < 4:
    print(*urls_set, sep="\n")
else:
    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), domain)):
        os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), domain))
    
    if len(os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), domain))) > 0:
        filename, extension = os.path.splitext(args.output_file)
        args.output_file = '%s_%s.%s' %(filename, len(os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), domain))) + 1, extension[1:])
    
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), domain, args.output_file), 'w') as output_file:
        output_file.writelines('%s\n' % l for l in urls_set)
