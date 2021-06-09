import regex

with open( 'cdrom_contents/DOCS/DOCUMENT.DOC', 'r', encoding='cp850' ) as doc_file:
  doc = doc_file.read().split( '\n' )

nr_re = regex.compile( '^([^=\s]+)\s=' )
codes_used = set()
for line in doc:
    match = nr_re.match( line )
    if match:
        codes_used.add( match.groups()[0].strip() )

print( sorted( codes_used ) )


with open( 'cdrom_contents/HLP/TAGINDEX.ENG', 'r', encoding='cp850' ) as doc_file:
  doc = doc_file.read().split( '\n' )

nr_re = regex.compile( '^   (.*)\t(.*)' )
codes_explained = dict()
for line in doc:
    match = nr_re.match( line )
    if match:
        codes_explained[ match.groups()[0][0:3].strip() ] = ( match.groups()[0].strip(), match.groups()[1].strip() )

print( '-------------' )
print( sorted( codes_explained ) )

def match_explained_code( k ):
    try:
        return ( k, codes_explained[k] )
    except KeyError:
        return ( k, ( k, k.title() ) )

explained = { k: match_explained_code(k) for k in codes_used }
for k,v in explained.items():
    print( k, v[0], v[1][0], v[1][1] )


# So, what this version proofs is that the more than 3 letter labels are
# not a good explanation for the three letter labels. Although there are
# matches, `PMS` is clearly not `PMSP`, as `PMS` seems to indicate some
# reference scholarly publication and `PMSP` sigla of mss. that have
# parallel text.
#
# Based on this insight, I am making a new version that has an explicit list
# of interpreted solutions for unexplained labels.
