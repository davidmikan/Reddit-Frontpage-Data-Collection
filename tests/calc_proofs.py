import pandas as pd

complete_set = pd.read_csv('dataset/datapoints_complete.csv')

def ratio_medians():
    # Der Median der Upvote-Ratios getrennt nach State
    dead_median = complete_set.loc[complete_set['State']=='dead']['Ratio'].median()
    rising_median = complete_set.loc[complete_set['State']=='rising']['Ratio'].median()
    hot_median = complete_set.loc[complete_set['State']=='hot']['Ratio'].median()

    print('MEDIAN\ndead\trising\thot')
    print(f'{dead_median}\t{rising_median}\t{hot_median}')

def final_score_means():
    # Das arithmetische Mittel der Scores der jeweils letzten Datenpunkte jedes Posts
    # Der Parameter Time muss für diese Datenpunkte >140 sein, da sie ja das 15. Update darstellen,
    # demnach 14*10 Minuten davor verstrichen sind
    dead_mean = complete_set.loc[(complete_set['State']=='dead') & (complete_set['Time'] > 140)]['Score'].mean()
    rising_mean = complete_set.loc[(complete_set['State']=='rising') & (complete_set['Time'] > 140)]['Score'].mean()
    hot_mean = complete_set.loc[(complete_set['State']=='hot') & (complete_set['Time'] > 140)]['Score'].mean()

    print('MEAN\ndead\trising\thot')
    print(f'{dead_mean}\t{rising_mean}\t{hot_mean}')

if __name__=='__main__':
    ratio_medians()
    final_score_means()