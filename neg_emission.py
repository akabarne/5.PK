import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()
sns.set_context("notebook", font_scale=1.25)
Arten = ('Braunkohle', 'Steinkohle', 'Erdgas', 'Geothermie')
pos = np.arange(len(Arten))
Emissionen = [2805.6, 1321.4, -1466, -3921.8]

colors = ['r' if e >= 0 else 'g' for e in Emissionen]

a = 1
plt.barh(pos, Emissionen, align='center', color = colors, edgecolor='black', alpha=a)
plt.axvline(x=5, ymin=0.0, ymax=1.0, color='black')
plt.axvline(x=-4000, ymin=0.0, ymax=1.0, color='green', ls=':')
plt.axvline(x=2805.6, ymin=0.0, ymax=1.0, color='grey', ls=':')
plt.axvline(x=-1466, ymin=0.0, ymax=1.0, color='grey', ls=':')
plt.axvline(x=-3921.8, ymin=0.0, ymax=1.0, color='grey', ls=':')
plt.axvline(x=1321.4, ymin=0.0, ymax=1.0, color='grey', ls=':')



plt.yticks(pos, Arten, fontsize=12)
plt.xlabel('CO$_2$ Ausstoß/Jahr in t', fontsize=12)



plt.tight_layout(pad=0.1)
plt.show()

