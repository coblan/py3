import requests
import json
import base64
def get_tokent(): 
    appkey = 'yuanjingkey12345678910'
    url = 'http://222.73.31.135:8084/api?handler=token&key=%(appkey)s&method=getAccessToken' % {'appkey': appkey,}
    rt = requests.get(url)
    dc = json.loads(rt.content.decode('utf-8'))
    return dc.get('data').get('access_token')

def get_data(): 
    access_token = get_tokent()
    url2 = "http://222.73.31.135:8084/api?access_token=%(access_token)s&handler=event&method=export" % {'access_token': access_token,}
    
    data = {
        'project_id': '201804040003',
        'send_time': '2018-05-11',
        'to_time': '2018-05-12',
    }
    rt = requests.get(url2, params = data)
    dc = json.loads(rt.content.decode('utf-8'))
    print(rt.content)

def test_send_data(): 
    with open(r"C:\Users\heyul\Desktop\jj20180512141450.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        p1 = 'data:image/jpeg;base64,%(data)s' % {'data': encoded_string,}
    with open(r"C:\Users\heyul\Desktop\jj20180512140349.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        p2 = 'data:image/jpeg;base64,%(data)s' % {'data': encoded_string,}    
        
    data = [{
        'taskid': '201805101289',
        'remark': '测试用',
        'pictures': [p1],
        }, 
        {'taskid': '201805101290',
         'remark': '测试用',
         'pictures': [p2],}
        ]
    access_token = get_tokent()
    url = 'http://222.73.31.135:8084/api?handler=event&method=import&access_token=%(access_token)s' % {'access_token': access_token,}
    rt = requests.post(url, data = {'data': json.dumps( data)})
    print(rt.content)

test_send_data()