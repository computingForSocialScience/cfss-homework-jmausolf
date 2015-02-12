# Imports functions:
import unicodecsv as csv 
import matplotlib.pyplot as plt
import subprocess #added module to increase stability. 
# plt.show() has been causing terminal to crash in past assignments.

#Defining the new function getBarChartData() which imports data from the 
#two CSV files artists.csv and albums.csv
def getBarChartData():
    """Function to import data from the two CSV files artists.csv and albums.csv in order 
    manipulate the data and prepare it for use in the plotBarChart() function."""

    #Importing the data from artists and albums csv files. Setting these files equal to 
    # new variables f_artists and f_albums.  
    f_artists = open('artists.csv')
    f_albums = open('albums.csv')

    #Defining artists_rows and albums_rows as equal to the the opened csv files 
    # that csv.reader "reads". Read data is saved as these new variables.
    artists_rows = csv.reader(f_artists)
    albums_rows = csv.reader(f_albums)

    #Setting the first row of artists.csv to artists_header
    #Setting the first row of albums.csv to albums_header
    artists_header = artists_rows.next()
    albums_header = albums_rows.next()

    #Creating new empty list artist_names
    artist_names = []
    
    #Creating New Variable 'decades'. This will be the x_values forming the x-axis
    # on the bar chart. This creates a list of numbers between 1900 and 2020 in 
    # 10 year increments. 
    decades = range(1900,2020, 10)

    #Creating Decade Dictionary with associated keys and values.
    # This will be the y_values for a given year (the x value).
    decade_dict = {} # Create dictionary

    #For each "decade" in the list decade,
    #set the initial value equal to zero.
    for decade in decades:
        decade_dict[decade] = 0
    
    #Loop over artist_rows list. It is currently empty. 
    for artist_row in artists_rows:
        if not artist_row: #if not an element of artists_rows, continue
            continue
        artist_id,name,followers, popularity = artist_row #redefine artist_row to equal 
        #the values of the entries found in the CSV file as created by fetchArtist.py and
        # artists.csv. If you added other categories to the fetchArtist list, you would 
        # need to add other values here, such as "genre" or "url". 

        #append all such names in artist row to artist_names list
        artist_names.append(name)


    #Loop over album_rows list. It is currently empty.     
    for album_row  in albums_rows:
        if not album_row: #if not an element of albums_rows, continue
            continue
        #redefine artist_row to equal the values of the entries found in the CSV file as created by fetchArtist.py and
        # artists.csv. 
        artist_id, album_id, album_name, year, popularity = album_row

        #Create a loop in this loop for every decade in the list decades.
        for decade in decades:
            #This is a counter function such that for every <year> entry in an album row,
            # (which represents an album since every album has a year associated with it)
            # we add a count to the decades dictionary for the appropriate decade.
            if (int(year) >= int(decade)) and (int(year) < (int(decade) + 10)):
                decade_dict[decade] += 1
                break


    x_values = decades # Sets the x-axis to decades
    y_values = [decade_dict[d] for d in decades] # Sets the y-axis to the number of albums
    # as measured by the year counts for a particular artist in a particular decade.

    #Returns all x_values(decades), y_values(counts of album(years) in a decade, and the
        #artist names from the header)
    return x_values, y_values, artist_names


#Creates a new bar chart function.
def plotBarChart():
    """Create Bar Chart using the Data from getBarChartData."""

    #Uses the x_values, y_values, and artist_names returned from the above function.
    x_vals, y_vals, artist_names = getBarChartData()
    
    #defines the type of figure and parameters
    fig , ax = plt.subplots(1,1)
    ax.bar(x_vals, y_vals, width=10) #bar chart with x_vals, y_vals, and a width of 10
    ax.set_xlabel('decades') #defines the x axis label
    ax.set_ylabel('number of albums') #defines y axis label
    ax.set_title('Totals for ' + ', '.join(artist_names)) #defines graph title

    # Draw the plot, save the figure as 'bar.jpg', and open said figure.
    plt.draw() #renders the plot but doesn't show it
    plt.savefig('bar.jpg') #saves the rendering to the filename bar.jpg
    subprocess.call("open bar.jpg", shell=True) #uses the shell subprocess to open this
    #as a jpg image. This avoids issues with the terminal locking up from the alternative
    #plt.show().
    

#Test code. 
#plotBarChart()