import twitter

# example of search query
results = api.GetSearch(
    raw_query="q=%23superbowl&result_type=recent")
print(results)

# get top five trend objects
trends = api.GetTrendsCurrent()[0:5]
trendNames = list()

# format top five real-time trends
for trend in trends:
    name = str(trend).split(",")[0]
    formatName = name.split(" ")[1]
    trendNames.append(formatName[1:-1])
print(trendNames)