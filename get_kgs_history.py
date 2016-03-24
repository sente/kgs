import sys
import lxml
import lxml.html
import urlparse
import os
import time

def get_months_for_user(user):

    root = lxml.html.parse('http://www.gokgs.com/gameArchives.jsp?oldAccounts=t&user=%s' % user).getroot()

    root.make_links_absolute()

    [p.text_content() for p in root.xpath('//*[(((count(preceding-sibling::*) + 1) = 6) and parent::*)]//a')]

    links = []
    tars = []

    for link in root.xpath('//td/a'):
        weblink = link.get('href','') 

        parsed = dict(urlparse.parse_qsl(weblink))
        month = parsed['month']
        year = parsed['year']

        tarlink = "https://www.gokgs.com/servlet/archives/en_US/%s-all-%s-%s.tar.gz" % (user, year, month)
        print weblink
        print tarlink

        links.append(weblink)
        tars.append(tarlink)

    return (links, tars)


if __name__ == '__main__':
    user = sys.argv[1]
    links, tars = get_months_for_user(user)

    if (not links) or (not tars):
        print "problem downloading history"
        sys.exit(1)

    if not os.path.isdir('out'):
        os.mkdir('out')

    if not os.path.isdir('out/%s' % user):
        os.mkdir('out/%s' % user)

    open('out/%s/links.txt' % user, 'w').write('\n'.join(links))
    open('out/%s/tars.txt' % user, 'w').write('\n'.join(tars))

    print '\n'.join(links)
    print '\n'.join(tars)

