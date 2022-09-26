#!/usr/bin/env python3.7.11
# -*- Coding: UTF-8 -*-

# conda deactivate
# conda create -n pvenv python=3.9
# conda activate pvenv
# conda install matplotlib pandas
# conda install -c pvlib pvlib
# conda env remove -n pvenv (para remover env)

# See more at https://pvlib-python.readthedocs.io/en/stable/reference/clearsky.html

import os
import itertools
import matplotlib.pyplot as plt
import pandas as pd
import pvlib
from pvlib import clearsky, atmosphere, solarposition
from pvlib.location import Location
from pvlib.iotools import read_tmy3

# lat, lon, timezone, alt(?) ; hora local, ja q informa TZ
#loc = Location(32.2, -111, 'US/Arizona', 700, 'Tucson')
loc = Location(-29.443, -53.823, tz='UTC', altitude=489, name='SMS')
#times = pd.date_range(start='2016-07-01', end='2016-07-04', freq='1min', tz=loc.tz)
times = pd.date_range(start='2015-02-08 09:00:00', end='2015-02-08 23:00:00', freq='5min', tz=loc.tz)
cs = loc.get_clearsky(times)  # ineichen with climatology table by default
cs.plot(linestyle=':', marker='o')
plt.ylabel('Irradiance $W/m^2$')
plt.title('Ineichen, climatological turbidity')
plt.savefig('cs.png', bbox_inches='tight')
