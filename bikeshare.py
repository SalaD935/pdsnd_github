import time
import pandas as pd
import numpy as np

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input(
            "Enter a city to analyze from these:\nchicago, new york city or washington.\n"
        ).lower()
        if city in ["chicago", "new york city", "washington"]:
            break
        else:
            print("Invalid city. Please choose from the options mentioned")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            "Enter a month from these:\njanuary, february, march, april, may, june.\nTo filter or enter 'all' to not apply any filter:\n"
        ).lower()
        if month in ["all", "january", "february", "march", "april", "may", "june"]:
            break
        else:
            print("Invalid month. Please choose from the options mentioned")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(
            "Choose a day from these:\nmonday, tuesday, wednesday, thursday, friday, saturday, sunday\nTo filter or enter 'all' to not apply any filter:\n"
        ).lower()
        if day in [
            "all",
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        ]:
            break
        else:
            print("Invalid day. Please choose from the mentioned")

    print("-" * 40)
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
    # this line loads the data file into df
    df = pd.read_csv(CITY_DATA[city])
    # this line converts the start time column to date time
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    # this line creats new columns by extracting the month and day from the start time
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()
    # this line filters by month if could
    if month != "all":
        # each month has its index and with that in use we get the int of it
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        # this line creats the new df from filtering by month
        df = df[df["month"] == month]
    # this line filters by day if could
    if day != "all":
        # this line creats the new df from filtering by day
        df = df[df["day_of_week"] == day.title()]
    return df

    row_index = 0
    pass


def display_raw_data(df):
    """Displays Raw data upon request by the user."""
    start_column = 0
    while True:
        user_input = input(
            "Do you want to see 5 lines of raw data? yes or no:\n"
        ).lower()
        if user_input == "yes":
            end_column = start_column + 5
            # Display the next 5 rows only
            print(df.iloc[start_column:end_column])
            # Update the start column
            start_column = end_column

            # Check if there is any more rows to display
            if start_column >= len(df):
                print("No more raw data to display.")
                break
        elif user_input == "no":
            break
        # Handles if the user inputs an invalid answer
        else:
            print("Please enter yes or no only")


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    print("The most common month is:", common_month)

    # TO DO: display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print("The most common day is:", common_day)

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    common_hour = df["hour"].mode()[0]
    print("The most common hour is:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].value_counts().idxmax()
    print("The most commonly used start station is:", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].value_counts().idxmax()
    print("The most commonly used end station is:", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_trip = df.groupby(["Start Station", "End Station"]).size().idxmax()
    print(
        "The most frequent combination of start station and end station trip is:",
        common_trip,
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("The total travel time is:", total_travel_time, "seconds")

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("The mean travel time is:", mean_travel_time, "seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("The user Types are:\n", user_types)

    # TO DO: Display counts of gender
    # i added a check if gender exists
    if "Gender" in df.columns:
        gender_counts = df["Gender"].value_counts()
        print("Gender counts:\n", gender_counts)
    else:
        print("Gender data doesnt exist")

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:  # checks if 'Birth Year' column exists
        earliest_year_of_birth = df["Birth Year"].min()
        most_recent_year_of_birth = df["Birth Year"].max()
        most_common_year_of_birth = df["Birth Year"].value_counts().idxmax()
        print("The earliest year of birth is:", earliest_year_of_birth)
        print("The most recent year of birth is:", most_recent_year_of_birth)
        print("The most common year of birth is:", most_common_year_of_birth)
    else:
        print("The birth Year data doesnt exist.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    main()
