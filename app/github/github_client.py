from github import Github
from app.config import settings


class GitHubClient:

    def __init__(self):
        self.client = Github(settings.GITHUB_TOKEN)

    def get_authenticated_user(self):
        return self.client.get_user()

    def get_repo(self):
        return self.client.get_repo(
            f"{settings.GITHUB_REPO_OWNER}/{settings.GITHUB_TEST_REPO}"
        )
    def get_pull_request(self, owner, repo, pr_number):
        repository = self.client.get_repo(f"{owner}/{repo}")
        return repository.get_pull(pr_number)