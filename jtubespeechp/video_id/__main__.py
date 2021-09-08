import argparse
import re
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
import requests
from tqdm import tqdm
from util import make_query_url
from gnutools.fs import parent, name
import os

def main(word, wait_sec, fn_videoid):
    try:
        # download search results
        url = make_query_url(word)
        html = requests.get(url).content

        # find video IDs
        videoids_found = [x.split(":")[1].strip("\"").strip(" ") for x in
                          re.findall(r"\"videoId\":\"[\w\_\-]+?\"", str(html))]
        videoids_found = list(set(videoids_found))
        with open(fn_videoid, "a") as f:
            # write
            f.writelines([v + "\n" for v in videoids_found])
            f.flush()
    except:
        print(f"No video found for {word}.")

    # wait
    if wait_sec > 0.01:
        time.sleep(wait_sec)


def obtain_video_id(lang, fn_word, outdir="videoid", wait_sec=0.2):
    fn_videoid = f"{outdir}/{lang}/{name(fn_word)}.txt"
    os.makedirs(parent(fn_videoid), exist_ok=True)

    with open(fn_videoid, "w") as f:
        f.write("")
        f.flush()

    with ProcessPoolExecutor() as e:
        fs = [e.submit(main, word, wait_sec, fn_videoid)
              for word in tqdm(list(open(fn_word, "r").readlines()))]
        for f in tqdm(as_completed(fs), total=len(fs), desc="Downloading"):
            assert f._exception is None
    return fn_videoid


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Obtaining video IDs from search words",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("lang", type=str, help="language code (ja, en, ...)")
    parser.add_argument("wordlist", type=str, help="filename of word list")
    parser.add_argument("--outdir", type=str, default="videoid", help="dirname to save video IDs")
    args = parser.parse_args()

    filename = obtain_video_id(args.lang, args.wordlist, args.outdir, wait_sec=0.2)
    print(f"save {args.lang.upper()} video IDs to {filename}.")
