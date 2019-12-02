import zipfile
import optparse
from threading import Thread

def extract_file(z_file, password):
	try:
		z_file.extract_all(pwd = password)
		print('[+] The password is ' + password + '\n')
	except:
		pass


def main():
	parser = optparse.OptionParser(usage = "usage: %prog [options] -f <zipfile> -d <dictionary>")
	parser.add_option('-f', dest = 'zname', type = 'string', help = 'specify zip file')
	parser.add_option('-d', dest = 'dname', type = 'string', help = 'specify dictionary file')
	(options, args) = parser.parse_args()
	if options.zname == None or options.dname == None:
		print(parser.usage)
		exit(0)
	else:
		zname = options.zname
		dname = options.dname

	z_file = zipfile.ZipFile(zname)
	passFile = open(dname)
	for line in passFile.readlines():
		password = line.strip('\n')
		t = Thread(target = extractFile, args = (z_file, password))
		t.start()


if __name__ == '__main__':
	main()