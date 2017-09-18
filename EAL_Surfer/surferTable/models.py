# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Summarytablea(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'SummaryTableA'


class Summarytableb(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'SummaryTableB'


class Summarytablec(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'SummaryTableC'


class Summarytabled(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'SummaryTableD'


class Tablea1(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c10 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c11 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableA_1'


class Tablea2(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableA_2'


class Tableb1(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c10 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableB_1'


class Tableb2(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c10 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c11 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableB_2'


class Tablec1A(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableC_1a'


class Tablec1B(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableC_1b'


class Tablec2(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c10 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c11 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c12 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c13 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c14 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableC_2'


class Tablec3(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c10 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c11 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c12 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c13 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c14 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c15 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableC_3'


class Tabled1A(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableD_1a'


class Tabled1B(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableD_1b'


class Tabled1C(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableD_1c'


class Tabled1D(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableD_1d'


class Tabled2A(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableD_2a'


class Tabled2B(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableD_2b'


class Tabled2C(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableD_2c'


class Tabled3A(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c10 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c11 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c12 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c13 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c14 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableD_3a'


class Tabled3B(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableD_3b'


class Tabled4A(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableD_4a'


class Tabled4B(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableD_4b'


class Tabled4C(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableD_4c'


class Tabled4D(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableD_4d'


class Tabled4E(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c10 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c11 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c12 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c13 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c14 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c15 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c16 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c17 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableD_4e'


class Tabled4F(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableD_4f'


class Tabled5(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableD_5'


class Tablee(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c10 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c11 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c12 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c13 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c14 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c15 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c16 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c17 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableE'


class Tablef2(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c10 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableF_2'


class Tablef3(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c10 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c11 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c12 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableF_3'


class Tableg1(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c10 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c11 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c12 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableG_1'


class Tableg2(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableG_2'


class Tableg3(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableG_3'


class Tableg4(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableG_4'


class Tableh(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c10 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c11 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c12 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c13 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c14 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c15 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c16 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c17 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c18 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c19 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c20 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c21 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c22 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c23 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c24 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c25 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableH'


class Tablei1(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c10 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c11 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c12 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableI_1'


class Tablei2(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c10 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c11 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableI_2'


class Tablei3(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableI_3'

class Tablej(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c10 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c11 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c12 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c13 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c14 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c15 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c16 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableJ'

class Tablek(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableK'


class Tablel(models.Model):
    c1 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c1

    class Meta:
        managed = False
        db_table = 'TableL'


class Allchemicals(models.Model):
    c1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c3 = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    c4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c9 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c10 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c11 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c12 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c13 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c14 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c15 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c16 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c17 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c18 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c19 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c20 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c21 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c22 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c23 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c24 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c25 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c26 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c27 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c28 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c29 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c30 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c31 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c32 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c33 = models.TextField(blank=True, null=True)  # This field type is a guess.

    # return the name of field to display in admin mode
    def __str__(self):
        return self.c3

    class Meta:
        managed = False
        db_table = 'allchemicals'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
