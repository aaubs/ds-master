# Datasets Descriptions

Data for this study was extracted using the Octoparse scraping tool from the "Ease My Trip" website. The dataset was collected in two parts, focusing on economy class tickets and business class tickets respectively. A total of 300261 distinct flight booking options were extracted. The data collection spanned 50 days, from February 11th to March 31st, 2022. The dataset comprises secondary data obtained exclusively from the "Ease My Trip" website. Below are the descriptions of each dataset:

## 1. `Clean_Dataset.csv`

This dataset contains information about various flight listings.

### Structure

- **Total Entries**: 300,153
- **Total Columns**: 12

### Columns

1. **Unnamed: 0** (Integer): An unnamed column, likely representing the row index.
2. **airline** (String): Name of the airline.
3. **flight** (String): Flight number or identifier.
4. **source_city** (String): City where the flight departs from.
5. **departure_time** (String): Time of day when the flight departs (e.g., Evening, Early_Morning).
6. **stops** (String): Number of stops or layovers.
7. **arrival_time** (String): Time of day when the flight arrives at the destination (e.g., Night, Morning).
8. **destination_city** (String): City where the flight arrives.
9. **class** (String): Class of the flight (e.g., Economy).
10. **duration** (Float): Duration of the flight in hours.
11. **days_left** (Integer): Number of days left until the flight.
12. **price** (Integer): Price of the flight ticket.


## 2. `business.csv`

This dataset contains information about various business class flight listings.

### Structure

- **Total Entries**: 93,487
- **Total Columns**: 11

### Columns

1. **date** (String): Date of the flight.
2. **airline** (String): Name of the airline.
3. **ch_code** (String): Airline code (character format).
4. **num_code** (Integer): Airline code (numeric format).
5. **dep_time** (String): Departure time of the flight.
6. **from** (String): City where the flight departs from.
7. **time_taken** (String): Duration of the flight (e.g., "02h 00m").
8. **stop** (String): Information about stops or layovers, including "non-stop" for direct flights.
9. **arr_time** (String): Arrival time of the flight.
10. **to** (String): City where the flight arrives.
11. **price** (String): Price of the flight ticket.


## 3. `economy.csv`

This dataset contains information about various economy class flight listings.

### Structure

- **Total Entries**: 206,774
- **Total Columns**: 11

### Columns

1. **date** (String): Date of the flight.
2. **airline** (String): Name of the airline.
3. **ch_code** (String): Airline code (character format).
4. **num_code** (Integer): Airline code (numeric format).
5. **dep_time** (String): Departure time of the flight.
6. **from** (String): City where the flight departs from.
7. **time_taken** (String): Duration of the flight (e.g., "02h 10m").
8. **stop** (String): Information about stops or layovers, including "non-stop" for direct flights.
9. **arr_time** (String): Arrival time of the flight.
10. **to** (String): City where the flight arrives.
11. **price** (String): Price of the flight ticket.





