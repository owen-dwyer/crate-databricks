"""
crate_anon/crateweb/consent/migrations/0007_auto_20170228_1052.py

===============================================================================

    Copyright (C) 2015, University of Cambridge, Department of Psychiatry.
    Created by Rudolf Cardinal (rnc1001@cam.ac.uk).

    This file is part of CRATE.

    CRATE is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    CRATE is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with CRATE. If not, see <https://www.gnu.org/licenses/>.

===============================================================================

**Consent app, migration 0007.**

"""

# Generated by Django 1.10.5 on 2017-02-28 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("consent", "0006_auto_20170206_1617"),
    ]

    operations = [
        migrations.AddField(
            model_name="consentmode",
            name="source",
            field=models.CharField(
                default="crate_user_entry",
                max_length=20,
                verbose_name="Source database used for lookup, or "
                "crate_user_entry/crate_auto_created",
            ),
        ),
        migrations.AlterField(
            model_name="patientlookup",
            name="source_db",
            field=models.CharField(
                choices=[
                    ("dummy_clinical", "Dummy clinical database for testing"),
                    ("cpft_crs", "CPFT Care Records System (CRS) 2005-2012"),
                    (
                        "cpft_rio_rcep",
                        "CPFT RiO 2013- (preprocessed by Servelec RCEP tool)",
                    ),
                    ("cpft_rio_crate", "CPFT RiO 2013- (raw)"),
                ],
                max_length=20,
                verbose_name="Source database used for lookup",
            ),
        ),
    ]
