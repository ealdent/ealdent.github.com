#!/usr/bin/env python


import time
import feedparser
import sys




def load_feed(feed_filename):
    print "Loading feed %s." % (feed_filename)
    f = open(feed_filename, 'r')
    txt = f.read()
    f.close()
    
    print "Parsing feed..."
    feed = feedparser.parse(txt)
    
    return feed
    



def parse_entry(entry):
    # given an entry turn into a proper post
    #  url => YYYY-MM-DD-slug-words-blah.html
    #  tags => list of tags
    #  title => title of post
    #  content => actual post
    title = entry.title
    # post_date = time.strptime(entry.wp_post_date, "%Y-%m-%d %H:%M:%S")
    tags = [tag['term'] for tag in entry.tags if tag['term'] != u'Uncategorized']
    content = entry.content[0].value
    link = "_posts/" + entry.link.split(".com")[1][1:].replace("/", "-")
    
    print "Processing entry:  %s" % (title)
    
    f = open(link, 'w')

    f.write(u"---\n")
    f.write(u"layout: post\n")
    f.write(u"title: %s\n" % (title))
    f.write(u"tags:\n")
    for tag in tags:
        f.write(u"- %s\n" % (tag))
    f.write(u"---\n")
    f.write(content)

    f.close()
    
    print "Finished writing new post:  %s" % (link)




def process_feed(feed):
    for entry in feed.entries:
        parse_entry(entry)



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage:  %s <feed file>" % (sys.argv[0])
        sys.exit(0)
    
    feed = load_feed(sys.argv[1])
    process_feed(feed)


