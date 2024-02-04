import pytest

@pytest.mark.api
def test_check_available_emojis(github_api):
    r = github_api.get_emojis()

    assert r["8ball"] == "https://github.githubassets.com/images/icons/emoji/unicode/1f3b1.png?v8"
    assert len(r) == 1877

@pytest.mark.api
def test_check_commits_in_existing_repo(github_api):
    r = github_api.get_commits("KaterynaSoloviova", "prometheus-qa-auto")

    assert r[0]["commit"]["author"]["name"] == "Kateryna Soloviova"
    assert len(r) >= 4
    
@pytest.mark.api
def test_check_commits_in_non_existing_repo(github_api):
    r = github_api.get_commits("KaterynaSoloviova", "non_existing_repo")

    assert r["message"] == "Not Found"
   
@pytest.mark.api
def test_check_commits_at_non_existing_user_and_repo(github_api):
    r = github_api.get_commits("non_existing_name", "non_existing_repo")

    assert r["message"] == "Not Found"
    
@pytest.mark.api
def test_check_commits_in_private_repo(github_api):
    r = github_api.get_commits("KaterynaSoloviova", "prometheus-python")

    assert r["message"] == "Not Found"

@pytest.mark.api
def test_check_code_frequency_in_new_repo(github_api):
    r = github_api.get_code_frequency("KaterynaSoloviova", "prometheus-qa-auto")

    assert len(r) >= 0
    
@pytest.mark.api
def test_check_code_frequency_in_repo_with_more_than_10000_commits(github_api):
    r = github_api.get_code_frequency("zed-industries", "zed")

    assert r["message"] == "repository must have fewer than 10000 commits"

@pytest.mark.api
def test_check_(github_api):
    r = github_api.get_branches("KaterynaSoloviova", "prometheus-qa-auto")

    assert r[0]["name"] == "main"
    assert len(r) == 1