import random

from chance import chance

LICENSE_SPEC = {
    'Apache-2.0': {'stub': 'Apache License', 'with_holder': False, 'filename': 'LICENSE'},
    'BSD-3-Clause': {'stub': 'BSD 3-Clause License', 'with_holder': True, 'filename': 'LICENSE'},
    'GPL-3.0-or-later': {'stub': 'GNU General Public License', 'with_holder': False, 'filename': 'COPYING'},
    'LGPL-3.0-or-later': {'stub': 'GNU Lesser General Public License', 'with_holder': False, 'filename': 'COPYING'},
    'MIT': {'stub': 'MIT License', 'with_holder': True, 'filename': 'LICENSE'},
    'MPL-2.0': {'stub': 'Mozilla Public License', 'with_holder': False, 'filename': 'LICENSE'},
    'Unlicense': {'stub': 'This is free and unencumbered software released into the public domain', 'with_holder': False, 'filename': 'UNLICENSE'}
}


def generate_copier_answers():
    return {
        'project_name': f'{chance.word()}-{chance.word()}',
        'project_package': f'{chance.word()}_{chance.word()}',
        'project_description': chance.sentence(),
        'project_version': f'{random.randint(0, 10)}.{random.randint(0, 10)}.{random.randint(0, 10)}',
        'project_keywords': f'{chance.word()},{chance.word()},{chance.word()}',
        'copyright_holder_name': chance.name(),
        'copyright_holder_email': chance.email(),
        'copyright_license': chance.pickone(list(LICENSE_SPEC.keys())),
        'copyright_year': str(random.randint(2000, 2024)),
        'vcs_github_path': f'{chance.word()}/{chance.word()}-{chance.word()}'.lower(),
        'python_version': chance.pickone(['>=3.10', '>=3.11', '>=3.12']),
        'with_tox': chance.pickone([True, False]),
    }
