from django.db import models


class Infrastructure(models.Model):
    class Meta:
        abstract = True

    uploaded_at = models.DateTimeField("datetime uploaded", auto_now_add=True)


class Cable(Infrastructure):
    location = models.CharField(max_length=200)
    fiber_strand_count = models.CharField(max_length=200)
    STRAND_CONFIG_CHOICES = [
        ('12', 'Typical Tube Color Order – 12 strands/tube'),
        ('6', 'Typical Tube Color Order– 6 strands/tube'),
        ('other', 'Other')
    ]
    strand_config = models.CharField(max_length=5, choices=STRAND_CONFIG_CHOICES)
    other_strand_config = models.CharField(max_length=200, blank=True, null=True)
    CABLE_TYPE_CHOICES = [
        ('ADSSMini', 'ADSS Mini-Span'),
        ('ADSSMedium', 'ADSS Medium'),
        ('ADSSTransmission', 'ADSS Transmission'),
        ('UGArmored', 'UG Armored'),
        ('OPGW', 'OPGW'),
        ('ABF', 'ABF'),
        ('other', 'Other')
    ]
    cable_type = models.CharField(max_length=16, choices=CABLE_TYPE_CHOICES)
    other_cable_type = models.CharField(max_length=200, blank=True, null=True)
    INFRASTRUCTURE_CLASS_CHOICES = [
        ('backbone', 'Backbone'),
        ('lateral', 'Lateral'),
        ('pigtail', 'Pigtail')
    ]
    infrastructure_class = models.CharField(max_length=8, choices=INFRASTRUCTURE_CLASS_CHOICES)
    FOOT_STAMP_UNITS_CHOICES = [
        ('foot', 'Foot'),
        ('meter', 'Meter')
    ]
    foot_stamp_units = models.CharField(max_length=5, choices=FOOT_STAMP_UNITS_CHOICES)
    foot_stamp_number = models.CharField(max_length=200)
    MANUFACTURER_CHOICES = [
        ('3M', '3M'),
        ('AFL', 'AFL Telecom'),
        ('alcatel', 'Alcatel'),
        ('ATT', 'AT&T'),
        ('belde', 'Belde'),
        ('chromatic', 'Chromatic Tech'),
        ('draka', 'Draka USA'),
        ('OFS', 'OFS'),
        ('OCC', 'Optical Cable Corp'),
        ('prysmian', 'Prysmian/Pirelli'),
        ('remmee', 'Remmee Products Corp'),
        ('other', 'Other')
    ]
    manufacturer = models.CharField(max_length=9, choices=MANUFACTURER_CHOICES)
    other_manufacturer = models.CharField(max_length=200, blank=True, null=True)
    manufacturer_catalog_number = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    OWNER_CHOICES = [
        ('EWEB', 'EWEB'),
        ('city', 'City'),
        ('LCOG', 'LCOG'),
        ('SUB', 'SUB'),
        ('level3', 'LEVEL 3'),
        ('LSN', 'LSN'),
        ('other', 'Other')
    ]
    owner = models.CharField(max_length=6, choices=OWNER_CHOICES)
    other_owner = models.CharField(max_length=200, blank=True, null=True)
    INSTALLER_CHOICES = [
        ('EWEB', 'EWEB'),
        ('MFS', 'MFS'),
        ('astroTech', 'AstroTech'),
        ('other', 'Other')
    ]
    installer = models.CharField(max_length=9, choices=INSTALLER_CHOICES)
    other_installer = models.CharField(max_length=200, blank=True, null=True)
    comments = models.CharField(max_length=200, blank=True, null=True)


class Panel(Infrastructure):
    location = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    mount_type = models.CharField(max_length=200)
    installation_type = models.CharField(max_length=200)
    location_type = models.CharField(max_length=200)
    card_rows = models.CharField(max_length=200)
    card_columns = models.CharField(max_length=200)
    slot_orientation = models.CharField(max_length=200)
    ports_per_card = models.CharField(max_length=200)
    port_type = models.CharField(max_length=200)
    installation_date = models.CharField(max_length=200)
    installer = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    comments = models.CharField(max_length=200, blank=True, null=True)
