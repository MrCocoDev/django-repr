import pytest

from tests.example_project.myapp.models import (
    FourOrLessFields,
    FourOrMoreFields,
    JustForFKs,
    WithoutDecorator,
)


def test_with_four_or_less_fields():
    instance = FourOrLessFields()
    actual = repr(instance)
    expected = "FourOrLessFields()"

    assert actual == expected


@pytest.mark.parametrize(
    'data, expected',
    [
        ({}, 'FourOrLessFields(id=1, four_id=1)'),
        ({'one': 'Some Value'}, "FourOrLessFields(id=1, one='Some Value', four_id=1)"),
        ({'one': '', 'two': None, 'three': None}, 'FourOrLessFields(id=1, two=None, four_id=1)'),
        ({'one': '', 'two': '', 'three': '77'}, "FourOrLessFields(id=1, two='', three='77', four_id=1)"),
        ({'one': '', 'two': 'Something', 'three': '77'}, "FourOrLessFields(id=1, two='Something', three='77', four_id=1)"),
    ]
)
@pytest.mark.django_db
def test_with_four_or_less_fields_saved(data, expected):
    instance = FourOrLessFields.objects.create(
        **data,
        four=JustForFKs.objects.create()
    )
    actual = repr(instance)
    assert actual == expected


@pytest.mark.parametrize(
    'data, expected',
    [
        ({}, 'FourOrLessFields(id=1, four_id=1)'),
        ({'one': 'Some Value'}, "FourOrLessFields(id=1, one='Some Value', four_id=1)"),
        ({'one': '', 'two': None, 'three': None}, 'FourOrLessFields(id=1, two=None, four_id=1)'),
        ({'one': '', 'two': '', 'three': '77'}, "FourOrLessFields(id=1, two='', three=77, four_id=1)"),
        ({'one': '', 'two': 'Something', 'three': '77'}, "FourOrLessFields(id=1, two='Something', three=77, four_id=1)"),
    ]
)
@pytest.mark.django_db
def test_with_four_or_less_fields_saved_and_refreshed(data, expected):
    instance = FourOrLessFields.objects.create(
        **data,
        four=JustForFKs.objects.create()
    )
    instance.refresh_from_db()
    actual = repr(instance)
    assert actual == expected


@pytest.mark.django_db
def test_with_four_or_more_fields():
    instance = FourOrMoreFields(
        one='one',
        two='two',
        three='three',
        four=JustForFKs.objects.create(),
        six=99.9,
    )
    actual = repr(instance)
    expected = "FourOrMoreFields(\n\tone='one',\n\ttwo='two',\n\tthree='three',\n\tfour_id=1,\n\tsix=99.9,\n)"

    assert actual == expected


@pytest.mark.django_db
def test_auto_configure_works():
    instance = WithoutDecorator.objects.create(
        one='one',
        two='two',
    )
    actual = repr(instance)
    expected = "WithoutDecorator(id=1, one='one', two='two')"
    assert actual == expected
