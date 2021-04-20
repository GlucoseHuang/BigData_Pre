from pyecharts.charts import Line
from pyecharts import options as opts

line = (
    Line()
        .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=False),
        legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=16)),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            min_="0.37",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
        .add_xaxis(xaxis_data=list(map(str, list(range(2014, 2017)))))
        .add_yaxis(
        series_name="China", y_axis=[0.43144843, 0.412704599, 0.398338597],
        is_symbol_show=True, label_opts=opts.LabelOpts(is_show=False),
    )
        .add_yaxis(
        series_name="Canada", y_axis=[0.407536355, 0.407608997, 0.391092225],
        is_symbol_show=True, label_opts=opts.LabelOpts(is_show=False),
    )
        .add_yaxis(
        series_name="Denmark", y_axis=[0.404137534, 0.412800639, 0.396844566],
        is_symbol_show=True, label_opts=opts.LabelOpts(is_show=False),
    )
        .add_yaxis(
        series_name="Austria", y_axis=[0.391126278, 0.394913664, 0.377246462],
        is_symbol_show=True, label_opts=opts.LabelOpts(is_show=False),
    )
        .add_yaxis(
        series_name="Hungary", y_axis=[0.423572765, 0.425600734, 0.40909463],
        is_symbol_show=True, label_opts=opts.LabelOpts(is_show=False),
    )
        .add_yaxis(
        series_name="Cyprus", y_axis=[0.410874696, 0.421765354, 0.395191687],
        is_symbol_show=True, label_opts=opts.LabelOpts(is_show=False),
    )
        .add_yaxis(
        series_name="Denmark", y_axis=[0.404137534, 0.412800639, 0.396844566],
        is_symbol_show=True, label_opts=opts.LabelOpts(is_show=False),
    )
        .add_yaxis(
        series_name="Germany", y_axis=[0.43535499, 0.431877898, 0.415396165],
        is_symbol_show=True, label_opts=opts.LabelOpts(is_show=False),
    )
        .add_yaxis(
        series_name="Poland", y_axis=[0.419207838, 0.423798193, 0.411165492],
        is_symbol_show=True, label_opts=opts.LabelOpts(is_show=False),
    )
)

# 将生成的图表保存到当前目录下
line.render("result.html")
