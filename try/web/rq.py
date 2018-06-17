import requests
import json
url = 'http://7.207.150.71:8000/rq'
data={
    'model':'TInsCaseMain',
    'filters':{
        'streetcode':1806,
        'status__in':[3 ,-2,-1],
    },
    'end':20
}
rt = requests.post(url,data=json.dumps(data))
print(rt.content)