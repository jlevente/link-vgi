import json
import urllib2
import urllib
import csv

api_key = 'API-KEY'
csv_path = 'wheelmap_python.csv'

class WheelmapItem:
	def __init__(self, name, osm_id, lat, lon, category, node_type, accessible):
		self.name = name
		self.osm_id = osm_id
		self.lat = lat
		self.lon = lon
		self.category = category
		self.node_type = node_type
		self.accessible = accessible

	def getName(self):
		if not self.name:
			return ''
		else:
			return self.name.encode('utf-8')

def getWheelmapNodes(ll_lat, ll_lon, ur_lat, ur_lon, page, accessible):
	bbox = str(ll_lat) + ',' + str(ll_lon) + ',' + str(ur_lat) + ',' + str(ur_lon)
	url = 'http://wheelmap.org/api/nodes?api_key=' + api_key + '&bbox=' + bbox + '&wheelchair=' + accessible + '&page=' + str(page)
	headers = {'User-Agent':'Python'}
	
	req = urllib2.Request(url, None, headers)

	print (url)
	resp = urllib2.urlopen(req).read().decode('utf-8')
	return json.loads(resp)

# When we get the first load of data we can read the meta info to see how many pages there are in total

firstPage = getWheelmapNodes(24.899319,60.150223,24.986683,60.177915,1,'yes')
numPages = firstPage['meta']['num_pages']

# so now we need to loop through each page and store the info
pagedData = []
pagedData.append(firstPage)

for i in range (2,numPages+1):
	pagedData.append(getWheelmapNodes(24.899319,60.150223,24.986683,60.177915,i,'yes'))

# now that we have the data we should go through and create a list of items 
# for now we will store the name, location, category, node type, accessibility and osm id
items = []
for i in range (0,len(pagedData)):
	page = pagedData[i]
	# go through each item
	nodes = page['nodes']
	for node in nodes:
		item = WheelmapItem(node['name'], node['id'], node['lat'], node['lon'], node['category']['identifier'], node['node_type']['identifier'], node['wheelchair'])
		items.append(item)

print('Total items read: ' + str(len(items)))

#finally output to a csv , encoding='UTF-8'
with open(csv_path, 'w') as csvfile:
	fieldnames = ['osm_id', 'name', 'lat', 'lon', 'category', 'type', 'accessible']
	wr = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
	wr.writeheader()

	for item in items:
		wr.writerow({'osm_id': item.osm_id, 'name': item.getName(), 'lat': item.lat, 'lon': item.lon, 'category': item.category, 'type': item.node_type, 'accessible': item.accessible})

