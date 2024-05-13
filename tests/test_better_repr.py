import pytest

from tests.example_project.myapp.models import (
    FourOrLessFields,
    FourOrMoreFields,
    JustForFKs,
    WithoutDecorator, JustForM2Ms,
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


@pytest.mark.xfail(reason="Unsaved models are not by default compared by field values")
@pytest.mark.django_db
def test_repr_eval_not_saved_no_fks_no_m2ms():
    instance = WithoutDecorator(
        one='one',
        two='two',
    )
    actual = instance
    expected = eval(repr(actual))
    assert actual == expected


@pytest.mark.django_db
def test_repr_eval_saved_no_fks_no_m2ms():
    instance = WithoutDecorator.objects.create(
        one='one',
        two='two',
    )
    actual = instance
    expected = eval(repr(actual))
    assert actual == expected


@pytest.mark.django_db
def test_repr_eval_saved_fks_no_m2ms():
    instance = FourOrLessFields.objects.create(
        one='one',
        two='two',
        three=2,
        four=JustForFKs.objects.create(),
    )
    actual = instance
    expected = eval(repr(actual))

    assert actual == expected
    assert actual.four == expected.four


@pytest.mark.django_db
def test_repr_eval_saved_fks_m2ms():
    instance = FourOrMoreFields.objects.create(
        one='one',
        two='two',
        three=2,
        four=JustForFKs.objects.create(),
        six=99.0
    )
    instance.five.add(JustForM2Ms.objects.create())
    actual = instance
    expected = eval(repr(actual))
    assert actual == expected
    assert list(actual.five.all()) == list(expected.five.all())
