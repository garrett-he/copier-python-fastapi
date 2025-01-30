import toml

from .utils import generate_copier_answers


def test_template_pyproject_toml(copie):
    answers = generate_copier_answers()
    result = copie.copy(extra_answers=answers)

    if result.exception:
        raise result.exception

    with open(result.project_dir.joinpath('pyproject.toml'), 'r', encoding='utf-8') as fp:
        pyproject = toml.loads(fp.read())

    assert pyproject['project']['name'] == answers['project_name']
    assert pyproject['project']['version'] == answers['project_version']
    assert pyproject['project']['description'] == answers['project_description']
    assert pyproject['project']['requires-python'] == answers['python_version']
    assert pyproject['project']['authors'][0]['name'] == answers['copyright_holder_name']
    assert pyproject['project']['authors'][0]['email'] == answers['copyright_holder_email']
    assert pyproject['project']['license']['text'] == answers['copyright_license']
    assert pyproject['project']['keywords'] == answers['project_keywords'].split(',')

    assert pyproject['project']['urls']['homepage'] == f"https://github.com/{answers['vcs_github_path']}"
    assert pyproject['project']['urls']['repository'] == f"https://github.com/{answers['vcs_github_path']}.git"
    assert pyproject['project']['urls']['changelog'] == f"https://github.com/{answers['vcs_github_path']}/blob/main/CHANGELOG.md"
