import requests

company = "http://www.kuaidi100.com/autonumber/autoComNum?text={0}"
post = "http://www.kuaidi100.com/query?type={0}&postid={1}"


def get_company_no(post_id):
    uri = company.format(post_id)
    resp = requests.get(uri)
    j = resp.json()
    if j is not None and j.get('auto') is not None and len(j['auto']) > 0:
        # if code exists return the first company code
        return j['auto'][0]['comCode']


def get_post_info(post_id):
    uri = post.format(get_company_no(post_id), post_id)
    resp = requests.get(uri)
    j = resp.json()
    return j

if __name__ == '__main__':
    data = get_post_info('881443775034378914')['data']
    for d in data:
        print(d['ftime']+' -> '+d['context'])
