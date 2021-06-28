import os
from datetime import datetime
import codecs

import requests


def document_connection_data(url, reachable, descr="ok"):
    """
    url: url of page
    reachable: is url reachable
    exc: exception of empty sting
    """
    try:
        with codecs.open(
            os.path.join(
                os.path.abspath(os.path.dirname(__file__)),
                "../data/connection_data.csv",
            ),
            "a",
            encoding="utf-8",
        ) as doc_file:
            doc_file.write(f"{datetime.now()};{url};{reachable};{descr}\n")
    except Exception as ex:
        print(f"[Exception] {__file__}::{document_connection_data.__name__} - {ex}")


def reach_url(url):
    """
    try reaching url with get request and document outcome
    """
    try:
        requests.get(url)
        # document_connection_data(url, True)
        return True
    except Exception as ex:
        document_connection_data(url, False, ex)
        return False


def establish_internet_connection():
    """
    This function checks the current internet connection
    and logs into internet if amplus is logged out
    """
    try:
        # urls
        url_google_dns_server_1 = "https://8.8.8.8"
        url_google_dns_server_2 = "https://8.8.4.4"
        url_amplus_login = (
            "http://hs1-5-amplus.spot/login?dst=&username=T-E0%3A28%3A6D%3A06%3A07%3AB0"
        )

        # check if google dns server is reachable
        # if yes internet connection is established
        if reach_url(url_google_dns_server_1):
            return

        if reach_url(url_google_dns_server_2):
            return

        # perform amplus internet login
        reach_url(url_amplus_login)

    except Exception as ex:
        # something went horribly wrong
        document_connection_data("")
        print(
            f"[Exception] {__file__}::{establish_internet_connection.__name__} - {ex}"
        )


if __name__ == "__main__":

    establish_internet_connection()
