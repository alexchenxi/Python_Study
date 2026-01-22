import requests
from operator import itemgetter
import plotly.express as px


def practice_17_1(language):
    url = "https://api.github.com/search/repositories"
    url += f"?q=language:{language}+sort:stars+stars:>10000"

    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")

    response_dict = r.json()
    print(f"Total repositories: {response_dict['total_count']}")
    print(f"Complete results: {response_dict['incomplete_results']}")

    repo_dicts = response_dict["items"]
    print(f"Repositories returned: {len(repo_dicts)}")

    print("\nSelected information about first repository:")
    for repo_dict in repo_dicts:
        print(f"\nName: {repo_dict['name']}")
        print(f"Owner: {repo_dict['owner']['login']}")
        print(f"Stars: {repo_dict['stargazers_count']}")
        print(f"Repository: {repo_dict['html_url']}")
        print(f"Description: {repo_dict['description']}")


def practice_17_2():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    r = requests.get(url)
    print(f"Status code: {r.status_code}")

    # 处理有关每篇文章的信息
    submission_ids = r.json()
    submission_dicts = []
    for submission_id in submission_ids[:30]:
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url)
        print(f"id: {submission_id}\tstatus: {r.status_code}")
        response_dict = r.json()

        submission_dict = {
            "title": response_dict["title"],
            "hn_link": f"http://news.ycombinator.com/item?id={submission_id}",
            "comments": response_dict.get("descendants", 0),
        }

        submission_dicts.append(submission_dict)

        submission_dicts = sorted(
            submission_dicts, key=itemgetter("comments"), reverse=True
        )

    article_links, comments_nums, hover_texts = [], [], []
    for submission_dict in submission_dicts:
        article_links.append(submission_dict["hn_link"])
        comments_nums.append(submission_dict["comments"])
        hover_texts.append(f"{submission_dict['title']}")

    title = "Most-Commented Hacker News Articles"
    labels = {"x": "Article", "y": "Comments"}
    fig = px.bar(
        x=article_links,
        y=comments_nums,
        title=title,
        labels=labels,
        hover_name=hover_texts,
    )
    fig.update_layout(
        title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20
    )
    fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)
    fig.show()


practice_17_2()
