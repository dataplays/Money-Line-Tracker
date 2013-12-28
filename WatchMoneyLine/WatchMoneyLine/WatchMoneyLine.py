import urllib2
from BeautifulSoup import BeautifulSoup
import string
import gzip

try:
    from io import BytesIO as _StringIO
except ImportError:
    try:
        from cStringIO import StringIO as _StringIO
    except ImportError:
        from StringIO import StringIO as _StringIO

#Grab the opening moneylines for NHL Games
def getOpeningLines():
    opener = urllib2.build_opener()
    response = opener.open ("http://www.vegasinsider.com/nhl/odds/las-vegas/")
    if response.info().get( 'Content-Encoding' ) == 'gzip':
        f = gzip.GzipFile( fileobj=_StringIO( response.read() ))
        page = f.read()
    else:
        print "Page wasn't coded with expected Content Encoding.  Ending execution."
        pass
    
    soup = BeautifulSoup( page )

    mainTable = soup.findChild( 'td', { "class" : "viBodyBorderNorm" })
    tables = mainTable.findAll( 'table' )

    oddsTable = tables[ 1 ]

    rows = oddsTable.findAll( 'tr' )

    for aRow in rows:
        teams = aRow.findChildren( 'a', { "class" : "tabletext" })
        print teams


getOpeningLines()

