from pyecharts.charts import Bar

bar = Bar()
bar.add_xaxis(["shirt", "Cardigan", "Chiffon shirt", "trousers", "High-heeled shoes", "Socks"])
bar.add_yaxis("business A", [5, 20, 36, 10, 75, 90])
# Render generates a local HTML file, which by default generates a render.html file in the current directory
# You can also pass in path parameters, such as bar.render("mycharts.html")
bar.render()