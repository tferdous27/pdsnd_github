import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    cities =['chicago', 'new york city', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\n''Would you like to get data for Chicago, New York City, or Washington?\n').lower()
        if city not in cities:
            print('\nIncorrect input. Please type in a city from the given options.\n')
            continue
        else:
            print('\nYou have chosen {}. If this is not the case, restart the program now!\n'.format(city.title()))
            break

    # get user input for month (all, january, february, ... , june)

    while True:
        time_filter = input('\nWould you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.\n').lower()
        if time_filter == 'month':
            #print('\nAlright. We will filter by month.\n')
            month = input('\nWhich month? January, February, March, April, May, June, or all? Please type the month name in full.\n').lower()
            day = 'all'
            if month not in months:
                print('\nIncorrect input. Please type in a month from the given options.\n')
                continue
        elif time_filter == 'day':
            #print('\nAlright. We will filter by day.\n')
            day = input('\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all? Please type the name of the day in full.\n').lower()
            month = 'all'
            if day not in days:
                print('\nIncorrect input. Please type in a day from the given options.\n')
                continue
        elif time_filter == 'both':
            print('\nYou have chosen both.\n')
            month = input('\nWhich month? January, February, March, April, May, June, or all? Please type the month name in full.\n').lower()
            if month not in months:
                print('\nIncorrect input. Please type in a month from the given options.\n')
            day = input('\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all? Please type the name of the day in full.\n').lower()
            if day not in days:
                print('\nIncorrect input. Please type in a day from the given options.\n')
                continue
        elif time_filter == 'none':
            print('\nYou have chosen no time filter.\n')
            month = 'all'
            day = 'all'
        else:
            print('\nUnrecognized input. Please restart the program now!')
        break
    # get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]
    if day!= 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('The most common month:', months[popular_month-1])


    # display the most common day of week
    popular_day = df['day'].mode()[0]
    print('The most common day:', popular_day)


    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nThe most commonly used start station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nThe most commonly used end station:', popular_end_station)

    # display most frequent combination of start station and end station trip

    popular_station_combination = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('\nThe most frequent combination of start station and end station trip:', popular_station_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum().astype(int)
    print('\nTotal travel time:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean().astype(int)
    print('\nMean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if 'User Type' in df.columns:
        counts_user_type = df['User Type'].value_counts()
        print('\nCounts of user types:', counts_user_type)
    else:
        print('\nUser Type column does not exist.\n')
    # Display counts of gender
    if 'Gender' in df.columns:
        counts_gender = df['Gender'].value_counts()
        print('\nCounts of gender:', counts_gender)
    else:
        print('\nGender column does not exist.\n')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = np.nanmin(df['Birth Year']).astype(int)
        print('\nEarliest year of birth:', earliest_birth_year)
        most_recent_birth_year = np.nanmax(df['Birth Year']).astype(int)
        print('\nMost recent year of birth:', most_recent_birth_year)
        most_common_birth_year = df['Birth Year'].mode().astype(int)
        print('\nMost common year of birth:', most_recent_birth_year)
    else:
        print('\nBirth Year column does not exist.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Display 5 lines of raw data upon request."""
    data = input('\nWould you like to see individual trip data? Please type "yes" or "no".\n').lower()
    if data == 'yes':
        index1 = 0
        index2 = 5
        while True:
            print(df.iloc[index1: index2])
            index1 += 5
            index2 += 5
            more_data = input('\nWould you like to see more data? Please type "yes" or "no".\n').lower()
            if more_data != 'yes':
                break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
