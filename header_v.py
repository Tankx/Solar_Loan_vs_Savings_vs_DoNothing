# This is the header file that is imported into all scripts

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler
import time
import datetime
from IPython.display import display, HTML

# Create a custom dictionary class with self as __dict__
class DDict(dict):
    def __init__(self, **kwargs):
        self.update(kwargs)
        self.__dict__ = self

# Initialize directory paths
Dirs = DDict(drive_loc=None, current=os.getcwd())

drive_path_parts = Dirs.current.split("\\")
# Provide a default value for next() to avoid StopIteration exception
drive_part = next((part for part in drive_path_parts if 'drive' in part.lower()), None)

if drive_part:
    drive_path = '\\\\'.join(drive_path_parts[: drive_path_parts.index(drive_part) + 1])
    Dirs.drive_loc = os.path.abspath(drive_path)
else:
    # Handle the case when no 'drive' part is found
    # You can customize this part based on your requirements
    print("No 'drive' directory found along the path. The 'Dirs.drive_loc' directory will be set to current directory.")
    drive_path = None
    Dirs.drive_loc = Dirs.current
Dirs.one_back = os.path.dirname(Dirs.current)

# Clean up temporary variables
del drive_path_parts, drive_path

# Some Line style stuff
    # Define custom linestyles using a cycler object
    # The cycler object will cycle through the specified linestyles
    # Linestyles include: solid, dashed, dotted, dash-dot,
    # long dash short dash, dash space dot space,
    # long dash short dash dot, dot space dot long space,
    # long dash double space short dash double space
custom_linestyles = cycler('linestyle', ['-', '--', ':', '-.', (0, (8, 2, 2, 2)), (0, (5, 2, 1, 2)), (0, (8, 2, 2, 2, 1, 2)), (0, (1, 2, 1, 4)), (0, (8, 4, 2, 4))])
plt.rc('axes', prop_cycle=(custom_linestyles)) 
# Apply the custom linestyle cycler to the plot's axes
# This will affect all subsequent plots created in the script

google_colors = [
    '#a93329',  # dark red
    '#e3b73c',  # dark yellow
    '#0c9458',  # dark green
    '#2154ac',  # dark blue
    '#d94234',  # light red
    '#ffd200',  # light yellow
    '#378fdd',  # light blue
    '#0ca55f',  # light green
    '#6b3e26',  # dark brown
    '#eac100',  # dark gold
    '#207178',  # dark teal
    '#3f2350',  # dark purple
    '#e17f32',  # light orange
    '#f3c300',  # light gold
    '#2c7aaf',  # light steel blue
    '#24a090',  # light sea green
    '#8b572a',  # brownish orange
    '#f06eaa',  # soft pink
    '#7ed321',  # lime green
    '#bd10e0',  # vibrant purple
    '#50e3c2',  # turquoise
    '#b8e986',  # light lime green
    '#4a90e2',  # medium blue
    '#9013fe',  # royal purple
]

colors = [
    ('dark red', '#a93329'),
    ('dark yellow', '#e3b73c'),
    ('dark green', '#0c9458'),
    ('dark blue', '#2154ac'),
    ('light red', '#d94234'),
    ('light yellow', '#ffd200'),
    ('light blue', '#378fdd'),
    ('light green', '#0ca55f'),
    ('dark brown', '#6b3e26'),
    ('dark gold', '#eac100'),
    ('dark teal', '#207178'),
    ('dark purple', '#3f2350'),
    ('light orange', '#e17f32'),
    ('light gold', '#f3c300'),
    ('light steel blue', '#2c7aaf'),
    ('light sea green', '#24a090'),
    ('brownish orange', '#8b572a'),
    ('soft pink', '#f06eaa'),
    ('lime green', '#7ed321'),
    ('vibrant purple', '#bd10e0'),
    ('turquoise', '#50e3c2'),
    ('light lime green', '#b8e986'),
    ('medium blue', '#4a90e2'),
    ('royal purple', '#9013fe'),
]




# Plotly tokens - https://www.mapbox.com/
plotly_token1 = "pk.eyJ1IjoidGFua3giLCJhIjoiY2sxbnAxa210MGNudDNtczBvcWp5M3NjZCJ9.V62gASFJHH68i3bfxiCHEw"
# plotly_token2 = "pk.eyJ1IjoidGFua3giLCJhIjoiY2pueXI3b255MDRiZDNqbWI0ZnVkeXowMiJ9.3YrwQ2KJMqI16PcRbsfQDw"
# plotly_token3 = "pk.eyJ1IjoidGFua3giLCJhIjoiY2pueXI5MWt0MDFkYzN2dDdtYm1vY2k2bSJ9.xtopABkqm1EZPPeMIB8CrA"


# Set pandas display options
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)


# Make screen usage wider
display(HTML(data="""
<style>
    div#notebook-container    { width: 95%; }
    div#menubar-container     { width: 65%; }
    div#maintoolbar-container { width: 99%; }
</style>
"""))
