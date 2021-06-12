import regex

hulthem_data = []
with open( 'cdrom_contents/DOCS/DOCUMENT.DOC', 'r', encoding='cp850' ) as doc_file:
    # Last line is empty.
    ididx=0
    for line in doc_file.read().split( '\n' )[0:-1]:
        # Checked: between label and line it's alway ' = '.
        hulthem_data.append( { 'handle': line[0:3], 'line': line[6:], 'ididx': ididx } )
        ididx += 1

with open( 'hulthem_repertorium.html' ) as html_file:
    html = html_file.read()

matches = []
matches_intm = regex.findall( r'prov="(DOCUMENT.DOC:L.*?)"', html )
for match in matches_intm:
    match = regex.sub( r'DOCUMENT.DOC:L', '', match )
    if( ',' in match ):
        matches += match.split( ',' )
    else:
        matches.append( match )
print( matches )
expected = [ '{}'.format( i ) for i in list( map( lambda x: x['ididx'], hulthem_data ) ) ]
missing = list( set( expected ) - set( matches ) )
missing = list( map( lambda x: int(x), missing ) )
print( 'Missing:',len( missing ) )
missing.sort()
for miss in missing:
    print( miss, hulthem_data[ miss ] )
