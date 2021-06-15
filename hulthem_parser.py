from yattag import Doc
from yattag import indent
import regex

# Create the HTML Doc
doc, tag, text = Doc().tagtext()
doc.asis('<!DOCTYPE html>')
contents = []

# Create the data
hulthem_data = []
with open( 'cdrom_contents/DOCS/DOCUMENT.DOC', 'r', encoding='cp850' ) as doc_file:
    # Last line is empty.
    ididx=0
    for line in doc_file.read().split( '\n' )[0:-1]:
        # Checked: between label and line it's alway ' = '.
        hulthem_data.append( { 'handle': line[0:3], 'line': line[6:], 'ididx': 'DOCUMENT.DOC:L{}'.format( ididx ) } )
        ididx += 1

# Create the reference data
ref_data = []
with open( 'cdrom_contents/DOCS/LITDOC.DOC', 'r', encoding='cp850' ) as ref_file:
    # Last line is empty.
    ref_data_text = ref_file.read()
ref_data_text = regex.sub( r'TIT = ', '', ref_data_text )
ref_data = ref_data_text.split( 'REF = ' )
ref_data = [ ref.strip().split('\n') for ref in ref_data ]

# Define often used regexs
re_hulthem_nr = regex.compile( r'\>(\d+.*)\<' )
re_lit_ref = regex.compile( r'LITERATURE="L(\d+)"' )
re_par_ref = regex.compile( r'PERSON="P(\d+)"' )
re_afb = regex.compile( r'HELP="(.*)".*\$HELPID,(.*) ></A></U>' )

# Define inline tag transformations
def html_5_tags( text ):
    text = regex.sub( r'\<(/?)I\>', r'<\1i>', text )
    text = regex.sub( r'\<(/?)B\>', r'<\1b>', text )
    return text

# Boilerplates for handlers
def label_boilerplate( options ):
    with tag( 'div', klass='column_left' ):
        with tag( 'span', klass='label' ):
            doc.asis( '{}:&nbsp;'.format( options['label'] ) )

def span_boilerplate( ididx, line, options ):
    with tag( 'span', klass=options['method'].__name__, prov=ididx ):
        doc.asis( html_5_tags( line ) )

# Define handlers

def nr( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            with tag( 'span', klass=options['method'].__name__, prov=ididx ):
                hulthem_nummer = re_hulthem_nr.search( line ).groups()[0]
                contents.append( [ hulthem_nummer ] )
                doc.asis( '{}&nbsp;'.format( hulthem_nummer ) )
            item = next( data_iter )
            if( item['handle']=='PL.' ):
                with tag( 'span', klass='pl', prov=item['ididx']):
                    contents[-1].append( item['line'] )
                    text( '({})'.format( item['line'] ) )
            else:
                return item

def afb_ref_handler( line ):
    matches = re_afb.search( line ).groups()
    return ( matches[0], matches[1] )

def afb( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        src, ref = afb_ref_handler( line )
        with tag( 'div', klass=options['method'].__name__, prov=ididx ):
            with tag( 'span', klass='afb_caption' ):
                text( ref )
            doc.stag( 'img', src='/images/{}.png'.format( src ), alt=ref, title=ref )
    return next( data_iter )

def ops( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            contents[-1].append( line )
            span_boilerplate( ididx, line, options )
            item = next( data_iter )
            if( item['handle']=='OPS' ):
                span_boilerplate( item['ididx'], item['line'], options )
            else:
                return item

def inc( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            span_boilerplate( ididx, line, options )
            item = next( data_iter )
            while( item['handle']=='IN2' ):
                span_boilerplate( item['ididx'], item['line'], options )
                item = next( data_iter )
            return item

def exp( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            span_boilerplate( ididx, line, options )
            item = next( data_iter )
            while( regex.match( r'EX[23]', item['handle'] ) ):
                span_boilerplate( item['ididx'], item['line'], options )
                item = next( data_iter )
            return item

def afr( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            span_boilerplate( ididx, line, options )
            item = next( data_iter )
            while( item['handle']=='AFR' ):
                span_boilerplate( item['ididx'], item['line'], options )
                item = next( data_iter )
            return item

def sam( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            span_boilerplate( ididx, line, options )

def sec( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            span_boilerplate( ididx, line, options )

def par( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            span_boilerplate( ididx, line, options )

def dsh( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            span_boilerplate( ididx, line, options )

def nam( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            span_boilerplate( ididx, line, options )
            item = next( data_iter )
            while( item['handle']=='NAM' ):
                span_boilerplate( item['ididx'], item['line'], options )
                item = next( data_iter )
            return item

def aut( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            span_boilerplate( ididx, line, options )
            item = next( data_iter )
            while( item['handle']=='AUT' ):
                span_boilerplate( item['ididx'], item['line'], options )
                item = next( data_iter )
            return item

def srt( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            span_boilerplate( ididx, line, options )

def vrm( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            span_boilerplate( ididx, line, options )

def lng( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            span_boilerplate( ididx, line, options )

def ain( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            span_boilerplate( ididx, line, options )

def pet( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            lines = [ line ]
            ididxs = [ ididx ]
            item = next( data_iter )
            while( item['handle']=='PET' ):
                lines.append( item['line'] )
                ididxs.append( item['ididx'] )
                item = next( data_iter )
            span_boilerplate( ','.join( [ str(ididx) for ididx in ididxs ] ), '; '.join( lines ), options )
            return item

def ref_handler( line ):
    ref = int( re_lit_ref.search( line ).groups()[0] )
    ref = ref_data[ref]
    cite = line.split( '$LITERATUREID,' )[-1][:-9]
    return ( ref, cite )

def elt( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            with tag( 'div', klass='editie' ):
                ref, cite = ref_handler( line )
                with tag( 'span', prov=ididx ):
                    text( cite )
                item = next( data_iter )
                if( item['handle']=='EPS' ):
                    with tag( 'span', prov=item['ididx'] ):
                        doc.asis( ',&nbsp;{}'.format( item['line'] ) )
                    item = next( data_iter )
                with tag( 'div', klass='ref' ):
                    with tag( 'span', klass='ref' ):
                        text( ref[0] )
                    with tag( 'span', klass='title' ):
                        doc.asis( html_5_tags( ref[1] ) )
            while( item['handle']=='ELT' ):
                with tag( 'div', klass='editie' ):
                    ref, cite = ref_handler( item['line'] )
                    with tag( 'span', prov=item['ididx'] ):
                        text( cite )
                    item = next( data_iter )
                    if( item['handle']=='EPS' ):
                        with tag( 'span', prov=item['ididx'] ):
                            doc.asis( ',&nbsp;{}'.format( item['line'] ) )
                        item = next( data_iter )
                    with tag( 'div', klass='ref' ):
                        with tag( 'span', klass='ref' ):
                            text( ref[0] )
                        with tag( 'span', klass='title' ):
                            doc.asis( html_5_tags( ref[1] ) )
    return item

def slt( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            with tag( 'div', klass='secundaire_lit' ):
                ref, cite = ref_handler( line )
                with tag( 'span', prov=ididx ):
                    text( cite )
                item = next( data_iter )
                while( item['handle']=='SPS' ):
                    with tag( 'span', prov=item['ididx'] ):
                        doc.asis( ',&nbsp;{}'.format( item['line'] ) )
                    item = next( data_iter )
                with tag( 'div', klass='ref' ):
                    with tag( 'span', klass='ref' ):
                        text( ref[0] )
                    with tag( 'span', klass='title' ):
                        doc.asis( html_5_tags( ref[1] ) )
            while( item['handle']=='SLT' ):
                with tag( 'div', klass='secundaire_lit' ):
                    ref, cite = ref_handler( item['line'] )
                    with tag( 'span', prov=item['ididx'] ):
                        text( cite )
                    item = next( data_iter )
                    if( item['handle']=='SPS' ):
                        with tag( 'span', prov=item['ididx'] ):
                            doc.asis( ',&nbsp;{}'.format( item['line'] ) )
                        item = next( data_iter )
                    with tag( 'div', klass='ref' ):
                        with tag( 'span', klass='ref' ):
                            text( ref[0] )
                        with tag( 'span', klass='title' ):
                            doc.asis( html_5_tags( ref[1] ) )
    return item

def parallel_handler( line ):
    ref = [ int( re_par_ref.search( line ).groups()[0] ), '0' ] # just to simulate for now!
    # ref = ref_data[ref]
    cite = line.split( '$PERSONID,' )[-1][:-9]
    return ( ref, cite )

def vss( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ) ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            with tag( 'div', klass='parallel_variant', prov=ididx ):
                with tag( 'span', klass=options['method'].__name__ ):
                    text( line )
                item = next( data_iter ) #PMS
                ref, cite = parallel_handler( item['line'] )
                with tag( 'span', prov=item['ididx'] ):
                    text( cite )
                with tag( 'div', klass='ref' ):
                    with tag( 'span', klass='ref' ):
                        text( ref[0] )
                    with tag( 'span', klass='title' ):
                        # doc.asis( html_5_tags( ref[1] ) )
                        doc.asis( '({})'.format( ref[0] ) )
                item = next( data_iter ) #DAT
                with tag( 'span', prov=item['ididx'] ):
                    doc.asis( '&nbsp;{}'.format( item['line'] ) )
                item = next( data_iter )
                with tag( 'span', prov=item['ididx'] ): #POS
                    doc.asis( ',&nbsp;{}'.format( item['line'] ) )
                item = next( data_iter )
            while( item['handle']=='VSS' ):
                with tag( 'div', klass='parallel_variant', prov=item['ididx']  ):
                    with tag( 'span', klass=options['method'].__name__ ):
                        text( line )
                    item = next( data_iter ) #PMS
                    ref, cite = parallel_handler( item['line'] )
                    with tag( 'span', prov=item['ididx']  ):
                        text( cite )
                    with tag( 'div', klass='ref' ):
                        with tag( 'span', klass='ref' ):
                            text( ref[0] )
                        with tag( 'span', klass='title' ):
                            # doc.asis( html_5_tags( ref[1] ) )
                            doc.asis( '({})'.format( ref[0] ) )
                    item = next( data_iter ) #DAT
                    with tag( 'span', prov=item['ididx']  ):
                        doc.asis( '&nbsp;{}'.format( item['line'] ) )
                    item = next( data_iter )
                    if( item['handle']=='POS' ):
                        with tag( 'span', prov=item['ididx']  ): #POS
                            doc.asis( ',&nbsp;{}'.format( item['line'] ) )
                        item = next( data_iter )
    return item

def zie( ididx, line, options, data_iter ):
    item = next( data_iter )  # zie is only an empty boundary signal
    with tag( 'div', klass=( options['method'].__name__ + '_container' ), prov=ididx ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            with tag( 'div', klass='secundaire_lit' ):
                ref, cite = ref_handler( item['line'] )
                with tag( 'span', prov=item['ididx'] ):
                    text( cite )
                item = next( data_iter )
                if( item['handle']=='PPS' ):
                    with tag( 'span', prov=item['ididx'] ):
                        doc.asis( ',&nbsp;{}'.format( item['line'] ) )
                    item = next( data_iter )
                with tag( 'div', klass='ref' ):
                    with tag( 'span', klass='ref' ):
                        text( ref[0] )
                    with tag( 'span', klass='title' ):
                        doc.asis( html_5_tags( ref[1] ) )
            while( item['handle']=='PMS' ):
                with tag( 'div', klass='secundaire_lit' ):
                    ref, cite = ref_handler( item['line'] )
                    with tag( 'span', prov=item['ididx'] ):
                        text( cite )
                    item = next( data_iter )
                    if( item['handle']=='PPS' ):
                        with tag( 'span', prov=item['ididx'] ):
                            doc.asis( ',&nbsp;{}'.format( item['line'] ) )
                        item = next( data_iter )
                    with tag( 'div', klass='ref' ):
                        with tag( 'span', klass='ref' ):
                            text( ref[0] )
                        with tag( 'span', klass='title' ):
                            doc.asis( html_5_tags( ref[1] ) )
    return item

def ovt( ididx, line, options, data_iter ):
    with tag( 'div', klass=( options['method'].__name__ + '_container' ), prov=ididx ):
        label_boilerplate( options )
        with tag( 'div', klass='column_right' ):
            with tag( 'span', klass=options['method'].__name__ ):
               text( line )
            item = next( data_iter )
            if( item['handle']=='PMS' ): # PMS
                with tag( 'div', klass='secundaire_lit' ):
                    if( '$LITERATUREID' in item['line'] ):
                        ref, cite = ref_handler( item['line'] )
                    else:
                        ref, cite = parallel_handler( item['line'] )
                    with tag( 'span', prov=item['ididx'] ):
                        text( cite )
                    with tag( 'div', klass='ref' ):
                        with tag( 'span', klass='ref' ):
                            text( ref[0] )
                        with tag( 'span', klass='title' ):
                            doc.asis( html_5_tags( ref[1] ) )
                    item = next( data_iter )
                    if( item['handle']=='DAT' ):
                        with tag( 'span', prov=item['ididx'] ):
                            doc.asis( ',&nbsp;{}'.format( item['line'] ) )
                        item = next( data_iter )
                    while( item and item['handle']=='OVT' ):
                        with tag( 'span', klass=options['method'].__name__, prov=item['ididx'] ):
                            text( item['line'] )
                        try:  # Very possibly the very last tag (OVT)
                            item = next( data_iter )
                            if( item['handle']=='PMS' ):
                                with tag( 'div', klass='secundaire_lit' ):
                                    if( '$LITERATUREID' in item['line'] ):
                                        ref, cite = ref_handler( item['line'] )
                                    else:
                                        ref, cite = parallel_handler( item['line'] )
                                    with tag( 'span', prov=item['ididx'] ):
                                        text( cite )
                                    with tag( 'div', klass='ref' ):
                                        with tag( 'span', klass='ref' ):
                                            text( ref[0] )
                                        with tag( 'span', klass='title' ):
                                            doc.asis( html_5_tags( ref[1] ) )
                                    item = next( data_iter )
                                    if( item['handle']=='DAT' ):
                                        with tag( 'span', prov=item['ididx'] ):
                                            doc.asis( ',&nbsp;{}'.format( item['line'] ) )
                                        item = next( data_iter )
                        except StopIteration:
                            item = None
    return item


# List handlers for reflective calling
handlers = {
    'NR.': { 'method': nr, 'label': 'Hulthem-Nr' }, # Implicitly handles PL
    'OPS': { 'method': ops, 'label': 'Opschrift' },
    'IN1': { 'method': inc, 'label': 'Incipit' }, # Implicitly handles IN2
    'EX1': { 'method': exp, 'label': 'Explicit' }, # Implicitly handles EX2, XS
    'EX2': { 'method': exp, 'label': 'Explicit' },
    'AFR': { 'method': afr, 'label': 'Afrondingsformule' },
    'SAM': { 'method': sam, 'label': 'Weergave inhoud' },
    'NAM': { 'method': nam, 'label': 'Namen' },
    'AUT': { 'method': aut, 'label': 'Auteurs' },
    'SRT': { 'method': srt, 'label': 'Tekstsoort' },
    'VRM': { 'method': vrm, 'label': 'Vorm' },
    'LNG': { 'method': lng, 'label': 'Lengte' },
    'AIN': { 'method': ain, 'label': 'Aanvullende informatie' },
    'PET': { 'method': pet, 'label': 'Petit-Nommer(s)' },
    'ELT': { 'method': elt, 'label': 'Edities' }, # Implicitly handles EPS
    'SLT': { 'method': slt, 'label': 'Secundaire literatuur' }, #Implicitly handles SPS
    'VSS': { 'method': vss, 'label': 'Parallellen en varianten' }, # Implicitly handles PMS, DAT, POS
    'ZIE': { 'method': zie, 'label': 'Zie' },
    'OVT': { 'method': ovt, 'label': 'Aanvullende informatie bij parallellen en Variant'}, # Implicitly handles PMS, DAT, OVT
    'AFB': { 'method': afb, 'label': 'Afbeelding' },
    'PAR': { 'method': par, 'label': 'Parallellen en varianten' },
    'SEC': { 'method': sec, 'label': 'SEC' },
     '─':  { 'method': dsh, 'label': '─' }
}

unhandled = set()

def save_as_doc( doc ):
    with open( 'resources/hulthem_repertorium.html', 'w' ) as html_file:
        html_file.write( indent( doc.getvalue() ) )

html_boiler_plate = '''<!DOCTYPE html>
<html lang="nl-NL">
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <!-- Enable responsiveness on mobile devices-->
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1">

  <title>
    {}
  </title>
  <link rel="stylesheet" href="/repertorium_hulthem/public/css/repertorium.css"">

  <body>
    <div class="header"><img id="logo" src="https://www.huygens.knaw.nl/wp-content/themes/huygens/img/logo-white.svg"></div>
    <div class="content_container_rep">
      <h2>Repertorium Hulthem</h2>
      <h1>{}</h1>
      <div class="nav_container">
        <div class="column_left">
        </div>
        <div class="column_right">
          <div class="pag_container">
            {}
            {}
            <a href="/repertorium_hulthem/public/hulthem_repertorium_contents.html"><div class="con_pag">
              <svg width="20pt" version="1.1" id="Rectangle_3_1_" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 16 16" style="enable-background:new 0 0 16 16;" xml:space="preserve">
                <path d="M2,5h2V3H2V5z M6,3v2h8V3H6z M2,9h2V7H2V9z M11,7H6v2h5V7z M2,13h2v-2H2V13z M6,13h7v-2H6V13z"/>
              </svg></div>
            </a>
            <a href="/repertorium_hulthem/index.html"><div class="home_pag">
              <svg width="20pt" version="1.1" id="Layer_6" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 16 16" style="enable-background:new 0 0 16 16;" xml:space="preserve">
                <path d="M7.4,3.5l-4,3.2C3.1,6.9,3,7.2,3,7.5V13h3.5v-2.5C6.5,9.7,7.2,9,8,9h0c0.8,0,1.5,0.7,1.5,1.5V13H13V7.5c0-0.3-0.1-0.6-0.4-0.8l-4-3.2C8.3,3.2,7.7,3.2,7.4,3.5z"/>
              </svg></div>
            </a>
          </div>
        </div>
      </div>
    <div class="nr_container">{}
    </div>
    <div class="footer">
      <div class="footer_column">
        <h2>Contact</h2>
        <p>Ons bezoekadres:<br>
        Spinhuis<br>
        Oudezijds Achterburgwal 185<br>
        1012 DK AMSTERDAM</p>
        <p>Ons postadres:<br>
        Huygens ING<br>
        Postbus 10855<br>
        1001 EW AMSTERDAM</p>
        <p><a href="mailto:info@huygens.knaw.nl">info@huygens.knaw.nl</a><br>
        +31 (0)20 — 224 68 00</p>
      </div>
    </div>
  </body>
</html>
'''

contents_boiler_plate = '''<!DOCTYPE html>
<html lang="nl-NL">
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <!-- Enable responsiveness on mobile devices-->
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1">

  <title>
    Online Repertorium van teksten in het handschrift Hulthem
  </title>
  <link rel="stylesheet" href="/repertorium_hulthem/public/css/repertorium.css"">

  <body>
    <div class="header"><img id="logo" src="https://www.huygens.knaw.nl/wp-content/themes/huygens/img/logo-white.svg"></div>
    <div class="content_container_rep">
      <h1>Repertorium Hulthem — Inhoud</h1>
      <div class="nav_container">
        <div class="column_left">
        </div>
        <div class="column_right">
          <div class="pag_container">
            <a href="/repertorium_hulthem/public/hulthem_repertorium_contents.html"><div class="con_pag">
              <svg width="20pt" version="1.1" id="Rectangle_3_1_" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 16 16" style="enable-background:new 0 0 16 16;" xml:space="preserve">
                <path d="M2,5h2V3H2V5z M6,3v2h8V3H6z M2,9h2V7H2V9z M11,7H6v2h5V7z M2,13h2v-2H2V13z M6,13h7v-2H6V13z"/>
              </svg></div>
            </a>
            <a href="/repertorium_hulthem/index.html"><div class="home_pag">
              <svg width="20pt" version="1.1" id="Layer_6" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 16 16" style="enable-background:new 0 0 16 16;" xml:space="preserve">
                <path d="M7.4,3.5l-4,3.2C3.1,6.9,3,7.2,3,7.5V13h3.5v-2.5C6.5,9.7,7.2,9,8,9h0c0.8,0,1.5,0.7,1.5,1.5V13H13V7.5c0-0.3-0.1-0.6-0.4-0.8l-4-3.2C8.3,3.2,7.7,3.2,7.4,3.5z"/>
              </svg></div>
            </a>
          </div>
        </div>
      </div>
{}
    </div>
    <div class="footer">
      <div class="footer_column">
        <h2>Contact</h2>
        <p>Ons bezoekadres:<br>
        Spinhuis<br>
        Oudezijds Achterburgwal 185<br>
        1012 DK AMSTERDAM</p>
        <p>Ons postadres:<br>
        Huygens ING<br>
        Postbus 10855<br>
        1001 EW AMSTERDAM</p>
        <p><a href="mailto:info@huygens.knaw.nl">info@huygens.knaw.nl</a><br>
        +31 (0)20 — 224 68 00</p>
      </div>
    </div>
  </body>
</html>
'''

contents_item_boiler_plate = '''      <div class="con_container">
        <div class="column_left">
          <span class="hulthem_nummer_contents">{}</span>
        </div>
        <a href="hulthem_repertorium_{}.html">
            <div class="column_right">
                <span class="pl_contents">{}&nbsp;</span><span class="ops_contents">{}</span>
            </div>
        </a>
      </div>
'''

def save_as_pages( doc ):
    html_doc = indent( doc.getvalue() )
    html_doc = html_doc.split( '\n' )
    html_doc = ( '\n'.join( html_doc[3:-2] ) ) + '\n'
    html_docs = html_doc.split( '    <div class="nr_container">' )
    max_idx = len( html_docs[1:] )
    print( max_idx )
    for idx,doc in enumerate( html_docs[1:] ):
        # I admit this is a terrible hack, but it's 30C and I'm lazy.
        ops = regex.search( '<span class="ops" prov="DOCUMENT.DOC:L\d+">(.*)</span>', doc ).groups()[0]
        next_page = '<a href="hulthem_repertorium_{}.html"><div class="next_pag">&#x25BA;</div></a>'.format( idx+2 )
        if( idx==max_idx-1 ):
            next_page = ''
        previous_page = '<a href="hulthem_repertorium_{}.html"><div class="prev_pag">&#x25C4;</div></a>'.format( idx )
        if( idx==0 ):
            previous_page = ''
        doc = html_boiler_plate.format( 'Repertorium Hulthem, tekst {}'.format( idx+1 ), ops, next_page, previous_page, doc[0:-1] )
        with open( 'docs/public/hulthem_repertorium_{}.html'.format(idx+1), 'w' ) as html_file:
            html_file.write( doc )

def save_contents( contents ):
    contents_html = ''
    idx = 1
    for item in contents:
        contents_item_html = contents_item_boiler_plate
        contents_item_html = contents_item_html.format( item[0], idx, item[1], item[2] )
        contents_html += contents_item_html
        idx += 1
    contents_html = contents_boiler_plate.format( contents_html )
    with open( 'docs/public/hulthem_repertorium_contents.html', 'w' ) as html_file:
        html_file.write( contents_html )

# MAIN
hulthem_iter = iter( hulthem_data )   #[0:924] )

with tag('html'):
    with tag('body'):

        for item in hulthem_iter:
            try:
                next_item = handlers[ item['handle'] ]['method']( item['ididx'], item['line'], handlers[ item['handle'] ], hulthem_iter )
                while( next_item ):
                    next_item = handlers[ next_item['handle'] ]['method']( next_item['ididx'], next_item['line'], handlers[ next_item['handle'] ], hulthem_iter )
            except KeyError as err:
                unhandled.add( 'No handler for {}'.format( err ) )


for nohandle in unhandled:
    print( nohandle )

# Postprocessing
# save_as_doc( doc )
save_as_pages( doc )
save_contents( contents )
