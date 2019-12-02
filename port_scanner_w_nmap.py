"""
	Haven't full tested this, might include some run-time errors
	Will fix it
"""

import nmap
import optparse


def nmapScan(targetHost, targetPort):
	nmScan = nmap.PortScanner()
	nmScan.scan(targetHost, targetPort)
	state = nmScan['targetHost']['tcp'][int(targetPort)]['state']
	print('[*]' + targetHost + ' tcp/' + targetPort + " " + state)


def main():
	parser = optparse.OptionParser(usage = 'usage: %prog -H <target host> -p <target port>')
	parser.add_option('-H', dest = 'targetHost', type = 'string', help = 'specify target host')
	parser.add_option('-p', dest = 'targetPort', type = 'string', help = 'specify target port(s) seperated by a comma')
	(options, args) = parser.parse_args()
	targetHost = options.targetHost
	targetPort = str(options.targetPort).split(', ')
	if targetHost == None or targetPort == None:
		print(parser.usage)
		exit(0)
	for tgtPort in targetPort:
		nmapScan(targetHost, targetPort)


if __name__ == '__main__':
	main()


