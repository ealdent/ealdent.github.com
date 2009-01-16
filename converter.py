#!/usr/bin/env python

import codecs
import feedparser
import sys
import time




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
    if entry.has_key('tags'):
        tags = [tag['term'] for tag in entry.tags if tag['term'] != u'Uncategorized']
    else:
        tags = list()
    if len(tags) == 0:
        return None
    content = entry.content[0].value
    link = "_posts/" + entry.link.split(".com")[1][1:-1].replace("/", "-") + ".html"
    original_link = "http://ealdent.wordpress.com" + entry.link.split(".com")[1]
    
    print "Processing entry:  %s" % (title)
    
    f = codecs.open(link, 'w', 'utf-8')

    f.write(u"---\n")
    f.write(u"layout: post\n")
    f.write(u"title: \"%s\"\n" % (title))
    if len(tags) > 0:
        f.write(u"tags: [%s]\n" % (', ').join(["\"%s\"" % (tag) for tag in tags]))
    else:
        print "*******************************************************************************"
    f.write(u"---\n")
    
    # replace youtube links
    idx = -1
    while True:
        idx = content.find(u"[youtube=", idx + 1)
        if idx < 0:
            break
        print "\t\tFOUND YOUTUBE"
        end_idx = content.find(u"]", idx) + 1
        if end_idx < 0:
            break
        youtube = content[idx:end_idx]
        youtube_link = youtube.split(u"youtube=")[1][:-1]
        new_youtube = u"""<div class="youtube"><object width="425" height="344"><param name="movie" value="%s=en&fs=1"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/Ni_rAamVP2s&hl=en&fs=1" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="425" height="344"></embed></object></div>""" % (youtube_link)
        content = content.replace(youtube, new_youtube)
        print "Replaced youtube for %s." % (title)
        print "**********************************************************************"
    
    # replace captions
    idx = -1
    while True:
        idx = content.find(u"[caption", idx + 1)
        if idx < 0 :
            break
        print "\t\tFOUND CAPTION"
        end_idx = content.find(u"]", idx) + 1
        if end_idx < 0:
            break
        content = content.replace(content[idx:end_idx], u" ")
        print "Replaced caption for %s." % (title)
        print "**********************************************************************"
    
    f.write(u"<hr /><br />Original post can be found at:  <a href=\"%s\" target=\"_blank\">%s</a><br /><br />\n%s\n" % (original_link, original_link, content))

    f.close()
    
    print "Finished writing new post:  %s" % (link)


# def parse_entry(entry):
#     # given an entry turn into a proper post
#     #  url => YYYY-MM-DD-slug-words-blah.html
#     #  tags => list of tags
#     #  title => title of post
#     #  content => actual post
#     title = entry.title
#     print title




def process_feed(feed):
    for entry in feed.entries:
        parse_entry(entry)



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage:  %s <feed file>" % (sys.argv[0])
        sys.exit(0)
    
    feed = load_feed(sys.argv[1])
    process_feed(feed)


