---
layout: post
title: Jekyll and Hyde
tags:
- blagoblag
- jekyll
- wordpress
- blogging
- markdown
- git
- github
- github pages
- textile
---

I have settled on the decision of migrating my blog engine from [WordPress.com][:wordpress] (WPC) to [Jekyll][:jekyll].  There are a number of disadvantages of using WPC that have been bothering me, but the alternatives weren't much better.  One option I had was to share a slice with a couple friends running [WordPress.org][:wporg], but the tradeoff between configurability and traffic boosts weren't enough to justify it.  I'll describe Jekyll after going through some advantages and disadvantages I'm currently facing.


### Advantages of WordPress.com

+ Extra traffic driven by tags pages.
+ Basic SEO is taken care of.
+ Mostly free, with just having to pay for upgrades (domain names, custom CSS, extra storage).
+ Upgrades, maintenance, and security are not my concern.
+ Pretty sweet control panel.

<br>
### Disadvantages of WordPress.com

+ Inability to use JavaScript of any kind.
+ Can't use custom plugins or widgets.
+ Supported widgets either suck or are for websites I've never heard of.
+ Cost for things like custom CSS exceed their value.
+ Minor things like being able to use Feedburner to serve my RSS feed in a convenient, non-hackish way.
+ Not really easy to do offline editing.
+ Data is hidden away in a database I have no control over.
+ The 2.7 dashboard conflicts with some hotkeys I use for Firefox and I have deleted large swaths of text resulting in bellows of "WTF?!"

<br>
### Why WordPress.org isn't ideal

+ Written in PHP, which I know but am no longer fond of.
+ Requires semi-serious web hosting service that would have to be paid for.
+ Offline editing is still an issue.

So what do I really want in a blog engine?  I don't want a WYSIWYG editor. The only thing consistent about them is how their inconsistency annoys me.  I want good analytics.  I want complete control over _everything_.  I want it to be fast and I want it to be search-engine friendly.


### Jekyll

Jekyll is a very different sort of blog engine.  Its beauty is in its simplicity.  Instead of being a dynamic engine that hits the db whenever a request is made, the blog engine is more of a preprocessor.  You begin by creating a static file (or files) for each post.  Then you run Jekyll over it and it generates your new website as a set of static files.  Static files that require nothing more than for your webserver to serve them.

Jekyll lets you your write your posts using [Textile][:textile] or [Markdown][:markdown].  Markdown is my new favorite, and I'm using it to write this post.  Jekyll was written by one of the co-founders of [GitHub][:github], so it's open source, hosted on GitHub, and therefore is easy to fork.  And did I mention it's written in Ruby?

GitHub pages basically acts as a Jekyll blog server.  As long as you obey the conventions of Jekyll, anything you push to your GHPages repo will be Jekyllified.  Free blog service!  I can edit and store all of my posts on my own machine with a safe backup on GitHub.  The free storage that comes with it is a bit more restrictive than with WordPress.com, but that's not really an issue for me since I use very little storage anyway.  I'm not saving video or a bunch of gigantic images.

Jekyll is a great alternative for me that just works.


[:wordpress]: http://www.wordpress.com
[:jekyll]: http://mojombo.github.com/jekyll
[:wporg]: http://www.wordpress.org
[:markdown]: http://daringfireball.net/projects/markdown/
[:textile]: http://en.wikipedia.org/wiki/Textile_(markup_language)
[:github]: http://github.com