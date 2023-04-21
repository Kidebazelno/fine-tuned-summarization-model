import json
import argparse
from tw_rouge import get_rouge


def main(args):
    refs, preds = {}, {}

    with open(args.reference) as file:
        for line in file:
            line = json.loads(line)
            refs[line['id']] = line['title'].strip() + '\n'

    with open(args.submission) as file:
        for line in file:
            line = json.loads(line)
            preds[line['id']] = line['title'].strip() + '\n'

    keys =  refs.keys()
    refs = [refs[key] for key in keys]
    preds = [preds[key] for key in keys]

    name = args.submission.split('.')[-2].split('/')[-1]
    with open("greedyrouge.json","a") as f:
        print("writing at",name)
        f.write(name)
        f.write(':\n')
        f.write(json.dumps(get_rouge(preds, refs), indent=2))
        f.write('\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--reference')
    parser.add_argument('-s', '--submission')
    args = parser.parse_args()
    main(args)
