{"filter":false,"title":"helpers.py","tooltip":"/pset6/sentiments/helpers.py","ace":{"folds":[],"scrolltop":731.000093460083,"scrollleft":0,"selection":{"start":{"row":52,"column":59},"end":{"row":52,"column":59},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":20,"state":"start","mode":"ace/mode/python"}},"hash":"ebdfe5862c6a8f33c5afeda8c42d1681ff7ed46d","undoManager":{"mark":94,"position":94,"stack":[[{"start":{"row":0,"column":0},"end":{"row":66,"column":0},"action":"remove","lines":["import html","import os","import plotly","import socket","","from twython import Twython","from twython import TwythonAuthError, TwythonError, TwythonRateLimitError","","def chart(positive, negative, neutral):","    \"\"\"Return a pie chart for specified sentiments as HTML.\"\"\"","","    # offline plot","    # https://plot.ly/python/pie-charts/","    # https://plot.ly/python/reference/#pie","    figure = {","        \"data\": [","            {","                \"labels\": [\"positive\", \"negative\", \"neutral\"],","                \"hoverinfo\": \"none\",","                \"marker\": {","                    \"colors\": [","                        \"rgb(0,255,00)\",","                        \"rgb(255,0,0)\",","                        \"rgb(255,255,0)\"","                    ]","                },","                \"type\": \"pie\",","                \"values\": [positive, negative, neutral]","            }","        ],","        \"layout\": {","            \"showlegend\": True","            }","    }","    return plotly.offline.plot(figure, output_type=\"div\", show_link=False, link_text=False)","","def get_user_timeline(screen_name, count=200):","    \"\"\"Return list of most recent tweets posted by screen_name.\"\"\"","","    # ensure count is valid","    if count < 1 or count > 200:","        raise RuntimeError(\"invalid count\")","","    # ensure environment variables are set","    if not os.environ.get(\"API_KEY\"):","        raise RuntimeError(\"API_KEY not set\")","    if not os.environ.get(\"API_SECRET\"):","        raise RuntimeError(\"API_SECRET not set\")","","    # get screen_name's (or @screen_name's) most recent tweets","    # https://dev.twitter.com/rest/reference/get/users/lookup","    # https://dev.twitter.com/rest/reference/get/statuses/user_timeline","    # https://github.com/ryanmcgrath/twython/blob/master/twython/endpoints.py","    try:","        twitter = Twython(os.environ.get(\"API_KEY\"), os.environ.get(\"API_SECRET\"))","        user = twitter.lookup_user(screen_name=screen_name.lstrip(\"@\"))","        if user[0][\"protected\"]:","            return None","        tweets = twitter.get_user_timeline(screen_name=screen_name, count=count)","        return [html.unescape(tweet[\"text\"].replace(\"\\n\", \" \")) for tweet in tweets]","    except TwythonAuthError:","        raise RuntimeError(\"invalid API_KEY and/or API_SECRET\") from None","    except TwythonRateLimitError:","        raise RuntimeError(\"you've hit a rate limit\") from None","    except TwythonError:","        return None",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":66,"column":0},"action":"insert","lines":["import html","import os","import plotly","import socket","","from twython import Twython","from twython import TwythonAuthError, TwythonError, TwythonRateLimitError","","def chart(positive, negative, neutral):","    \"\"\"Return a pie chart for specified sentiments as HTML.\"\"\"","","    # offline plot","    # https://plot.ly/python/pie-charts/","    # https://plot.ly/python/reference/#pie","    figure = {","        \"data\": [","            {","                \"labels\": [\"positive\", \"negative\", \"neutral\"],","                \"hoverinfo\": \"none\",","                \"marker\": {","                    \"colors\": [","                        \"rgb(0,255,00)\",","                        \"rgb(255,0,0)\",","                        \"rgb(255,255,0)\"","                    ]","                },","                \"type\": \"pie\",","                \"values\": [positive, negative, neutral]","            }","        ],","        \"layout\": {","            \"showlegend\": True","            }","    }","    return plotly.offline.plot(figure, output_type=\"div\", show_link=False, link_text=False)","","def get_user_timeline(screen_name, count=200):","    \"\"\"Return list of most recent tweets posted by screen_name.\"\"\"","","    # ensure count is valid","    if count < 1 or count > 200:","        raise RuntimeError(\"invalid count\")","","    # ensure environment variables are set","    if not os.environ.get(\"API_KEY\"):","        raise RuntimeError(\"API_KEY not set\")","    if not os.environ.get(\"API_SECRET\"):","        raise RuntimeError(\"API_SECRET not set\")","","    # get screen_name's (or @screen_name's) most recent tweets","    # https://dev.twitter.com/rest/reference/get/users/lookup","    # https://dev.twitter.com/rest/reference/get/statuses/user_timeline","    # https://github.com/ryanmcgrath/twython/blob/master/twython/endpoints.py","    try:","        twitter = Twython(os.environ.get(\"API_KEY\"), os.environ.get(\"API_SECRET\"))","        user = twitter.lookup_user(screen_name=screen_name.lstrip(\"@\"))","        if user[0][\"protected\"]:","            return None","        tweets = twitter.get_user_timeline(screen_name=screen_name, count=count)","        return [html.unescape(tweet[\"text\"].replace(\"\\n\", \" \")) for tweet in tweets]","    except TwythonAuthError:","        raise RuntimeError(\"invalid API_KEY and/or API_SECRET\") from None","    except TwythonRateLimitError:","        raise RuntimeError(\"you've hit a rate limit\") from None","    except TwythonError:","        return None",""],"id":2}],[{"start":{"row":66,"column":0},"end":{"row":67,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":67,"column":0},"end":{"row":68,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":68,"column":0},"end":{"row":68,"column":1},"action":"insert","lines":["g"],"id":5}],[{"start":{"row":68,"column":1},"end":{"row":68,"column":2},"action":"insert","lines":["e"],"id":6}],[{"start":{"row":68,"column":2},"end":{"row":68,"column":3},"action":"insert","lines":["t"],"id":7}],[{"start":{"row":68,"column":3},"end":{"row":68,"column":4},"action":"insert","lines":["_"],"id":8}],[{"start":{"row":68,"column":4},"end":{"row":68,"column":5},"action":"insert","lines":["u"],"id":9}],[{"start":{"row":68,"column":5},"end":{"row":68,"column":6},"action":"insert","lines":["s"],"id":10}],[{"start":{"row":68,"column":6},"end":{"row":68,"column":7},"action":"insert","lines":["e"],"id":11}],[{"start":{"row":68,"column":7},"end":{"row":68,"column":8},"action":"insert","lines":["r"],"id":12}],[{"start":{"row":68,"column":8},"end":{"row":68,"column":9},"action":"insert","lines":["_"],"id":13}],[{"start":{"row":68,"column":9},"end":{"row":68,"column":10},"action":"insert","lines":["t"],"id":14}],[{"start":{"row":68,"column":10},"end":{"row":68,"column":11},"action":"insert","lines":["i"],"id":15}],[{"start":{"row":68,"column":11},"end":{"row":68,"column":12},"action":"insert","lines":["m"],"id":16}],[{"start":{"row":68,"column":12},"end":{"row":68,"column":13},"action":"insert","lines":["e"],"id":17}],[{"start":{"row":68,"column":13},"end":{"row":68,"column":14},"action":"insert","lines":["l"],"id":18}],[{"start":{"row":68,"column":14},"end":{"row":68,"column":15},"action":"insert","lines":["i"],"id":19}],[{"start":{"row":68,"column":15},"end":{"row":68,"column":16},"action":"insert","lines":["n"],"id":20}],[{"start":{"row":68,"column":16},"end":{"row":68,"column":17},"action":"insert","lines":["e"],"id":21}],[{"start":{"row":68,"column":17},"end":{"row":68,"column":19},"action":"insert","lines":["()"],"id":22}],[{"start":{"row":68,"column":18},"end":{"row":68,"column":20},"action":"insert","lines":["\"\""],"id":23}],[{"start":{"row":68,"column":19},"end":{"row":68,"column":20},"action":"insert","lines":["@"],"id":24}],[{"start":{"row":68,"column":20},"end":{"row":68,"column":21},"action":"insert","lines":["c"],"id":25}],[{"start":{"row":68,"column":21},"end":{"row":68,"column":22},"action":"insert","lines":["s"],"id":26}],[{"start":{"row":68,"column":22},"end":{"row":68,"column":23},"action":"insert","lines":["5"],"id":27}],[{"start":{"row":68,"column":23},"end":{"row":68,"column":24},"action":"insert","lines":["0"],"id":28}],[{"start":{"row":68,"column":25},"end":{"row":68,"column":26},"action":"insert","lines":[","],"id":29}],[{"start":{"row":68,"column":26},"end":{"row":68,"column":27},"action":"insert","lines":["2"],"id":30}],[{"start":{"row":68,"column":26},"end":{"row":68,"column":27},"action":"remove","lines":["2"],"id":31}],[{"start":{"row":68,"column":26},"end":{"row":68,"column":27},"action":"insert","lines":["1"],"id":32}],[{"start":{"row":68,"column":27},"end":{"row":68,"column":28},"action":"insert","lines":["0"],"id":33}],[{"start":{"row":68,"column":28},"end":{"row":68,"column":29},"action":"insert","lines":["0"],"id":34}],[{"start":{"row":68,"column":23},"end":{"row":68,"column":24},"action":"insert","lines":["i"],"id":35}],[{"start":{"row":68,"column":24},"end":{"row":68,"column":25},"action":"insert","lines":["d"],"id":36}],[{"start":{"row":68,"column":25},"end":{"row":68,"column":26},"action":"insert","lines":["e"],"id":37}],[{"start":{"row":68,"column":26},"end":{"row":68,"column":27},"action":"insert","lines":["f"],"id":38}],[{"start":{"row":68,"column":27},"end":{"row":68,"column":28},"action":"insert","lines":["o"],"id":39}],[{"start":{"row":68,"column":28},"end":{"row":68,"column":29},"action":"insert","lines":["i"],"id":40}],[{"start":{"row":68,"column":29},"end":{"row":68,"column":30},"action":"insert","lines":["e"],"id":41}],[{"start":{"row":68,"column":30},"end":{"row":68,"column":31},"action":"insert","lines":["f"],"id":42}],[{"start":{"row":68,"column":31},"end":{"row":68,"column":32},"action":"insert","lines":["h"],"id":43}],[{"start":{"row":67,"column":0},"end":{"row":67,"column":1},"action":"insert","lines":["i"],"id":44}],[{"start":{"row":67,"column":1},"end":{"row":67,"column":2},"action":"insert","lines":["f"],"id":45}],[{"start":{"row":67,"column":2},"end":{"row":67,"column":3},"action":"insert","lines":[" "],"id":46}],[{"start":{"row":67,"column":3},"end":{"row":67,"column":4},"action":"insert","lines":["_"],"id":47}],[{"start":{"row":67,"column":4},"end":{"row":67,"column":5},"action":"insert","lines":["_"],"id":48}],[{"start":{"row":67,"column":5},"end":{"row":67,"column":6},"action":"insert","lines":["n"],"id":49}],[{"start":{"row":67,"column":6},"end":{"row":67,"column":7},"action":"insert","lines":["a"],"id":50}],[{"start":{"row":67,"column":7},"end":{"row":67,"column":8},"action":"insert","lines":["m"],"id":51}],[{"start":{"row":67,"column":8},"end":{"row":67,"column":9},"action":"insert","lines":["e"],"id":52}],[{"start":{"row":67,"column":9},"end":{"row":67,"column":10},"action":"insert","lines":["_"],"id":53}],[{"start":{"row":67,"column":10},"end":{"row":67,"column":11},"action":"insert","lines":["_"],"id":54}],[{"start":{"row":67,"column":11},"end":{"row":67,"column":12},"action":"insert","lines":[" "],"id":55}],[{"start":{"row":67,"column":12},"end":{"row":67,"column":13},"action":"insert","lines":["="],"id":56}],[{"start":{"row":67,"column":13},"end":{"row":67,"column":14},"action":"insert","lines":["="],"id":57}],[{"start":{"row":67,"column":14},"end":{"row":67,"column":15},"action":"insert","lines":[" "],"id":58}],[{"start":{"row":67,"column":15},"end":{"row":67,"column":17},"action":"insert","lines":["\"\""],"id":59}],[{"start":{"row":67,"column":16},"end":{"row":67,"column":17},"action":"insert","lines":["_"],"id":60}],[{"start":{"row":67,"column":17},"end":{"row":67,"column":18},"action":"insert","lines":["_"],"id":61}],[{"start":{"row":67,"column":18},"end":{"row":67,"column":19},"action":"insert","lines":["m"],"id":62}],[{"start":{"row":67,"column":19},"end":{"row":67,"column":20},"action":"insert","lines":["a"],"id":63}],[{"start":{"row":67,"column":20},"end":{"row":67,"column":21},"action":"insert","lines":["i"],"id":64}],[{"start":{"row":67,"column":21},"end":{"row":67,"column":22},"action":"insert","lines":["n"],"id":65}],[{"start":{"row":67,"column":22},"end":{"row":67,"column":23},"action":"insert","lines":["_"],"id":66}],[{"start":{"row":67,"column":23},"end":{"row":67,"column":24},"action":"insert","lines":["_"],"id":67}],[{"start":{"row":67,"column":25},"end":{"row":67,"column":26},"action":"insert","lines":[":"],"id":68}],[{"start":{"row":67,"column":26},"end":{"row":68,"column":0},"action":"insert","lines":["",""],"id":69},{"start":{"row":68,"column":0},"end":{"row":68,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":69,"column":0},"end":{"row":69,"column":4},"action":"insert","lines":["    "],"id":70}],[{"start":{"row":68,"column":0},"end":{"row":68,"column":4},"action":"remove","lines":["    "],"id":71}],[{"start":{"row":67,"column":0},"end":{"row":69,"column":43},"action":"remove","lines":["if __name__ == \"__main__\":","","    get_user_timeline(\"@cs5idefoiefh0\",100)"],"id":72}],[{"start":{"row":58,"column":80},"end":{"row":59,"column":0},"action":"insert","lines":["",""],"id":73},{"start":{"row":59,"column":0},"end":{"row":59,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":58,"column":8},"end":{"row":59,"column":0},"action":"insert","lines":["",""],"id":74},{"start":{"row":59,"column":0},"end":{"row":59,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":58,"column":4},"end":{"row":58,"column":8},"action":"remove","lines":["    "],"id":75}],[{"start":{"row":58,"column":0},"end":{"row":58,"column":4},"action":"remove","lines":["    "],"id":76}],[{"start":{"row":57,"column":23},"end":{"row":58,"column":0},"action":"remove","lines":["",""],"id":77}],[{"start":{"row":59,"column":4},"end":{"row":59,"column":8},"action":"remove","lines":["    "],"id":78}],[{"start":{"row":59,"column":0},"end":{"row":59,"column":4},"action":"remove","lines":["    "],"id":79}],[{"start":{"row":58,"column":80},"end":{"row":59,"column":0},"action":"remove","lines":["",""],"id":80}],[{"start":{"row":55,"column":71},"end":{"row":56,"column":0},"action":"insert","lines":["",""],"id":81},{"start":{"row":56,"column":0},"end":{"row":56,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":56,"column":4},"end":{"row":56,"column":8},"action":"remove","lines":["    "],"id":82}],[{"start":{"row":56,"column":0},"end":{"row":56,"column":4},"action":"remove","lines":["    "],"id":83}],[{"start":{"row":55,"column":71},"end":{"row":56,"column":0},"action":"remove","lines":["",""],"id":84}],[{"start":{"row":58,"column":80},"end":{"row":59,"column":0},"action":"insert","lines":["",""],"id":85},{"start":{"row":59,"column":0},"end":{"row":59,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":60,"column":4},"end":{"row":60,"column":8},"action":"remove","lines":["    "],"id":86}],[{"start":{"row":60,"column":0},"end":{"row":60,"column":4},"action":"remove","lines":["    "],"id":87}],[{"start":{"row":59,"column":8},"end":{"row":60,"column":0},"action":"remove","lines":["",""],"id":88}],[{"start":{"row":60,"column":4},"end":{"row":61,"column":0},"action":"insert","lines":["",""],"id":89},{"start":{"row":61,"column":0},"end":{"row":61,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":63,"column":4},"end":{"row":64,"column":0},"action":"insert","lines":["",""],"id":90},{"start":{"row":64,"column":0},"end":{"row":64,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":66,"column":4},"end":{"row":67,"column":0},"action":"insert","lines":["",""],"id":91},{"start":{"row":67,"column":0},"end":{"row":67,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":58,"column":4},"end":{"row":59,"column":0},"action":"insert","lines":["",""],"id":92},{"start":{"row":59,"column":0},"end":{"row":59,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":56,"column":4},"end":{"row":57,"column":0},"action":"insert","lines":["",""],"id":93},{"start":{"row":57,"column":0},"end":{"row":57,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":54,"column":4},"end":{"row":55,"column":0},"action":"insert","lines":["",""],"id":94},{"start":{"row":55,"column":0},"end":{"row":55,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":54,"column":0},"end":{"row":54,"column":4},"action":"remove","lines":["    "],"id":95},{"start":{"row":57,"column":0},"end":{"row":57,"column":4},"action":"remove","lines":["    "]},{"start":{"row":60,"column":0},"end":{"row":60,"column":4},"action":"remove","lines":["    "]},{"start":{"row":63,"column":0},"end":{"row":63,"column":4},"action":"remove","lines":["    "]},{"start":{"row":66,"column":0},"end":{"row":66,"column":4},"action":"remove","lines":["    "]},{"start":{"row":69,"column":0},"end":{"row":69,"column":4},"action":"remove","lines":["    "]}]]},"timestamp":1512550863946}