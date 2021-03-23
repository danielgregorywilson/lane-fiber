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
    OWNER_CHOICES = [
        ('EWEB', 'EWEB'),
        ('4J', '4J SD'),
        ('bethel', 'Bethel SD'),
        ('ESD', 'Lane ESD'),
        ('LTD', 'LTD'),
        ('LCOG', 'LCOG'),
        ('eugene', 'City of Eugene'),
        ('springfield', 'City of Springfield'),
        ('lane', 'Lane County'),
        ('SUB', 'SUB'),
        ('level3', 'Level 3'),
        ('UO', 'U of O'),
        ('other', 'Other')
    ]
    owner = models.CharField(max_length=11, choices=OWNER_CHOICES)
    other_owner = models.CharField(max_length=200, blank=True, null=True)
    MOUNT_TYPE_CHOICES = [
        ('rack', 'Rack'),
        ('frame', 'Frame'),
        ('cabinet', 'Cabinet')
    ]
    mount_type = models.CharField(max_length=7, choices=MOUNT_TYPE_CHOICES)
    MOUNT_TYPE_CHOICES = [
        ('free', 'Free Standing'),
        ('wall', 'Wall Mount')
    ]
    installation_type = models.CharField(max_length=4, choices=MOUNT_TYPE_CHOICES)
    LOCATION_TYPE_CHOICES = [
        ('indoors', 'Indoors'),
        ('outdoors', 'Outdoors')
    ]
    location_type = models.CharField(max_length=8, choices=LOCATION_TYPE_CHOICES)
    card_rows = models.CharField(max_length=200)
    card_columns = models.CharField(max_length=200)
    SLOT_ORIENTATION_CHOICES = [
        ('horizontal', 'Horizontal'),
        ('vertical', 'Vertical')
    ]
    slot_orientation = models.CharField(max_length=10, choices=SLOT_ORIENTATION_CHOICES)
    ports_per_card = models.CharField(max_length=200)
    PORT_TYPE_CHOICES = [
        ('SC', 'SC'),
        ('LC', 'LC'),
        ('ST', 'ST'),
        ('other', 'Other')
    ]
    port_type = models.CharField(max_length=5, choices=PORT_TYPE_CHOICES)
    other_port_type = models.CharField(max_length=200, blank=True, null=True)
    installation_date = models.CharField(max_length=200)
    INSTALLER_CHOICES = [
        ('EWEB', 'EWEB'),
        ('MFS', 'MFS'),
        ('astroTech', 'AstroTech'),
        ('other', 'Other')
    ]
    installer = models.CharField(max_length=9, choices=INSTALLER_CHOICES)
    other_installer = models.CharField(max_length=200, blank=True, null=True)
    MODEL_CHOICES = [
        ('BJ-1346', 'BJ-1346'),
        ('CCH-04U', 'CCH-04U'),
        ('FDC-001', 'FDC-001'),
        ('FDC-002', 'FDC-002'),
        ('FDC-005F', 'FDC-005F'),
        ('FL2000', 'FL2000'),
        ('WDC-001', 'WDC-001'),
        ('WDC-002', 'WDC-002'),
        ('other', 'Other')
    ]
    model = models.CharField(max_length=8, choices=MODEL_CHOICES)
    other_model = models.CharField(max_length=200, blank=True, null=True)
    comments = models.CharField(max_length=200, blank=True, null=True)
