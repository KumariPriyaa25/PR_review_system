from fastapi import APIRouter, Request
from app.services.review_service import process_pull_request


router = APIRouter()

print("=" * 50)
print("WEBHOOK RECEIVED")
print("=" * 50)


@router.post("/webhook/github")
async def github_webhook(request: Request):
    print("Received webhook request")
    payload = await request.json()

    event = request.headers.get("X-GitHub-Event")
    print(f" Event type: {event}")

    if event != "pull_request":
        print(" Ignoring event: not a pull_request")
        return {"message": "Ignored: not a pull_request event"}

    action = payload.get("action")
    print(f"PR action: {action}")
    if action not in ["opened", "synchronize", "reopened"]:
        print(f"Ignoring PR action: {action}")
        return {"message": f"Ignored PR action: {action}"}

    repo_data = payload.get("repository", {})
    owner = repo_data.get("owner", {}).get("login")
    repo = repo_data.get("name")

    pr_data = payload.get("pull_request", {})
    pr_number = pr_data.get("number")

    if not all([owner, repo, pr_number]):
        print("Missing PR data in webhook payload")
        return {"message": "Missing PR data"}

    print(f"Processing PR #{pr_number} from {owner}/{repo}")
    files = process_pull_request(owner, repo, pr_number)
    print(f"Finished processing PR #{pr_number}")

    return {
        "message": "PR event processed successfully",
        "owner": owner,
        "repo": repo,
        "pr_number": pr_number,
        "files": files
    }