import twitter

# example of search query
results = api.GetSearch(
    raw_query="q=%23superbowl&result_type=recent&count=100&lang=en&geocode=40.44,-79.94,30km")
    
def removeHTML(text):
    new = ''
    if "https://" in text:
        i = text.find("https://")
        new = text[:i-1]
    return new

for result in results[0:20]:
    print(removeHTML(result.text))

'''# get top five trend objects
trends = api.GetTrendsCurrent()[0:5]
trendNames = list()

# format top five real-time trends
for trend in trends:
    name = str(trend).split(",")[0]
    formatName = name.split(" ")[1]
    trendNames.append(formatName[1:-1])
# print(trendNames)'''