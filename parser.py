from Bio import Medline
from datetime import datetime
from argparse import ArgumentParser
def main(medline):
    with open(medline) as handle:
        records = Medline.parse(handle)
        for record in records:
            # Take the epub date as the publication date
            pubDate = datetime.strptime(record['EDAT'], "%Y/%m/%d %H:%M")
            authors = ', '.join(record['AU'])
            # there are multiple AIDs so we need to find the right one and then strip off the embeded ID
            doi = ''.join([x for x in record['AID'] if x[-5:] == '[doi]'])[:-6]
            # This forms the body in the detailed page
            content = ''
            content += '**{}**\n\n'.format(authors)
            content += '{}\n\n'.format(record['SO'])
            if 'AB' in record:
                content += record['AB']

            # we need a unique filename and the PMID is good enough for this
            with open('{}.md'.format(record['PMID']), 'w') as f:
                f.write('---\n')
                f.write('title: "{}"\n'.format(record['TI']))
                f.write('date: {}\n'.format(pubDate))
                f.write('pubtype: "Article"\n')
                f.write('description: "{}. {}"\n'.format(authors, record['SO']))
                f.write('tags: [""]\n')
                f.write('image: ""\n')
                f.write('link: "https://doi.org/{}"\n'.format(doi))
                f.write('---\n')
                f.write('{}\n'.format(content))

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('medline', help="medline results file to parse into publications")
    args = parser.parse_args()
    main(args.medline)
