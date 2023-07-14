# Link Crawler
A simple link Crawler for web pages. basically it will filter the initial URL html page, extract all the hrefs attributes and add it to a array, after this, the process restart for each url in the array.
I implemented a "pattern" filter, allowing the user to save only the url that contains the pattern.

For now to use this script just run:

```
$ python3 crawler.py [url] "[pattern]"
```
An example for how to craw all the links that contain "example.com" at www.example.com :
```
$ python3 crawler.py www.example.com "example.com"
```

To download this script:
```
$ git clone https://github.com/Leooliveoi/Simple_Link_Crawler
```
