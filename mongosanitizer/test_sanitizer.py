from mongosanitizer.sanitizer import sanitize


def test_sanitize_first_level_key():
    query = {'$bob': 'alice'}
    sanitize(query)
    assert '$bob' not in query


def test_sanitize_second_level_dict():
    query = {'jim': {'$bob': 'jones'}}
    sanitize(query)
    assert '$bob' not in query['jim']


def test_sanitize_in_a_second_level_list():
    query = {'jim': [{'$bob': 'jones'}]}
    sanitize(query)
    assert '$bob' not in query['jim'][0]


def test_sanitize_a_third_level_dict_in_a_second_level_list():
    query = {'jim': [{'johnson': {'$bob': 'jones'}}]}
    sanitize(query)
    assert '$bob' not in query['jim'][0]['johnson']
