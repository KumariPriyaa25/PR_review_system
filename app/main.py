from fastapi import FastAPI
from app.github.github_client import GitHubClient
from app.api.webhook_routes import router as webhook_router

app = FastAPI(title="PR Review System")

# Register webhook routes
app.include_router(webhook_router)


@app.get("/")
def home():
    return {"message": "PRISM local server is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/github-test")
def github_test():

    github = GitHubClient()

    user = github.get_authenticated_user()

    repo = github.get_repo()

    return {
        "authenticated_user": user.login,
        "repository": repo.full_name,
        "private": repo.private,
        "default_branch": repo.default_branch,
    }