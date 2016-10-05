#!/usr/bin/env python
"""
use lxml xpath to resolve xml or html file
"""
from lxml import etree


def main():
    books = etree.parse('books.xml')
    print(books)
    all = books.xpath(r'/bookstore/book[price>35]/title/node()')
    for elem in all:
        print(elem)


if __name__ == '__main__':
    main()
