import requests

def func_request(url):
    cookie = "fspop=test; _lxsdk_cuid=186827ab718c8-0343515a7fea35-26021051-144000-186827ab718c8; _lxsdk=186827ab718c8-0343515a7fea35-26021051-144000-186827ab718c8; _hc.v=7b3b5ba5-32b8-1ded-31f0-88ddae0a50b5.1710470579; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1710470580; cy=6; cye=suzhou; s_ViewType=10; WEBDFPID=y9763yv681wx5wz61x336yvx363zuu8881v59992691979581u3437yu-2025830758353-1710470758353MSOKYASfd79fef3d01d5e9aadc18ccd4d0c95072683; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; dper=0202ae2624bcdbd09c4702f8dd95a3ced4b3370ca79a23a359e4d32e67e9b7fc7d043d1cd585fbded37ba8773b0ec6fe72e7422c58f227d4c46500000000a81e0000c688e7ea19f35aadcfd333ac0ecb7c699b86309011b3ad5c65abc008fa4a7ac719ddf49da41ae01c68308813cacdddfb; qruuid=aceeb77c-29f0-4040-b0de-aa9b34a0bdf0; ll=7fd06e815b796be3df069dec7836c3df; _lxsdk_s=18e3ffdc24d-c5c-e3e-969%7C%7C246; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1710472540"
    headers = {
        "cookie": cookie,
        "Host": "www.dianping.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    }

    resp = requests.get(url, headers=headers)
    if resp.status_code in [200, 302]:
        return resp.text
    else:
        print(resp.status_code)
        return resp.text

def func_response(resp: str):
    print(resp)


def main():
    url = "https://www.dianping.com/shop/jTYIYHRl2kiDdYGe/review_all/p4"
    resp = func_request(url)
    func_response(resp)


if __name__ == '__main__':
    main()


