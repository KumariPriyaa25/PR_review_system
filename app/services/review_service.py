from app.github.diff_parser import DiffParser
from app.github.pr_fetcher import PRFetcher


def process_pull_request(owner , repo , pr_number):
    print(f"Starting review workflow for PR #{pr_number}")
    fetcher = PRFetcher()
    # result = fetcher.fetch(owner, repo, pr_number)
    # print(f"Fetched changed files for PR #{pr_number}")
    # return result
    review = fetcher.fetch(owner, repo, pr_number)

    parser = DiffParser()

    parsed = parser.parse(review["files"])

    review["parsed_files"] = parsed

    return review