
# coding: utf-8

# ### Read Dataset: Gun Deaths in the US

# In[1]:


import csv
f = open("guns.csv", "r")
data = list(csv.reader(f))



# In[2]:


print(data[:5])


# ### Remove Header from Dataset

# In[3]:


headers = data[:1]
data = data[1:]


# In[4]:


print(headers)
print(data[:5])


# ### List Comprehension to Extract Yearly Counts

# In[5]:


years = [row[1] for row in data]
year_counts = {}

for value in years:
    if value not in year_counts:
       year_counts[value] = 1
    else:
        year_counts[value] += 1

year_counts


# ### List Comprehension to Explore by Month & Year

# In[6]:


import datetime

dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]
dates[:5]



# In[7]:


date_counts = {}

for date in dates:
    if date not in date_counts:
        date_counts[date] = 1
    else:
        date_counts[date] += 1

date_counts


# ### Identifying Gender & Race Counts

# In[8]:


sex_counts = {}
sex_gender = [row[5] for row in data]

for sex in sex_gender:
    if sex not in sex_counts:
        sex_counts[sex] = 0
    sex_counts[sex] += 1
    
sex_counts


# In[9]:


race_counts = {}
races = [row[7] for row in data]

for race in races:
    if race not in race_counts:
        race_counts[race] = 0
    race_counts[race] += 1
    
race_counts


# ### Reading Second Dataset

# In[10]:


c = open("census.csv", "r")
census = list(csv.reader(c))
print(census)


# ### Rates of Gun Deaths per Race

# In[11]:


mapping = {'Asian/Pacific Islander': 15159516 + 674625 ,
 'Black': 40250635,
 'Hispanic': 44618105,
 'Native American/Native Alaskan': 3739506,
 'White': 197318956}

race_per_hundredk = {}

for race, population in race_counts.items():
    race_per_hundredk[race] = (population / mapping[race]) * 100000

race_per_hundredk


# ### Rate of Homicides per Race 

# In[12]:


intents = [row[3] for row in data]
homicide_race_counts = {}

for i, race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i] == "Homicide":
        homicide_race_counts[race] += 1

homicide_per_hundredk = {}   
        
for race, count in homicide_race_counts.items():
    homicide_per_hundredk[race] = (count/mapping[race]) * 100000

homicide_per_hundredk


# ### Key Findings
# 
# Most victims of gun related fatalities in relation to race are White (66,237), followed by Black (23,296). However, when exploring deaths due to "homicide" taking into consideration the rate of victims per 100,000 population, most fatalities are incurred by Black (48.4), followed by Hispanics (12.6). 

# ## Filtered by Intent Rate Calculator

# In[13]:


total_population = sum([mapping[population] for population in mapping])

def rate_calculator(column, intent_name):
    data_column = [row[column] for row in data]
    intent_count = {}

    for i, datapoint in enumerate(data_column):
        if datapoint not in intent_count:
            intent_count[datapoint] = 0
        if intents[i] == intent_name:
            intent_count[datapoint] += 1

    for item, count in intent_count.items():
        intent_count[item] = (count/total_population) * 100000
            
    return intent_count
    
homicide_monthly_rate = rate_calculator(2, "Homicide")
print(homicide_monthly_rate,"\n")

homicide_gender_rate = rate_calculator(5, "Homicide")
print(homicide_gender_rate, "\n")

accidental_monthly_rate = rate_calculator(2, "Accidental")
print(accidental_monthly_rate, "\n")

accidental_gender_rate = rate_calculator(5, "Accidental")
print(accidental_gender_rate, "\n")


# ## Filtered by Intent Rate Calculator (Valid for Race)

# In[14]:


def race_rate_calc(column, intent_name):
    data_column = [row[column] for row in data]
    intent_type = intent_name
    intent_racial_count = {}

    for i, datapoint in enumerate(data_column):
        if datapoint not in intent_racial_count:
            intent_racial_count[datapoint] = 0
        if intents[i] == intent_type:
            intent_racial_count[datapoint] += 1

    for datapoint, count in intent_racial_count.items():
        intent_racial_count[datapoint] = (count/mapping[datapoint]) * 100000
            
    return intent_racial_count

accidental_race_rate = race_rate_calc(7, "Accidental")
print(accidental_race_rate, "\n")

suicide_race_rate = race_rate_calc(7, "Suicide")
print(suicide_race_rate, "\n")

undertermined_race_rate = race_rate_calc(7, "Undetermined")
print(undertermined_race_rate, "\n")


# ### Gun Death Rate Correlation (Location & Education)

# In[15]:


location = [row[9] for row in data]
education = [row[10] for row in data]

location_types = set(location)
location_dict = {}
counter = 1

for place in location_types:
    location_dict[place] = counter
    counter = counter + 1

location_int = [location_dict[value] for value in location]

for level, i in enumerate(education):
      if i == 'NA':
         education[level] = '5'

education_int = [int(i) for i in education]


# In[16]:


import pandas as pd
corr_lst1 = list(zip(education_int, location_int))
corr_lst = pd.DataFrame(corr_lst1, columns=['Education', 'Location'])
corr_lst

corr_lst.corr()

