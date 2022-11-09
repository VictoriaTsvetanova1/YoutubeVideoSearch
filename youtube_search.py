#!/usr/bin/env python3

import webbrowser

quary = input("Enter username: ")

url = "https://www.youtube.com/results?search_query=" + str(quary)

webbrowser.open(url)
