from typing import Generator
import pytest
from playwright.sync_api import Playwright, APIRequestContext, expect, Page
from configparser import ConfigParser
from pathlib import Path
current_folder = Path(__file__).parent.resolve()

# Loading user info
config = ConfigParser()
config.read(f"{current_folder}/gittoken.ini")
# user = input("What is your name?: ")
user = "GITHUB"
try:
    config_data = config[user]
except:
    print("User not found!")
    exit(0)

GITHUB_API_TOKEN = config_data['token']
assert GITHUB_API_TOKEN, "GITHUB_API_TOKEN is not set"

GITHUB_USER = config_data['username']
assert GITHUB_USER, "GITHUB_USER is not set"

GITHUB_REPO = "test"


# ... # GitHub API requires authorization
@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    '''GitHub API requires authorization'''
    headers = {
        # We set this header per GitHub guidelines.
        "Accept": "application/vnd.github.v3+json",
        # Add authorization token to all requests.
        # Assuming personal access token available in the environment.
        "Authorization": f"token {GITHUB_API_TOKEN}",
    }
    request_context = playwright.request.new_context(
        base_url="https://api.github.com", extra_http_headers=headers
    )
    yield request_context
    request_context.dispose()


# ... # create a new repository before running tests and delete it afterwards
@pytest.fixture(scope="session", autouse=True)
def create_test_repository(
    api_request_context: APIRequestContext,
) -> Generator[None, None, None]:
    
    # Before all
    new_repo = api_request_context.post("/user/repos", data={"name": GITHUB_REPO})
    assert new_repo.ok
    yield

    # After all
    deleted_repo = api_request_context.delete(f"/repos/{GITHUB_USER}/{GITHUB_REPO}")
    assert deleted_repo.ok


# # ... # These tests assume that repository exists
# def test_should_create_bug_report(api_request_context: APIRequestContext) -> None:
#     data = {
#         "title": "[Bug] report 1",
#         "body": "Bug description",
#     }
#     new_issue = api_request_context.post(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data)
#     assert new_issue.ok

#     issues = api_request_context.get(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues")
#     assert issues.ok

#     issues_response = issues.json()
#     issue = list(filter(lambda issue: issue["title"] == "[Bug] report 1", issues_response))[0]
#     assert issue
#     assert issue["body"] == "Bug description"


# def test_should_create_feature_request(api_request_context: APIRequestContext) -> None:
#     data = {
#         "title": "[Feature] request 1",
#         "body": "Feature description",
#     }
#     new_issue = api_request_context.post(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data)
#     assert new_issue.ok

#     issues = api_request_context.get(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues")
#     assert issues.ok

#     issues_response = issues.json()
#     issue = list(filter(lambda issue: issue["title"] == "[Feature] request 1", issues_response))[0]
#     assert issue
#     assert issue["body"] == "Feature description"


# def test_last_created_issue_should_be_first_in_the_list(api_request_context: APIRequestContext, page: Page) -> None:
#     def create_issue(title: str) -> None:
#         data = {
#             "title": title,
#             "body": "Feature description",
#         }
#         new_issue = api_request_context.post(
#             f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data
#         )
#         assert new_issue.ok
#     create_issue("[Feature] request 1")
#     create_issue("[Feature] request 2")
#     page.goto(f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/issues")
#     first_issue = page.locator("a[data-hovercard-type='issue']").first
#     expect(first_issue).to_have_text("[Feature] request 2")


# def test_last_created_issue_should_be_on_the_server(api_request_context: APIRequestContext, page: Page) -> None:
#     page.goto(f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/issues")
#     page.locator("text=New issue").click()
#     page.locator("[aria-label='Title']").fill("Bug report 1")
#     page.locator("[aria-label='Comment body']").fill("Bug description")
#     page.locator("text=Submit new issue").click()
#     issue_id = page.url.split("/")[-1]

#     new_issue = api_request_context.get(f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/issues/{issue_id}")
#     assert new_issue.ok
#     assert new_issue.json()["title"] == "[Bug] report 1"
#     assert new_issue.json()["body"] == "Bug description"