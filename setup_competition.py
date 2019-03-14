#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os

import requests


def get_ins_outs(response):
    texts = response.text.split("\r\n")
    starts = [i for i, _l in enumerate(texts) if "<pre>" in _l]
    ends = [i for i, _l in enumerate(texts) if "</pre>" in _l]

    tmp = []
    for _s, _e in zip(starts, ends):
        if "Sample" not in texts[_s]:
            continue
        tmp.append("\n".join(texts[_s:_e]).split("<pre>")[-1])
    return tmp


def make_test_code(_file, problem, _in, _out):
    with open(_file, "w") as f:
        f.write("import pytest\n")
        f.write("from {} import solve\n\n\n".format(problem.upper()))
        f.write("def test_solve():\n")
        for _i, _o in zip(_in, _out):
            f.write("    assert solve('{}') == '{}'\n".format(
                _i.replace("\n", "\\n"), _o.replace("\n", "\\n")))


def make_answer_basecode(_file):
    with open(_file, "w") as f:
        f.write("def solve(string):\n")
        f.write("    pass\n\n\n")
        f.write("if __name__ == '__main__':\n")
        f.write("    print(solve(input()))\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int)
    parser.add_argument("--division", choices=["abc", "arc"], default="abc")
    args = parser.parse_args()

    prob_char = ["a", "b", "c", "d"]
    base = "https://{div}{num:03}.contest.atcoder.jp/".format(div=args.division, num=args.number)
    r = requests.get(base + "assignments/")
    tmp = [_l for _l in r.text.split("\n") if "linkwrapper" in _l.strip()][::2]
    urls = [_t.split("href=\"")[1].split("\">")[0] for _t in tmp]

    for _c, _u in zip(prob_char, urls):
        save_dir = "{}{}".format(args.division.upper(), args.number)
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)

        r = requests.get(base + _u)
        ins_outs = get_ins_outs(r)
        ins = ins_outs[::2]
        outs = ins_outs[1::2]
        print(ins)
        print(outs)

        testcode = "{}/Test_{}.py".format(save_dir, _c.upper())
        make_test_code(testcode, _c, ins, outs)
        answercode = "{}/{}.py".format(save_dir, _c.upper())
        if os.path.exists(answercode):
            continue
        make_answer_basecode(answercode)
