import plotnine as p9
import pandas as pd
import matplotlib.font_manager as fm
# from config import *

font = fm.FontProperties(fname='fonts/atkinson.ttf')
PLOT_NAME = 'time0-40_score_convex_all_final'

# dead = pd.read_csv('sub_scraper/datasets/datapoints_dead.csv')
# rising = pd.read_csv('sub_scraper/datasets/datapoints_rising.csv')
# hot = pd.read_csv('sub_scraper/datasets/datapoints_hot.csv')
complete_set = pd.read_csv('dataset/datapoints_complete.csv')
complete_set['State'] = complete_set['State'].astype('category').cat.reorder_categories(['dead', 'rising', 'hot'])

col = ['dead' if (not r and not h) else 'hot' if h else 'rising' for r, h in zip(complete_set['Rising'], complete_set['Hot'])]
complete_set['Color'] = col
complete_set['Color'] = complete_set['Color'].astype('category').cat.reorder_categories(['dead', 'rising', 'hot'])
# complete_set['Timeframes'] = pd.cut(complete_set['Score'], bins=[0, 200, 400, 600, 800, 1000, 20000])
# complete_set['Timeframes'] = complete_set['Timeframes'].astype('string')


plot = (p9.ggplot(data=complete_set.sample(10000),
           mapping=p9.aes(x='State', y='Color', color='State'))
        #       ---- THEMING ----
        # +
        # p9.xlim([0, 40])
        # +
        # p9.ylim([0, 300])
        +
        p9.scale_color_manual([dead, rising, hot])
        +
        p9.theme(
        text=p9.element_text(color=dark,fontproperties=font),
        plot_background=p9.element_rect(fill=light),
        legend_background=p9.element_rect(fill=light),
        legend_box_background=p9.element_rect(fill=light2),
        panel_background=p9.element_rect(fill=light2),
        strip_background=p9.element_rect(fill=light2),
        axis_title=p9.element_text(color=dark, fontproperties=font, margin={'t': 10, 'r': 10,}),
        legend_title=p9.element_text(linespacing=1.6, margin={'b':25}),
        )
        +
        p9.labs(
        title='Violiiin'
        )
        #       ---- VIOLIN PLOT -----  legend_position: 'none'
        +
        p9.geom_violin(fill=light, linetype='dashed', draw_quantiles = (0.25, 0.5, 0.75))
        +
        p9.geom_violin(fill=None, draw_quantiles=0.5)
        # +
        # p9.geom_violin(fill=light)
        #       ---- SCATTER PLOT -----
        # +
        # p9.geom_point(data=complete_set.loc[complete_set['State']=='dead'].sample(700), alpha=0.1, size=0.6)
        # +
        # p9.geom_point(data=complete_set.loc[complete_set['State']=='rising'].sample(1000), alpha=0.1, size=0.6)
        # +
        # p9.geom_point(data=complete_set.loc[complete_set['State']=='hot'], alpha=0.1, size=0.6)
        # +
        # p9.stat_hull()
        # +
        # p9.geom_smooth(color='black', alpha=0.4)
        #       ---- BIN PLOT ----
        # p9.geom_bin2d(data=complete_set.loc[complete_set['State']=='dead'].sample(1500), bins=50)
        # +
        # p9.geom_bin2d(data=complete_set.loc[complete_set['State']=='rising'], bins=50)
        # +
        # p9.geom_bin2d(data=complete_set.loc[complete_set['State']=='hot'], bins=50)
        #       ---- WRAP PER CATEGORY ----
        # +
        # p9.facets.facet_wrap('State')
)

# plot.save(
#     filename = GGPLOT_PATH+ PLOT_NAME +'.pdf',
#     format = 'pdf',
#     width = 6,
#     height = 4
#     )

print(plot)