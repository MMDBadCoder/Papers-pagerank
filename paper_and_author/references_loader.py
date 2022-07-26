import json

import requests

paper_ids_file = open('./papers.txt', 'r')
paper_ids = json.loads('\n'.join(paper_ids_file.readlines()))
paper_ids_file.close()

last_file = open('./references_of_papers.txt', 'r')
data = json.loads('\n'.join(last_file.readlines()))
last_file.close()

print(len(data))

with open('./references_of_papers.txt', 'w') as file:
    try:
        for paper_id in paper_ids:
            if not data.__contains__(paper_id):
                url = 'https://api.semanticscholar.org/graph/v1/paper/' + paper_id + '/references?fields=paperId'
                response = requests.get(url=url)
                all_referenced_paper_ids = []
                for reference in json.loads(response.content)['data']:
                    referenced_paper_id = reference['citedPaper']['paperId']
                    all_referenced_paper_ids.append(referenced_paper_id)
                data[paper_id] = all_referenced_paper_ids
    except Exception as e:
        pass
    finally:
        print('All data has been saved')
        file.write(json.dumps(data))
