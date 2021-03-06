from __future__ import print_function
import Pyro4
import chainTopology

@Pyro4.expose

this = "2"
next = "3"

servername = "example.chainTopology." + this

daemon = Pyro4.core.Daemon()
obj = chainTopology.Chain(this, next)
uri = daemon.register(obj)
ns = Pyro4.locateNS()
ns.register(servername, uri)

#进入服务循环
print("server_%s started" % this)
daemon.requestLoop()