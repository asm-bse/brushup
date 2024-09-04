import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./docs/PrepHomework_data.csv')

corruption = df['corruption']
social_media_penetration = df['socialnetshare']


plt.figure(figsize=(10, 6))
plt.scatter(social_media_penetration, corruption, color='blue')
plt.title('Correlation between Social Media Penetration and Corruption')
plt.xlabel('Social Media Penetration')
plt.ylabel('Corruption Index')
plt.grid(True)
plt.show()

df['gdp_quintile'] = pd.qcut(df['lngdp'], 5, labels=False) + 1


top_quintile = df[df['gdp_quintile'] == 5]


bottom_quintile = df[df['gdp_quintile'] == 1]


plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.scatter(top_quintile['socialnetshare'], top_quintile['corruption'], color='blue')
plt.title('Top Quintile: Social Media Penetration vs. Corruption')
plt.xlabel('Social Media Penetration')
plt.ylabel('Corruption Index')
plt.grid(True)


plt.subplot(1, 2, 2)
plt.scatter(bottom_quintile['socialnetshare'], bottom_quintile['corruption'], color='red')
plt.title('Bottom Quintile: Social Media Penetration vs. Corruption')
plt.xlabel('Social Media Penetration')
plt.ylabel('Corruption Index')
plt.grid(True)

plt.tight_layout()
plt.show()
