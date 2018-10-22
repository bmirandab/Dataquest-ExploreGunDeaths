## Dataquest.io - Guided Project: Exploring Gun Deaths in the US
Instructions from Dataquest.io for exercises corresponding to "Guided Project: Exploring Gun Deaths in the US". In the Jupyter and Python code attached you will find **my** solution to the exercises. There are many ways to solve the problems, these were my attempts.

### 1: Introduction to Dataset
1. Read the dataset in as a list using the csv module.
* Import the csv module.
* Open the file using the open() function.
* Use the csv.reader() function to load the opened file.
2. Call list() on the result to get a list of all the data in the file.
* Assign the result to the variable data.
3. Display the first 5 rows of data to verify everything.

### 2: Eliminating Headers
1. Extract the first row of data, and assign it to the variable headers.
2. Remove the first row from data.
3. Display headers.
4. Display the first 5 rows of data to verify that you removed the header row properly.

### 3: List Comprehension
1. Use a list comprehension to extract the year column from data.
* Because the year column is the second column in the data, you'll need to get the element at index 1 in each row.
* Assign the result to the variable years.
2. Create an empty dictionary called year_counts.
3. Loop through each element in years.
* If the element isn't a key in year_counts, create it, and set the value to 1.
* If the element is a key in year_counts, increment the value by one.
4. Display year_counts to see how many gun deaths occur in each year.

### 4: List Comprehension with datetime.datetime
1. Use a list comprehension to create a datetime.datetime object for each row. Assign the result to dates.
* The year column is in the second element in each row.
* The month column is the third element in each row.
* Make sure to convert year and month to integers using int().
* Pass year, month, and day=1 into the datetime.datetime() function.
2. Display the first 5 rows in dates to verify everything worked.
3. Count up how many times each unique date occurs in dates. Assign the result to date_counts.
* This follows a similar procedure to what we did in the last screen with year_counts.
4. Display date_counts.

### 5: Item counts
1. Count up how many times each item in the sex column occurs.
* Assign the result to sex_counts.
2. Count up how many times each item in the race column occurs.
* Assign the result to race_counts.
3. Display race_counts and sex_counts to verify your work, and see if you can spot any patterns.
4. Write a markdown cell detailing what you've learned so far, and what you think might need further examination.
  
### 6: Importing another dataset
1. Read in census.csv, and convert to a list of lists. Assign the result to the census variable.
2. Display census to verify your work.

### 7: Rates by 10,000
1. Manually create a dictionary, mapping that maps each key from race_counts to the population count of the race from census.
* The keys in the dictionary should be Asian/Pacific Islander, Black, Native American/Native Alaskan, Hispanic, and White.
* In the case of Asian/Pacific Islander, you'll need to add the counts from census for Race Alone - Asian, and Race Alone - Native Hawaiian and Other Pacific Islander.
2. Create an empty dictionary, race_per_hundredk.
3. Loop through each key in race_counts.
* Divide the value associated with the key in race_counts by the value associated with the key in mapping.
* Multiply by 100000.
* Assign the result to the same key in race_per_hundredk.
4. When you're done, race_per_hundredk should contain the rate of gun deaths per 100000 people for each racial category.
5. Print race_per_hundredk to verify your work.

### 8: Filtering by Intent
1. Extract the intent column using a list comprehension. The intent column is the fourth column in data.
* Assign the result to intents.
2. Extract the race column using a list comprehension. The race column is the eighth column in data.
* Assign the result to races.
3. Create an empty dictionary called homicide_race_counts
4. Use the enumerate() function to loop through each item in races. The position should be assigned to the loop variable i, and the value to the loop variable race.
* Check the value at position i in intents.
* If the value at position i in intents is Homicide:
  * If the key race doesn't exist in homicide_race_counts, create it.
  * Add 1 to the value associated with race in homicide_race_counts.
5. When you're done, homicide_race_counts should have one key for each of the racial categories in data. The associated value should be the number of gun deaths by homicide for that race.
6. Perform the same procedure we did in the last screen using mapping on homicide_race_counts to get from raw numbers to rates per 100000.
7. Display homicide_race_counts to verify your work.
8. Write up your findings in a markdown cell.
9. Write up any next steps you want to pursue with the data in a markdown cell.

### 8: Further Exploration of Data
1. Figure out the link, if any, between month and homicide rate.
2. Explore the homicide rate by gender.
3. Explore the rates of other intents, like Accidental, by gender and race.
4. Find out if gun death rates correlate to location and education.
