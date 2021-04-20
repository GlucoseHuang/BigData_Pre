import pyecharts.options as opts
from pyecharts.charts import Pie, Timeline
from pyecharts.faker import Faker

attr = Faker.choose()
tl = Timeline()
for i in range(2011, 2020):
    pie = (
        Pie(init_opts=opts.InitOpts(width="1200px", height="600px")).add(
            "Shop A",
            [list(z) for z in zip(attr, Faker.values())],
            rosetype="radius",
            radius=["30%", "55%"],
        )
    )
    tl.add(pie, f"{i}year")

tl.render("timeline_pie.html")
