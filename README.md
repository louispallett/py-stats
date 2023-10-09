# py-stats
#### _A basic analysis of UK Smoking Stats_

This is a simple analysis of some statistics on a survey of UK nationals and their smoking habits.

- The .csv file with the raw data is found here: https://www.kaggle.com/datasets/utkarshx27/smoking-dataset-from-uk
- Only the 'smoking.csv' file is external. Everything else has been created by me.
- The source code contains a main.py file and the charts, which can be found in the charts/ directory.

## Analysis
#### _The Population_
The population contains a total of 1691 participants. They are split by smoking habits and gender as such:

![3 pie Charts displaying the population by smoking habits and gender](charts/gender.png)

Clearly, the most striking thing about this data is the fact that, despite this being a study on smoking habits, around *75%* of the participants do not smoke, meaning that conclusions drawn on the (comparatively) smaller population of smokers may not be as reliable as those drawn on non-smokers.
However, the split between gender, especially compared between smokers and non-smokers, is balenced. This makes the data a little more reliable when comparing the smokers and non-smokers by gender (but, it should still be noted, the number of - for example - female smokers is still much smaller than non-smokers, even if the percentages are more balanced).

We can also split both populations (smokers and non-smokers) by qualification. Doing so results in the following:

![2 pie Chart displaying smokers and non-smokers by highest qualification](charts/qualifications.png)

The only really significant difference is between the proportion of "Degrees" and "GCSEs" (which includes O Level and CSE), with nearly double the proportion of non-smokers having degrees. However, since the population of non-smokers is so much larger, this may simply be down to chance - a greater proportion of non-smokers, for example, have "No Qualification". So, displaying a relationship between qualifications and smoking habits using _this_ data is not possible.

#### _Smoking Habits_
Taking those who do smoke, we can plot their smoking habits verses their age by the number of times their smoke per day on weekends verses weekdays:

![2 scatter graphs displaying the number of times smokers smoke each day on weekdays verses the weekend](charts/habits.png)

Again, there isn't a stark difference between the two, but we do get a couple of anomalies - namely, the two plots at 60 times smoking a day in their 30s during the weekend.  