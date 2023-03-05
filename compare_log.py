import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme()
sns.set_context("notebook", font_scale=1.25)
arten = ("Ausstoß weltweit", "DAC Reduktion")
pos = np.arange(len(arten))
print(pos)
emissionen = [37123850000, 4000]
werte = ["37.123.850.000t", "4000t"]

plt.axhline(y=37123850000, xmin=0.0, xmax=1, color='grey', ls=':')
plt.axhline(y=4000, xmin=0.0, xmax=1, color='grey', ls=':')
plt.bar(pos, emissionen,color =["red", "green"],
align='center', edgecolor='black', label = werte, alpha= 0.8)



plt.yscale("log")

plt.xticks(pos, arten, fontsize=12)
plt.ylabel('CO$_2$ in t', fontsize=12)

plt.tight_layout(pad=0.1)
plt.legend(loc=5)
plt.show()
