# Grotte 

# aggiunge tag source=RAFVG
add_source = False
source = 'RAFVG'

# do not add unique reference IDs to OSM?

# aggiunge tag ref:<dataset_id>=<id del RAFVG>
# True -> relying only on geometric matching every time
no_dataset_id = True
# sito opendata della regione fvg                           
dataset_id = 'rafvg'

# Overpass query to use when searching OSM for data
#overpass_timeout = 120 default
overpass_timeout = 300
query = [('natural', 'cave_entrance')]

# parameter --osm will use indipendently generated queries, for cave_amtrance:
# http://overpass-turbo.eu/s/1729
# use wget -O manual-query.osm <http_addr obtained exporting compact query>

bbox = True


# tags to replace on matched OSM objects
master_tags = ('description')

delete_unmatched = False
tag_unmatched = { 'note':'this cave entrance has not matches with confirmed RAFVG object within a 20m radius' }


# max distance to search for a match in meters
max_distance = 20

duplicate_distance = 1
