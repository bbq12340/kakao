import requests
import pandas as pd
import time


def functionA(query, p):
    url = 'https://m.map.kakao.com/actions/searchJson'
    payload = {
        "type": "PLACE",
        "q": query,
        "wxEnc": "LVSOTP",
        "wyEnc": "QNLTTMN",
        "pageNo": p,
        "sort": "0"
    }
    my_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
        "Host": "m.map.kakao.com",
        "Referer": f"https://m.map.kakao.com/actions/searchView?q={query}&wxEnc=LVSOTP&wyEnc=QNLTTMN"
    }
    r = requests.get(url, params=payload, headers=my_headers)
    if r.status_code == 200:
        place_list = r.json()["placeList"]
    else:
        place_list = []

    return place_list


def request_kakao(query, p):
    url = 'https://search.map.daum.net/mapsearch/map.daum'
    payload = {
        "q": query,
        "msFlag": "S",
        "page": p,
        "sort": "0"
    }
    my_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
        "Host": "search.map.daum.net",
        "Referer": "https://map.kakao.com/"
    }
    r = requests.get(url, params=payload, headers=my_headers)
    return r


def extract_kakao(query, p):
    result = []
    r = request_kakao(query, p)
    if r.status_code == 200:
        place_list = r.json().get("place")
        for place in place_list:
            cat = (",").join(
                [place[f"cate_name_depth{i}"] for i in range(1, 6)]).rstrip(",")
            data = {
                "업체명": place["name"],  # 업체명
                "별점": place["rating_average"],  # 별점
                "방문뷰": place["rating_count"],  # 방문뷰
                "블로그리뷰": place["reviewCount"],  # 블로그리뷰
                "업종": cat,  # 업종,
                "전화번호": place["tel"],  # 전화번호
                "지번": place["address"],  # 지번
                "도로명": place["new_address"]  # 도로명
            }
            result.append(data)
    return result


def start_scraping(query, target=0, delay=0):
    l = 0
    p = 1
    encoded_query = query.encode("utf-8")
    if target == 0:
        r = request_kakao(encoded_query, 1)
        target = int(r.json().get("place_totalcount"))
        print(target)
    while l < target:
        data = extract_kakao(encoded_query, p)
        print(p)
        if len(data) == 0:
            print("무슨 일이지 시발?")
            break
        p = p + 1
        df = pd.DataFrame(data, columns=["name", "rating", "rating_count",
                                         "review_count", "reviewCount", "category", "tel", "address", "new_address"])
        df.to_csv(f"{query}.csv", mode="a", encoding="utf-8-sig",
                  header=False, index=False)
        l = l + len(data)
        time.sleep(delay)
        if l >= target:
            print("끝!")
            break


if __name__ == '__main__':
    # start_scraping("마포구 맛집", target=0, delay=1)
    r = request_kakao("강남구 맛집".encode("utf-8"), 34)
    print(r.text)
