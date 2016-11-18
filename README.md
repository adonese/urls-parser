urls-parser
===========

## urls-parser

I use this script to parse a website when I need to download several links without doing that manually. I was kinda lazy of generalizing this tool, so I always end up modifying the script, or even worse I write it from the beginning.

As I mentioned, I use to extract links from a website, but you can literally extract any kind of valid html tag. Why? You never know..

## How to use it

The simplest case is

```shell

$ python urls_parser.py website
# The website can be just a single, or it can also be a list of websites e.g.
$ python url_parser.py wwww.foo1.com www.foo2.com
# If you didn't specify any type of html tag, by default we will use the `a`. If, however, you
# want to specify one, you can simply do that by
$ python urls_parser.py website --html-tag p
# In that case it will download whole p tags
```
The results can either be stored into a file in you current directory, with the name of your website. If the results, the parsed links for instance, are less than 4, we will output them to stdin, else we will save them to a file with a default name of `output_file.txt` very informative name, I know :P

You can, and I encourage you to, specify a name of the output_file, using

```shell

$ python urls_parser.py website --output_file my_file.txt
# Where `my_file.txt` is the name of the file you want to store the results in.
```

## Installation

urls_parse has only two dependencies BeautifulSoup and sortedcontainers

After you have downloaded this file, using

```bash

$ git clone https://github.com/adonese/urls-parser.git
# go to urls-parser directory
$ cd urls-parser
# Then download the requirements using pip
$ pip install -r requirements.txt
# After that you are ready to go
# If you find it helpful you may want to alias it, and add it to your path
```

## Contribution

You are very welcome to contribute to this tool, fork it, refactor the code you name it.

## License

It is a free software you can redistribute it, modify it, etc.
