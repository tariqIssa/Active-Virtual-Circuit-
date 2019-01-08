from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink
 
  
 
def topology():
    net = Mininet( controller=RemoteController, link=TCLink, switch=OVSSwitch )
    h1 = net.addHost( 'h1', ip='10.0.0.1' )
    h2 = net.addHost( 'h2', ip='10.0.0.2' )
    h3 = net.addHost( 'h3', ip='10.0.0.3' )
    h4 = net.addHost( 'h4', ip='10.0.0.4' )
    h5 = net.addHost( 'h5', ip='10.0.0.5' )
    h6 = net.addHost( 'h6', ip='10.0.0.6' )
    h7 = net.addHost( 'h7', ip='10.0.0.7' )
    h8 = net.addHost( 'h8', ip='10.0.0.8' )
    h9 = net.addHost( 'h9', ip='10.0.0.9' )
    h10 = net.addHost( 'h10', ip='10.0.0.10' )
    h11 = net.addHost( 'h11', ip='10.0.0.11' )
    h12 = net.addHost( 'h12', ip='10.0.0.12' )
    h13 = net.addHost( 'h13', ip='10.0.0.13' )
    h14 = net.addHost( 'h14', ip='10.0.0.14' )
   


    s1 = net.addSwitch( 's1', protocols='OpenFlow13' )
    s2 = net.addSwitch( 's2', protocols='OpenFlow13' )
    s3 = net.addSwitch( 's3', protocols='OpenFlow13' )
    s4 = net.addSwitch( 's4', protocols='OpenFlow13' )
    s5 = net.addSwitch( 's5', protocols='OpenFlow13' )
    s6 = net.addSwitch( 's6', protocols='OpenFlow13' )
    s7 = net.addSwitch( 's7', protocols='OpenFlow13' )
	s8 = net.addSwitch( 's8', protocols='OpenFlow13' )
	s9 = net.addSwitch( 's9', protocols='OpenFlow13' )
    c0 = net.addController( 'c0', controller=RemoteController, ip='192.168.56.1' )
    print "*** Creating links"
 
 
    net.addLink(s1, s2, 1, 1)
	net.addLink(s1, s4, 2, 1) 
    net.addLink(s2, s3, 4, 1)
    net.addLink(s2, s5, 3, 1)
    net.addLink(s2, s4, 2, 2)
    net.addLink(s2, s6, 5, 1)
    net.addLink(s3, s6, 2, 2)
    net.addLink(s4, s7, 5, 1)
    net.addLink(s4, s5, 3, 2)
    net.addLink(s4, s8, 4, 1)
    net.addLink(s5, s6, 3, 3)
    net.addLink(s5, s8, 4, 2)
    net.addLink(s6, s9, 4, 1)
    net.addLink(s6, s8, 5, 4)
    net.addLink(s7, s8, 2, 3)
    net.addLink(s8, s9, 5, 2)
    net.addLink(s1, h1, 3, 1)
    net.addLink(s1, h2, 4, 1)
    net.addLink(s2, h3, 6, 1)
    net.addLink(s3, h4, 3, 1)
    net.addLink(s3, h5, 4, 1)
    net.addLink(s3, h6, 5, 1)
    net.addLink(s7, h7, 3, 1)
    net.addLink(s7, h8, 5, 1)
    net.addLink(s7, h9, 4, 1)
    net.addLink(s8, h10, 6, 1)
    net.addLink(s8, h11, 7, 1)
    net.addLink(s9, h12, 3, 1)
    net.addLink(s9, h13, 4, 1)
    net.addLink(s9, h14, 5, 1)
 
    print "*** Starting network"
    net.build()
    c0.start()
    s1.start( [c0] )
    s2.start( [c0] )
    s3.start( [c0] ) 
    s4.start( [c0] )
    s5.start( [c0] )
    s6.start( [c0] )
    s7.start( [c0] )
    s8.start( [c0] )
    s9.start( [c0] )
    print "*** Running CLI"
    CLI( net )
    print "*** Stopping network"
    net.stop() 
 
if __name__ == '__main__':
 
    setLogLevel( 'info' )
    topology()

