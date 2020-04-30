from bokeh.embed import components
from bokeh.plotting import *
from numpy import pi

# define starts/ends for wedges from percentages of a circle
percents = [0, 0.3, 0.4, 0.6, 0.9, 1]
starts = [p*2*pi for p in percents[:-1]]
ends = [p*2*pi for p in percents[1:]]

# a color for each pie piece
colors = ["red", "green", "blue", "orange", "yellow"]

p = figure(x_range=(-1,1), y_range=(-1,1))

p.wedge(x=0, y=0, radius=1, start_angle=starts, end_angle=ends, color=colors)

# display/save everythin 
#p.plot_width=250
#p.plot_height=250

script, div = components(p)
#show(p)