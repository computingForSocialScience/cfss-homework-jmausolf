import unicodecsv as csv
import matplotlib.pyplot as plt
import subprocess #added module to increase stability. 
# plt.show() has been causing terminal to crash in past assignments

#Defining the new function getBarChartData() which imports data from the 
#two CSV files artists.csv and albums.csv
def getBarChartData():
    """Function to import data from the two CSV files artists.csv and albums.csv in order 
    manipulate the data and prepare it for use in the plotBarChart() function."""

    #Importing the data
    f_artists = open('artists.csv')
    f_albums = open('albums.csv')

    #Defining 
    artists_rows = csv.reader(f_artists)
    albums_rows = csv.reader(f_albums)

    artists_header = artists_rows.next()
    albums_header = albums_rows.next()

    artist_names = []
    
    #Creating New Variable 'decades'. This will be the x_values forming the x-axis
    # on the bar chart. 
    decades = range(1900,2020, 10)

    #Creating Decade Dictionary with associated keys and values.
    # This will be the y_values for a given year (the x value).
    decade_dict = {} # Create dictionary

    #Set initial dictionary counts equal to zero.
    for decade in decades:
        decade_dict[decade] = 0
    

    for artist_row in artists_rows:
        if not artist_row:
            continue
        artist_id,name,followers, popularity = artist_row
        artist_names.append(name)

    for album_row  in albums_rows:
        if not album_row:
            continue
        artist_id, album_id, album_name, year, popularity = album_row
        for decade in decades:
            if (int(year) >= int(decade)) and (int(year) < (int(decade) + 10)):
                decade_dict[decade] += 1
                break

    x_values = decades
    y_values = [decade_dict[d] for d in decades]
    return x_values, y_values, artist_names

def plotBarChart():
    """Create Bar Chart using the Data from getBarChartData."""

    x_vals, y_vals, artist_names = getBarChartData()
    
    fig , ax = plt.subplots(1,1)
    ax.bar(x_vals, y_vals, width=10)
    ax.set_xlabel('decades')
    ax.set_ylabel('number of albums')
    ax.set_title('Totals for ' + ', '.join(artist_names))

    # Draw the plot, save the figure as 'bar.jpg', and open said figure.
    plt.draw()
    plt.savefig('bar.jpg')
    subprocess.call("open bar.jpg", shell=True)
    


#plotBarChart()

    
