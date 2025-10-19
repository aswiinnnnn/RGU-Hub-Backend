# Generated manually to fix out-of-sync PostgreSQL sequences for AutoField PKs
from django.db import migrations

RESET_SQL = [
    # Reset sequence for resources_program.id
    """
    SELECT setval(
        pg_get_serial_sequence('resources_program', 'id'),
        COALESCE((SELECT MAX(id) FROM resources_program), 1),
        (SELECT COUNT(*) > 0 FROM resources_program)
    );
    """,
    # Reset sequence for resources_syllabus.id
    """
    SELECT setval(
        pg_get_serial_sequence('resources_syllabus', 'id'),
        COALESCE((SELECT MAX(id) FROM resources_syllabus), 1),
        (SELECT COUNT(*) > 0 FROM resources_syllabus)
    );
    """,
    # Reset sequence for resources_term.id
    """
    SELECT setval(
        pg_get_serial_sequence('resources_term', 'id'),
        COALESCE((SELECT MAX(id) FROM resources_term), 1),
        (SELECT COUNT(*) > 0 FROM resources_term)
    );
    """,
    # Reset sequence for resources_subject.id
    """
    SELECT setval(
        pg_get_serial_sequence('resources_subject', 'id'),
        COALESCE((SELECT MAX(id) FROM resources_subject), 1),
        (SELECT COUNT(*) > 0 FROM resources_subject)
    );
    """,
    # Reset sequence for resources_materialtype.id
    """
    SELECT setval(
        pg_get_serial_sequence('resources_materialtype', 'id'),
        COALESCE((SELECT MAX(id) FROM resources_materialtype), 1),
        (SELECT COUNT(*) > 0 FROM resources_materialtype)
    );
    """,
    # Reset sequence for resources_subjectmaterial.id
    """
    SELECT setval(
        pg_get_serial_sequence('resources_subjectmaterial', 'id'),
        COALESCE((SELECT MAX(id) FROM resources_subjectmaterial), 1),
        (SELECT COUNT(*) > 0 FROM resources_subjectmaterial)
    );
    """,
]


def forwards(apps, schema_editor):
    if schema_editor.connection.vendor != 'postgresql':
        return
    with schema_editor.connection.cursor() as cursor:
        for sql in RESET_SQL:
            cursor.execute(sql)


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0008_alter_materialtype_options_alter_program_options_and_more'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
