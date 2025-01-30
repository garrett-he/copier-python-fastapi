from .utils import generate_copier_answers


def test_package(copie):
    answers = generate_copier_answers()
    result = copie.copy(extra_answers=answers)

    if result.exception:
        raise result.exception

    about_file = result.project_dir / 'src' / answers['project_package'] / '__about__.py'
    assert answers['project_package'] in about_file.read_text(encoding='utf-8')
