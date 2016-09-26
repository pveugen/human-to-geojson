# Convert a Human data export to geoJSON
Turn your Human data export into a map with Mapbox Studio

1. Export Human data in the Human settings (iOS only)
2. Wait for an e-mail to arrive with a link to your data export.
3. Download the archive to your laptop and unzip.
4. Download [this Python script](https://github.com/pveugen/human-to-geojson/blob/master/convert-to-geojson.py) and store in root of the export folder. 
5. Open a terminal and go to the export folder.
6. Run the Python script: `python convert-to-geojson.py`
7. Go into Mapbox Studio and select Tilesets in the menu.
8. Create a new Tileset and upload the generated output.geojson file.
9. Tap the ≡ icon next to your newly created Tileset and select _Add to Style_
10. Style your data


<img src="https://raw.githubusercontent.com/pveugen/human-to-geojson/master/mapbox-studio.png" alt="Data uploaded to Mapbox Studio">


<img src="https://raw.githubusercontent.com/pveugen/human-to-geojson/master/mapbox-example.png" alt="Example of a Mapbox heatmap map with Human data">
