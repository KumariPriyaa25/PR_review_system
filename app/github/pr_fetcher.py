from app.github.github_client import GitHubClient

class PRFetcher:
    def __init__(self):
        self.github_client = GitHubClient()
        
    def fetch(self, owner: str, repo: str, pr_number: int):
        
        pr = self.github_client.get_pull_request(owner , repo , pr_number)
        files = []
        
        for file in pr.get_files():
            files.append({
                "filename": file.filename,
                "status": file.status,
                "additions": file.additions,
                "deletions": file.deletions,
                "changes": file.changes,
                "patch": file.patch
            })
        return {
            "pr_number": pr.number,
            "title": pr.title,
            "author": pr.user.login,
            "state": pr.state,
            "base_branch": pr.base.ref,
            "head_branch": pr.head.ref,
            "files": files
        }
        