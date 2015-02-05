### Designed to Run in MacOSX Terminal. "Open" commands do not run in Linnux.
echo "This script was designed to run in MAC OSX Terminal."
echo "It will not have full functionality in Linnux."
echo "Created by Joshua G. Mausolf"

sleep 1.5

#Run LatLong and Print Results to Terminal and text document
python parse.py "latlong"

python parse.py "latlong" > Avg_lat_long.txt
open Avg_lat_long.txt

sleep 1

#Run and Open Bar Chart
python parse.py "bar"
