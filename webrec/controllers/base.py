
from cement import Controller, ex
from cement.utils.version import get_version_banner
from ..core.version import get_version
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pdfkit

url = "https://libreboot.org/docs"
url2 = "https://vuetifyjs.com/en/"
url3 = "https://nodejs.org/en/docs/"
url4 = "https://docs.microsoft.com/en-us/dotnet/csharp/"
VERSION_BANNER = """
Webpage to PDF %s
%s
""" % (get_version(), get_version_banner())


class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'Webpage to PDF'

        # text displayed at the bottom of --help output
        epilog = 'Usage: webrec command1 --foo bar'

        # controller level arguments. ex: 'webrec --version'
        arguments = [
            ### add a version banner
            ( [ '-v', '--version' ],
              { 'action'  : 'version',
                'version' : VERSION_BANNER } ),
        ]


    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()


    @ex(
        help='example sub command1',

        # sub-command level arguments. ex: 'webrec command1 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            ( [ '-f', '--foo' ],
              { 'help' : 'notorious foo option',
                'action'  : 'store',
                'dest' : 'foo' } ),
        ],
    )
    def printUrl(self):
        pdfkit.from_url(url, 'out.pdf')
        # self.app.render(data, 'command1.jinja2')
    
    def printFromRoute(self):
        def printContent(url):
            req = Request(url, headers={'User-Agent': 'chrome/79'})
            html = urlopen(req).read()
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all('a', href=True)
            print(links) #will be used for testing instead of pdfkit
            for link in links :
                print(link["href"])
                if True : #figure out what a valid link and think of a way to prevent duplicates
                    printContent( url + link["href"] )
            return True
        
            
        self.app.render(data, 'command1.jinja2')
