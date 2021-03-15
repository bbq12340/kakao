from PySide2.QtCore import QThread, QObject, Signal
import time
import pandas as pd
from scraper import request_kakao, extract_kakao


class Worker(QObject):
    finished = Signal()
    progress = Signal(float)

    def __init__(self, query_list, delay):
        super().__init__()
        self.query_list = query_list
        self.delay = float(delay)

    def run(self):
        for query in self.query_list:
            self.progress.emit(
                ((self.query_list.index(query)+1)/len(self.query_list))*100)
            l = 0
            p = 1
            encoded_query = query.encode("utf-8")
            # if target == 0:
            #     r = request_kakao(encoded_query, 1)
            #     target = int(r.json().get("place_totalcount"))
            #     print(target)
            while l < 500:
                data = extract_kakao(encoded_query, p)
                if len(data) == 0:
                    break
                p = p + 1
                df = pd.DataFrame(data, columns=["업체명", "별점", "방문뷰",
                                                 "블로그리뷰", "업종", "전화번호", "지번", "도로명"])
                df.to_csv(f"result/{query}.csv", mode="a", encoding="utf-8-sig",
                          header=False, index=False)
                l = l + len(data)
                time.sleep(self.delay)
                if l >= 500:
                    break
        self.finished.emit()
