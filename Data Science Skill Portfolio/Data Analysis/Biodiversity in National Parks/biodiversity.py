import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# setting pandas options
pd.set_option('display.max_columns', 500)

# reading in 'observations' and 'species_info' to dfs
species = pd.read_csv('species_info.csv', encoding='utf-8')
observations = pd.read_csv('observations.csv', encoding='utf-8')

# determining the data of
print(f'Species Columns: {species.columns}')
print(f'Observations Columns: {observations.columns}')
# species contains information on the animal species, including its name, scientific name, and conservation status
# observations are sightings of the species within the parks over the past week

# determining the dimensions of each dataset
print(f'Species Shape: {species.shape}')
print(f'Observations Shape: {observations.shape}')

## species_info.csv overview
# getting the number of categories in species
print(f'Number of categories in Species: {species.category.nunique()}')
print(f'Category types: {species.category.unique()}')

# determining the size of each category in species
print(species.groupby('category').size())

# conservation statues exploration
print(f'Number of conservation statuses:{species.conservation_status.nunique()}')
print(f'Conservation statuses:{species.conservation_status.unique()}')

# Note: nan values indicate species not in threat of extinction due to no conservation status
print(f'nan values: {species.conservation_status.isna().sum()}')
print(species.groupby('conservation_status').size())

## observations.csv overview
# determining the number of parks in the set
print(f'Number of parks: {observations.park_name.nunique()}')
print(f'Unique parks: {observations.park_name.unique()}')

# getting the total observations in the past week
print(f'Number of observations: {observations.observations.sum()}')

## Analysis
# changing the nan values in species to a new status 'No Concern'
species.fillna('No Concern', inplace=True)
print(species.groupby('conservation_status').size())

# filtering species based on status and then pivoting the table
conservationCategory = species[species.conservation_status != 'No Concern']\
	.groupby(['conservation_status', 'category'])['scientific_name']\
	.count()\
	.unstack()
print(conservationCategory)

# visualizing species based on conservation status
ax = conservationCategory.plot(kind = 'bar', figsize=(8,6),
                               stacked=True)
ax.set_xlabel("Conservation Status")
ax.set_ylabel("Number of Species")
plt.show()

## Are different species more likely to be protected on a per category basis?
# creating a column 'is_protected' based on exclusion of 'No Concern'
species['is_protected'] = species.conservation_status != 'No Concern'
category_counts = species.groupby(['category', 'is_protected'])\
                        .scientific_name.nunique()\
                        .reset_index()\
                        .pivot(columns='is_protected',
                                      index='category',
                                      values='scientific_name')\
                        .reset_index()
category_counts.columns = ['category', 'not_protected', 'protected']
print(category_counts)

# determining percent protected per category
category_counts['percent_protected'] = category_counts.protected / \
                                      (category_counts.protected + category_counts.not_protected) * 100
print(category_counts)