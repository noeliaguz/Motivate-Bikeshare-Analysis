# EXPLORE US BIKESHARE PROJECT
"""
In this program, we will be exploring data related to
bikeshare systems for three major cities in the US: Chicago, 
New York, and Washington. Let's see what we can discover
about our data!
"""

import time
import pandas as pd
import numpy as np

# VARIABLES NEEDED 
"""Below is the information we will use to access our data.

We will need a dictionary that has the city names as keys, and 
the file names as values.
We will also need to assign the variables for MONTHS and DAYS
as lists to help us access our data.
"""

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june'] 
DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
CITIES = list(CITY_DATA.keys()) # This is useful to help access the keys in our dictionary as a list

def get_filters():
    """This function asks the user to specify a city, month, and day to analyze.

    The output of this function returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('\nHello! Let\'s explore some US bikeshare data!\n')

    # First, we need to get user input for city (chicago, new york city, washington)
    while True:
        city = input('Which city would you like to see data for?\nPlease select one of the following: Chicago, New York City, Washington\n').casefold()
        if city in CITY_DATA:
            break
        else:
            print('\nSorry! That\'s not a valid option. Please try again.\n')
            continue
        
    # Next, we need to get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month would you like to see data for?\n').casefold()
        # month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june'] THIS IS ONE WAY TO DO THIS LOOP, with the list in the loop
        if month in MONTHS:
            break
        else:
            print('\nSorry! That\'s not a valid option. Please try again.\n')
            continue

    # Lastly, we need to get user input for day (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhich day would you like to see data for?\n').casefold()
        if day in DAYS:
            break
        else:
            print('\nSorry! That\'s not a valid option. Please try again.\n')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """This function loads data for the specified city and filters by month and day if applicable.

    It will take in the following arguments defined from the previous function:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    The output returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Let's load the data file into a dataframe (df) using the dictionary CITY_DATA
    df = pd.read_csv(CITY_DATA[city])
    
    # Next, we'll convert the Start Time column to a datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Then, we will extract month and day_of_week from Start Time to create new columns in the original dataframe
    # Remember, depending on the version of Python, you may need to change .weekday_name --> .day_name
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Let's filter by month, if applicable
    if month != 'all':
        # We can use the index of the MONTHS list to get the corresponding integers.
        # Since the MONTHS list begins with 'all' the index for 'january' is one, and we do not need to address this by adding 1 when assigning month_int
        
        month_int = MONTHS.index(month) # We'll use month_int to avoid confusion with month

        # Now, we'll filter by month to create the new dataframe
        df = df[df['month'] == month_int] 

    # Let's also filter by day_of_week, if applicable
    if day != 'all':
        
        # Here, we filter by day_of_week to create the new dataframe
        df = df[df['day_of_week'] == day.title()] 
       
        # day.title() is properly cased user input
        # we compare the column day_of_week to a single string (user input)
        # the inner info returns a bool per row uses false rows, that dont match user input, to drop them since they 'fail'
  
    return df


def time_stats(df):
    """This function displays statistics on the most frequent times of travel.
   
    We'll display the most common month traveled, the most common day traveled, and the most common start hour.
    """ 

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Let's display the most common month traveled
    most_common_month = df['month'].mode()[0] #returns row index and mode value
    #month_list = ['all', 'january', 'febraury', 'march', 'april', 'may', 'june'] NEED THIS LIST IF YOU USE THE LIST WITHIN INDIVIDUAL FUNCTIONS
    #print('The most common moth traveled is: {}'.format(month_list[most_common_month].title()))
    #print('string'.format(MONTHS[month_list-1]))...this is for if the month list does not have 'all'
    print('The most common month traveled is: {}'.format(MONTHS[most_common_month].title())) #We need to display month as a string/name

    # Here, we will display the most common day traveled
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of the week traveled is: ', most_common_day_of_week)


    # And this will display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is: ', most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    This function displays statistics on the most popular start and end stations and 
    the most popular trip taken according to the start and end station used for the trip.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # This displays the most commonly used start station, object datatype because it's a group of strings
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ', most_common_start_station)


    # This displays the most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: ', most_common_end_station)


    # We concatenate the start and end station columns in our dataframe (df) and then display 
    # the most popular trip taken according to the start and end station used
    df['popular_trip'] = df['Start Station'] + ' to ' + df['End Station'] #added ' to ' for user friendly purposes
    most_freq_start_end_station = df['popular_trip'].mode()[0]
    print('The most popular trip taken according to the start and end station used is: ', most_freq_start_end_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """This function displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Here, we display the total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: ', total_travel_time)


    # This will display the avg travel time (mean)
    avg_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is: ', avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """This function displays statistics on bikeshare users.
    
    IMPORTANT: The data for the 'washington.csv' file does NOT have columns for 'Gender' or 'Birth Year'
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # First, we'll display counts of user types with .value_counts()
    user_types = df['User Type'].value_counts()
    print('The count of user types is: ', user_types)


    # Let's then display counts of gender, we should account for missing columns
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('The counts of gender is: ', gender)
    else:
        print('Sorry! No data for Gender exists for this city.')


    # Let's also display earliest min, most recent max, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest birth year is: \n', earliest_birth_year)

        most_recent_birth_year = df['Birth Year'].max()
        print('The most recent birth year is: \n', most_recent_birth_year)

        most_common_birth_year = df['Birth Year'].mode()[0]
        print('The most common birth year is: \n', most_common_birth_year)
    else:
        print('Sorry! No data for Birth Year exists for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#want the user to ask for the raw data, first 5 rows, next 5 if Y, none if N
def raw_data(df):
    """This function allows the user to view raw data from the file.
    
    The function will return 5 rows of data at a time, beginning with the first 5 rows.
    """
    view_data = input('Would you like to view the raw data?\n Please enter "Y" or "N": ').upper()
    i = 0 # We will need a starting value for i since we want to begin with the first 5 rows of data
    while True:
        if view_data == 'Y':
            print(df.iloc[i:i+5,:]) # This shows us int location for (row, column)
            i += 5 # This accounts for when user says Y again
            view_data = input('Would you like to view more raw data?\n Please select "Y" or "N": ').upper()

        elif view_data == 'N':
            print('\nNo problem!')
            break

        else:
            view_data = input('Sorry! That\'s not a valid option.\nPlease only select "Y" or "N": \n').upper()
            

def main():
    """This is the function that will run the entire program."""
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df) # We must add in raw_data(df) as well in case the user would like to view raw data

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            print('\nAlright! See you next time!\n')
            break


if __name__ == "__main__":
	main()
