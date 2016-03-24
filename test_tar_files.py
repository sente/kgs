import time
import requests
import sys
import glob

r = requests

infiles = glob.glob('out/*/tars.txt')


def load_data_to_search():
    tars = []
    for fpath in infiles:
        f = open(fpath,'r')
        tars.extend([x.strip() for x in f.readlines() if x])

    pairs = [x.strip() for x in open('out/stim728/tars.dat','r').readlines()]
    pairs = [x.split('\t') for x in pairs]

    urls = [p[1] for p in pairs]

    print len(tars)
    res = set(tars) - set(urls)
    print len(list(res))

    return list(sorted(list(res)))






def process_file(infile, ofile):

    infilepath = infile
    ofilepath = ofile

    tars = [a.strip() for a in open(infilepath).readlines()]

    ofile = open(ofilepath,'r').lines

    ofile = open(ofilepath,'a')

    for t in tars:
        resp = r.head(t)
        results.append(resp)
        ofile.write('%s\t%s\n' % (resp.status_code, resp.request.url))
        sys.stdout.write('%s\t%s\n' % (resp.status_code, resp.request.url))
        time.sleep(20)


    #[(r.status_code, r.request.url) for r in results]

def main():
    pass

if __name__ == '__main__':
    main()

    tars = load_data_to_search()

    for t in tars:
        resp = r.head(t)
        with open('out/stim728/tars.dat','a') as ofile:
            ofile.write('%s\t%s\n' % (resp.status_code, resp.request.url))
            sys.stdout.write('%s\t%s\n' % (resp.status_code, resp.request.url))
            time.sleep(20)


