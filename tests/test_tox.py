from .utils import generate_copier_answers


def test_template_tox(copie):
    answers = generate_copier_answers()
    answers['with_tox'] = True
    result = copie.copy(extra_answers=answers)

    if result.exception:
        raise result.exception

    assert result.project_dir.joinpath('tox.ini').is_file()

    answers['with_tox'] = False
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert not result.project_dir.joinpath('tox.ini').is_file()
