# Convert an export of raw Human data on iOS (Profile / Settings / Export data) to geoJSON
# Use this data export for examople to create your own map in Mapbox Studio

import csv
import os
import math

# Directory that has all Human CSV exported files
path = 'activities/csv/'

def distance(lat1, lng1, lat2, lng2):
    # return estimated distance in meters
    radius = 6371 * 1000

    dLat = (lat2-lat1) * math.pi / 180
    dLng = (lng2-lng1) * math.pi / 180

    lat1 = lat1 * math.pi / 180
    lat2 = lat2 * math.pi / 180

    val = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLng/2) * math.sin(dLng/2) * math.cos(lat1) * math.cos(lat2)
    ang = 2 * math.atan2(math.sqrt(val), math.sqrt(1-val))
    return radius * ang


# output head
output = '''{ "type" : "FeatureCollection", "features" : [
    '''

# geoJSON feature template
template = '''\
{ "type" : "Feature", "geometry" : { "type" : "LineString", "coordinates" : %s}, "properties" : { "mode" : "%s", "speed" : "%s", "date" : "%s"}}
    '''


for root, dirs_list, files_list in os.walk(path):
    for file_name in files_list:
        # only csv files
        if os.path.splitext(file_name)[-1] == '.csv':
            file_name_path = os.path.join(root, file_name)
            # Read in raw data from csv
            rawData = csv.reader(open(file_name_path, 'rb'))
            # Skip the first line
            next(rawData, None)
            coordinates = []

            for row in rawData:
                # Only lines if previous location is < 300m
                if len(coordinates) > 0:
                    meters = distance(float(row[2]), float(row[3]), coordinates[-1][1], coordinates[-1][0])
                    print meters
                    if meters < 300:
                        coordinates.append([float(row[3]), float(row[2])])
                else:
                    coordinates.append([float(row[3]), float(row[2])])

            # a line needs at least two points
            if len(coordinates) > 1:
                output += template % (coordinates, row[1], row[4], row[0])
                # add comma
                output += ","

            print coordinates
            print file_name_path   # This is the full path of the filter file

    # remove last comma
    output = output[0:-1]


# add tail for geojson file
output += ''']}'''

# opens an geoJSON file to write the output to
outFileHandle = open("output.geojson", "w")
outFileHandle.write(output)
outFileHandle.close()
