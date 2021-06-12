from yattag import Doc
from yattag import indent
import regex

# Create the HTML Doc
doc, tag, text = Doc().tagtext()
doc.asis('<!DOCTYPE html>')

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
                doc.asis( '{}&nbsp;'.format( re_hulthem_nr.search( line ).groups()[0] ) )
            item = next( data_iter )
            if( item['handle']=='PL.' ):
                with tag( 'span', klass='pl', prov=item['ididx']):
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
    with open( 'hulthem_repertorium.html', 'w' ) as html_file:
        html_file.write( indent( doc.getvalue() ) )

html_boiler_plate = '''<!DOCTYPE HTML>
<html>
  <head>
    <title>{}</title>
    <link rel="stylesheet" type="text/css" href="css/repertorium.css" />
    <meta charset="UTF-8">
  </head>
  <body>
    <div class="nav_container">
      <div class="column_left">
      </div>
      <div class="column_right">
        <div class="pag_container">
            {}
            {}
        </div>
      </div>
    </div>
    <div class="nr_container">{}
  </body>
</html>
'''

def save_as_pages( doc ):
    html_doc = indent( doc.getvalue() )
    html_doc = html_doc.split( '\n' )
    html_doc = ( '\n'.join( html_doc[3:-2] ) ) + '\n'
    html_docs = html_doc.split( '    <div class="nr_container">' )
    max_idx = len( html_docs[1:] )
    print( max_idx )
    for idx,doc in enumerate( html_docs[1:] ):
        next_page = '<a href="hulthem_repertorium_{}.html"><div class="next_pag">&#x25BA;</div></a>'.format( idx+2 )
        if( idx==max_idx-1 ):
            next_page = ''
        previous_page = '<a href="hulthem_repertorium_{}.html"><div class="prev_pag">&#x25C4;</div></a>'.format( idx )
        if( idx==0 ):
            previous_page = ''
        if( idx>=max_idx-3 ):
            print(doc)
            print('-------------')
        doc = html_boiler_plate.format( 'Repertorium Hulthem, tekst {}'.format( idx+1 ), next_page, previous_page, doc[0:-1] )
        with open( 'public/hulthem_repertorium_{}.html'.format(idx+1), 'w' ) as html_file:
            html_file.write( doc )

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
