import json


def get_graph_of_authors(top_papers_count):
    import json

    author_ids_by_paper_id = {}
    paper_ids = set()
    for i in range(20):
        with open('./top_papers/search_results/offset' + str(i) + '.txt', 'r') as file:
            data = json.loads('\n'.join(file.readlines()))
            for record in data['data']:
                paper_id = record['paperId']
                paper_ids.add(paper_id)
                author_ids = set()
                for author in record['authors']:
                    author_id = author['authorId']
                    author_ids.add(author_id)
                    author_ids_by_paper_id[paper_id] = list(author_ids)
                if len(paper_ids) >= top_papers_count:
                    break
            if len(paper_ids) >= top_papers_count:
                break

    with open('./paper_and_author/references_of_papers.txt', 'r') as file:
        references_by_paper_id = json.loads('\n'.join(file.readlines()))

    links = []

    for paper_id, references in references_by_paper_id.items():
        if paper_id in paper_ids:
            for referenced_paper_id in references:
                if referenced_paper_id in paper_ids:
                    for source_author in author_ids_by_paper_id[paper_id]:
                        for target_author in author_ids_by_paper_id[referenced_paper_id]:
                            links.append([source_author, target_author, 1])

    return links
