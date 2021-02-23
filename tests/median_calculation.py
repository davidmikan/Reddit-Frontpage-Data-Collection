import pandas as pd

complete_set = pd.read_csv('dataset/datapoints_complete.csv')

# die pandas.DataFrame.median Methode liefert den Median, praktisch!
dead_median = complete_set.loc[complete_set['State']=='dead']['Ratio'].median()
rising_median = complete_set.loc[complete_set['State']=='rising']['Ratio'].median()
hot_median = complete_set.loc[complete_set['State']=='hot']['Ratio'].median()

print('dead\trising\thot')
print(f'{dead_median}\t{rising_median}\t{hot_median}')