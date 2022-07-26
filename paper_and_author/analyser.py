import json

author_id_by_paper_id = []
papers = set()
authors = set()
for i in range(20):
    with open('../top_papers/search_results/offset' + str(i) + '.txt', 'r') as file:
        data = json.loads('\n'.join(file.readlines()))
        for record in data['data']:
            paper_id = record['paperId']
            papers.add(paper_id)
            for author in record['authors']:
                author_id = author['authorId']
                authors.add(author_id)
                author_id_by_paper_id.append([paper_id, author_id])

with open('./authors.txt', 'w') as file:
    file.write(json.dumps(list(authors)))

with open('./papers.txt', 'w') as file:
    file.write(json.dumps(list(papers)))

print(len(author_id_by_paper_id))
print(len(papers))
print(len(authors))
