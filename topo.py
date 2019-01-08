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
    s1 = net.addSwitch( 's1', protocols='OpenFlow13' )
    s2 = net.addSwitch( 's2', protocols='OpenFlow13' )
    s3 = net.addSwitch( 's3', protocols='OpenFlow13' )
    s4 = net.addSwitch( 's4', protocols='OpenFlow13' )
    s5 = net.addSwitch( 's5', protocols='OpenFlow13' )
    s6 = net.addSwitch( 's6', protocols='OpenFlow13' )
    s7 = net.addSwitch( 's7', protocols='OpenFlow13' )
    c0 = net.addController( 'c0', controller=RemoteController, ip='192.168.56.1' )
    print "*** Creating links"


    net.addLink(s1, s2, 1, 1, bw=150)
    net.addLink(s1, s3, 2, 1, bw=200)
    net.addLink(s2, s3, 2, 2, bw=100)
    net.addLink(s2, s4, 3, 1, bw=60)
    net.addLink(s2, s5, 4, 1, bw=70)
    net.addLink(s3, s6, 3, 1, bw=80)
    net.addLink(s3, s7, 4, 1, bw=90)
    net.addLink(s4, s5, 2, 2, bw=10)
    net.addLink(s5, s6, 3, 2, bw=20)
    net.addLink(s6, s7, 3, 2, bw=30)


    net.addLink(s4, h1, 3, 1)
    net.addLink(s4, h2, 4, 1)
    net.addLink(s4, h3, 5, 1)
    net.addLink(s5, h4, 4, 1)
    net.addLink(s5, h5, 5, 1)
    net.addLink(s6, h6, 4, 1)
    net.addLink(s7, h7, 3, 1)
    net.addLink(s7, h8, 4, 1)
    net.addLink(s7, h9, 5, 1)

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
    print "*** Running CLI"
    CLI( net )
    print "*** Stopping network"
    net.stop() 

if __name__ == '__main__':

    setLogLevel( 'info' )
    topology()

