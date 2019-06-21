import argparse
import os

import requests
from bs4 import BeautifulSoup as bs
from bs4.element import Comment

import config


def login(session):
    LOGIN_URL = "https://atcoder.jp/login"
    r = session.get(LOGIN_URL)
    csrf_token = bs(r.text, 'lxml').find(attrs={'name': 'csrf_token'}).get('value')
    login_info = {"csrf_token": csrf_token, "username": config.name, "password": config.pwd}
    session.post(LOGIN_URL, data=login_info)


def get_urls(result):
    urls = [
        b.a for b in bs(result.text, "html.parser").find_all("td", class_="text-center no-break")
    ]
    return [(b.text, base + b.attrs["href"].split("/")[-1]) for b in urls]


def get_ins_outs(result):
    return [
        b.text.strip()
        for b in bs(result.text, "html.parser").find_all("pre")
        if len(b.contents) == 1 and tag_visible(b)
    ]


def make_test_code(savedir, problem, inout):
    with open("{}/Test_{}.py".format(savedir, problem), "w") as f:
        f.write("import pytest\n")
        f.write("from {} import solve\n\n\n".format(problem.upper()))
        f.write("def test_solve():\n")
        for _i, _o in zip(*[iter(inout)] * 2):
            f.write("    assert solve('{}') == '{}'\n".format("\\n".join(_i.splitlines()),
                                                              "\\n".join(_o.splitlines())))


def make_answer_basecode(_file):
    with open(_file, "w") as f:
        f.write("def solve(string):\n")
        f.write("    pass\n\n\n")
        f.write("if __name__ == '__main__':\n")
        f.write("    print(solve(input()))\n")


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int)
    parser.add_argument("--division", choices=["abc", "arc"], default="abc")
    args = parser.parse_args()

    save_dir = "{}{:03}".format(args.division.upper(), args.number)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    base = "https://atcoder.jp/contests/{}{:03}/tasks/".format(args.division, args.number)
    with requests.session() as s:
        login(s)
        urls = get_urls(s.get(base))
        for name, url in urls:
            make_answer_basecode("{}/{}.py".format(save_dir, name))
            make_test_code(save_dir, name, get_ins_outs(s.get(url)))
