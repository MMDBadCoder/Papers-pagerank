import requests

each_step = 50
total_count = 1000
if __name__ == '__main__':
    for i in range(int(total_count / each_step)):
        url = 'https://api.semanticscholar.org/graph/v1/paper/search?query=Leukemia&offset=' + str(i * each_step) + \
              '&limit=' + str(each_step) + '&fields=title,authors'
        response = requests.get(url=url)
        with open('./search_results/offset' + str(i) + '.txt', 'w') as file:
            file.write(response.text)
