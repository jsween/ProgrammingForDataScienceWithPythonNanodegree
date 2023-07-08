import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
VALID_MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
VALID_DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', ]

def get_city():
    """
    Asks user to specify city to analyze.

    Returns:
        (str) selected_city - name of the city to analyze
    """
    selected_city = None
    while selected_city not in CITY_DATA.keys():
        selected_city = input("Please select a city: Chicago, New York City or Washington\n").lower()

        if selected_city in CITY_DATA.keys():
            return selected_city
        else:
            print(f"{selected_city} is not available. Please try selecting again.\n")

def get_month():
    """
    Asks user to specify month to analyze.

    Returns:
        (str) selected_month - name of the month to filter by, or "all" to apply no month filter
    """
    selected_month = None
    while selected_month not in VALID_MONTHS:
        selected_month = input("Please select a month: January, February, March, April, May, June, or all\n").lower()

        if selected_month in VALID_MONTHS:
            return selected_month
        else:
            print(f"{selected_month.capitalize()} is not available. Please try selecting again.\n")

def get_day_of_week():
    """
    Asks user to specify day to analyze.

    Returns:
        (str) selected_day - name of the day of week to filter by, or "all" to apply no day filter
    """
    selected_day = None
    while selected_day not in VALID_DAYS:
        selected_day = input("Please select a day of the week: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or all\n").lower()

        if selected_day in VALID_MONTHS:
            return selected_day
        else:
            print(f"{selected_day.capitalize()} is not available. Please try selecting again.\n")


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = get_city()

    # get user input for month (all, january, february, ... , june)
    month = get_month()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_day_of_week()

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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
