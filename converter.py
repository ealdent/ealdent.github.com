import feedparser


def load_feed(feed_filename):
    f = open(feed_filename, 'r')
    txt = f.read()
    f.close()
    
    feed = feedparser.parse(txt)
    
    return feed
    



def parse_entry(entry):
    # given an entry turn into a proper post
    #  url => YYYY-MM-DD-slug-words-blah.html
    #  tags => list of tags
    #  title => title of post
    #  content => actual post