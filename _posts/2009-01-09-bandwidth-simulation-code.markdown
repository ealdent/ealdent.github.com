# Bandwidth Simulation Python Code

This code accompanies [this post][:bwsim-post] on [my blog][:mendicantbug].

{% highlight python %}
#!/usr/bin/env python

# Bandwidth Simulator

import sys
import numpy


class Download(object):
    
    def __init__(self, size):
        self.size = size
        self.size_left = size
        self.elapsed = 0.0
        
    
    def decrement(self, bytes):
        if bytes > self.size_left:
            self.elapsed += self.size_left / float(bytes)
            self.size_left = 0.0
        else:
            self.elapsed += 1.0
            self.size_left = self.size_left - bytes
        
        
    def __repr__(self):
        return "Download(%d of %d):  %d s" % (self.size_left, self.size, self.elapsed)
        
        
    def average_speed(self):
        if self.elapsed > 0.0:
            return (self.size - self.size_left) / self.elapsed
        else:
            return 0.0
            
            
class SurfingDownload(Download):
    def __init__(self):
        Download.__init__(self, 75000.0 + numpy.random.uniform(0, 50000))
        # print "Generated %s." % (str(self))


class BigDownload(Download):
    def __init__(self):
        Download.__init__(self, numpy.random.uniform(0, 10) * 1024.0 * 1024.0)
        # print "Generated %s." % (str(self))
        


class WebSurfer(object):
    
    def __init__(self):
        """Create a random web surfer with various surfing habits.
        """
        self.prob_download = numpy.random.uniform(0, 5) / 28800.0     # 0 - 5 / work day
        self.prob_surfing = numpy.random.uniform(0, 200) / 3600.0     # 0 - 200 / hour
        
    
    def act(self):
        """Generate a download or do nothing.
        """
        chance = numpy.random.uniform(0, 1)
        if chance < self.prob_download:
            return BigDownload()
        elif chance < self.prob_surfing:
            return SurfingDownload()
        else:
            return None
        

    
class Scheduler(object):
    
    def __init__(self, users, max_bandwidth):
        self.users              = users
        self.max_bandwidth      = max_bandwidth
        
        self.download_queue     = list()
        self.done_queue         = list()
        self.total_downloads    = 0
        

    def simulate(self, timespan=100):
        for i in xrange(timespan):
            self.single_step()
            if i + 1 % 1000 == 0:
                print "%d seconds have elapsed." % (i + 1)
        
    
    def single_step(self):
        new_download_queue = list()
        if len(self.download_queue) > 0:
            bandwidth_available = self.max_bandwidth / len(self.download_queue)
        else:
            bandwidth_available = self.max_bandwidth
        
        for download in self.download_queue:
            download.decrement(bandwidth_available)
            if download.size_left > 0:
                new_download_queue.append(download)
            else:
                self.done_queue.append(download)
        
        self.download_queue = new_download_queue
        
        # generate new items
        for user in self.users:
            new_download = user.act()
            if new_download is not None:
                self.total_downloads += 1
                self.download_queue.append(new_download)
                
    
    def summarize(self):
        averages = list()
        sizes = list()
        for download in self.done_queue:
            averages.append(download.average_speed() / 1024.0)
            sizes.append(download.size)
        
        print "  Total downloads completed:  %d" % (len(averages))
        print "       Incomplete downlaods:  %d" % (self.total_downloads - len(averages))
        print "          Average file size:  %.3f" % (sum(sizes) / float(len(sizes)))
        avgds = sum(averages) / float(len(averages))
        print "     Average download speed:  %.3f" % (avgds)
        print "Percentage of max bandwidth:  %.3f%%" % (100.0 * avgds / (self.max_bandwidth / 1024.0))



if __name__ == '__main__':
    if len(sys.argv) < 4:
        print "Usage:  %s <# users> <timespan> <max bandwidth in KB>"
        sys.exit(0)
    num_users       = int(sys.argv[1])
    total_time      = int(sys.argv[2])
    max_bandwidth   = int(sys.argv[3]) * 1024
        
    users = list()
    for i in xrange(num_users):
        users.append(WebSurfer())
    
    s = Scheduler(users, max_bandwidth)
    s.simulate(total_time)
    s.summarize()

{% endhighlight %}

This code is distributed under the ![BSD license](http://creativecommons.org/licenses/BSD/ "BSD license") [BSD license][:bsd].

[:bwsim-post]: http://mendicantbug.com/2009/01/06/bandwidth-simulation/
[:mendicantbug]: http://mendicantbug.com
[:bsd]: http://creativecommons.org/licenses/BSD/