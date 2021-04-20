import pyecharts.options as opts
from pyecharts.charts import Tree

data = [
    {
        "name": "信息管理",
        "children":
            [
                {
                    "name": "信息分布",
                    "children":
                        [
                            {"name": "马太效应", "value": "P1"},
                            {"name": "信息的离散分布规律", "value": "P2"},
                            {"name": "信息生产者的分布规律", "value": "P3"},
                            {"name": "信息对时间的分布规律", "value": "P4"}
                        ]
                },
                {
                    "name": "信息组织",
                    "children":
                        [
                            {"name": "体系分类法", "value": "P5"},
                            {"name": "组配分类法", "value": "P6"},
                            {"name": "网络信息的分类组织", "value": "P7"},
                            {"name": "知识组织", "value": "P8"}
                        ]
                },
                {
                    "name": "信息检索",
                    "children":
                        [
                            {"name": "信息检索模型", "value": "P9"},
                            {"name": "信息检索评价", "value": "P10"},
                            {"name": "信息检索工具", "value": "P11"},
                            {"name": "信息检索系统", "value": "P12"},
                        ]
                },
                {
                    "name": "信息系统",
                    "children":
                        [
                            {"name": "信息系统分析", "value": "P13"},
                            {"name": "信息系统评价", "value": "P14"},
                            {"name": "信息系统设计", "value": "P15"},
                            {"name": "信息系统管理", "value": "P16"},
                        ]
                }
            ]
    }
]

tree = Tree(init_opts=opts.InitOpts(width="1200px", height="600px")).add(
    "目录",
    data,
    collapse_interval=2,
    label_opts=opts.LabelOpts(
        position="top",
        horizontal_align="right",
        vertical_align="middle",
        font_size=24
    )
)

tree.render("tree.html")
