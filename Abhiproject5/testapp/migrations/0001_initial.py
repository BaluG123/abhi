# Generated by Django 3.2.3 on 2022-03-20 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(choices=[('finolex', 'Finolex'), ('sudhakar', 'Sudhakar'), ('meco', 'Meco'), ('lt', 'LT'), ('lk', 'LK'), ('mascot', 'Mascot')], max_length=16)),
                ('Item_Name', models.CharField(max_length=1000)),
                ('Item_Image', models.FileField(blank=True, null=True, upload_to='cables/')),
                ('meter', models.CharField(max_length=150)),
                ('thickness', models.CharField(max_length=150)),
                ('Price', models.IntegerField()),
                ('Offered_Price', models.IntegerField()),
                ('Offer', models.IntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('post', 'Post')], default='post', max_length=10)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Motar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(choices=[('kirloskar', 'Kirloskar'), ('slv', 'SLV'), ('ashirvad', 'Ashirvad'), ('vguard', 'V-Guard'), ('sharpplus', 'Sharp Plus'), ('mascot', 'Mascot')], max_length=16)),
                ('choose', models.CharField(choices=[('inwater', 'In Water'), ('outsidewater', 'OutSide Water')], max_length=15)),
                ('Item_Name', models.CharField(max_length=1000)),
                ('Item_Image', models.FileField(blank=True, null=True, upload_to='motars/')),
                ('hp', models.CharField(max_length=150)),
                ('stage', models.CharField(max_length=150)),
                ('feet', models.CharField(max_length=150)),
                ('Price', models.IntegerField()),
                ('Offered_Price', models.IntegerField()),
                ('Offer', models.IntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('post', 'Post')], default='post', max_length=10)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_type', models.CharField(choices=[('paint', 'Paint'), ('pvc', 'Pvc'), ('steel', 'Steel'), ('sheet', 'Sheet'), ('flat', 'Flat'), ('angle', 'Angle'), ('motar', 'Motar'), ('cables', 'Cables'), ('pvcfittings', 'Pvcfittings'), ('tanks', 'Tanks'), ('others', 'Others'), ('channel', 'Channel')], max_length=20)),
                ('Item_Name', models.CharField(max_length=2000)),
                ('Item_Image', models.FileField(blank=True, null=True, upload_to='new/')),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('Price', models.IntegerField()),
                ('Offered_Price', models.IntegerField()),
                ('Offer', models.IntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('post', 'Post')], default='post', max_length=10)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Others',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_Name', models.CharField(max_length=1000)),
                ('Item_Image', models.FileField(blank=True, null=True, upload_to='others/')),
                ('Price', models.IntegerField()),
                ('Offered_Price', models.IntegerField()),
                ('Offer', models.IntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('post', 'Post')], default='post', max_length=10)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Paint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_Name', models.CharField(max_length=1000)),
                ('Item_Image', models.FileField(blank=True, null=True, upload_to='paints/')),
                ('company', models.CharField(choices=[('asianPaints', 'asianpaints'), ('indigo paints', 'INDIGO Paints'), ('agsar paints', 'Agsar Paints'), ('mrf Paints', 'MRF Paints'), ('berger paints', 'Berger Paints'), ('birla paints', 'Birla Paints')], max_length=15)),
                ('volume', models.CharField(max_length=150)),
                ('Price', models.IntegerField()),
                ('Offered_Price', models.IntegerField()),
                ('Offer', models.IntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('post', 'Post')], default='post', max_length=10)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Pvc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_Name', models.CharField(max_length=1000)),
                ('Item_Image', models.FileField(blank=True, null=True, upload_to='pvcs/')),
                ('company', models.CharField(choices=[('supreme', 'Supreme'), ('a1 plast', 'A1 PLAST'), ('spectra', 'Spectra'), ('mahesh', 'Mahesh'), ('others', 'Others')], max_length=15)),
                ('length', models.CharField(max_length=150)),
                ('size', models.CharField(max_length=150)),
                ('Price', models.IntegerField()),
                ('Offered_Price', models.IntegerField()),
                ('Offer', models.IntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('post', 'Post')], default='post', max_length=10)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='PvcFittings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_Name', models.CharField(max_length=1000)),
                ('Item_Image', models.FileField(blank=True, null=True, upload_to='pvcfittings/')),
                ('size', models.CharField(max_length=150)),
                ('ltrs', models.CharField(max_length=10)),
                ('Price', models.IntegerField()),
                ('Offered_Price', models.IntegerField()),
                ('Offer', models.IntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('post', 'Post')], default='post', max_length=10)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet', models.CharField(choices=[('asper', 'Asper'), ('gc', 'GC'), ('colourcoated', 'Colour Coated'), ('fibre', 'Fibre')], max_length=20)),
                ('Item_Name', models.CharField(max_length=1000)),
                ('Item_Image', models.FileField(blank=True, null=True, upload_to='sheets/')),
                ('company', models.CharField(choices=[('ramco', 'Ramco'), ('jsw', 'JSW'), ('uttam', 'Uttam'), ('amns', 'AMNS'), ('jindal', 'Jindal'), ('kamdenu', 'Kamdenu'), ('charminar', 'Charminar')], max_length=15)),
                ('colour', models.CharField(choices=[('gray', 'Gray'), ('silver', 'Silver'), ('skyblue', 'SkyBlue'), ('brickred', 'Brick red'), ('green', 'Green'), ('yellow', 'Yellow'), ('red', 'Red'), ('transparent', 'TransParent')], max_length=15)),
                ('length', models.CharField(max_length=150)),
                ('width', models.CharField(max_length=150)),
                ('thickness', models.CharField(max_length=150)),
                ('Price', models.IntegerField()),
                ('Offered_Price', models.IntegerField()),
                ('Offer', models.IntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('post', 'Post')], default='post', max_length=10)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Steel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steel', models.CharField(choices=[('tmt', 'TMT'), ('tube', 'Tube'), ('plain sheet', 'Plain Sheet')], max_length=15)),
                ('Item_Name', models.CharField(max_length=1000)),
                ('Item_Image', models.FileField(blank=True, null=True, upload_to='sheets/')),
                ('company', models.CharField(choices=[('sk', 'SK'), ('tata', 'TATA'), ('indus', 'Indus'), ('kamdenu', 'Kamdenu'), ('a1gold', 'A1 Gold'), ('jindal', 'Jindal'), ('jsw', 'JSW')], max_length=15)),
                ('size', models.CharField(max_length=150)),
                ('Price', models.IntegerField()),
                ('Offered_Price', models.IntegerField()),
                ('Offer', models.IntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('post', 'Post')], default='post', max_length=10)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Tanks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(choices=[('supreme', 'Supreme'), ('ashirvad', 'Ashirvad'), ('hitank', 'Hitank'), ('ganga', 'Ganga'), ('premium plus', 'Premium Plus'), ('kaveri', 'Kaveri'), ('prestige', 'Prestige'), ('vastuganga', 'Vastuganga')], max_length=15)),
                ('type', models.CharField(choices=[('roto mold', 'Roto Mold'), ('blow mold', 'Blow Mold')], max_length=15)),
                ('Item_Name', models.CharField(max_length=1000)),
                ('Item_Image', models.FileField(blank=True, null=True, upload_to='tanks/')),
                ('ltrs', models.CharField(max_length=100)),
                ('colour', models.CharField(max_length=20)),
                ('Price', models.IntegerField()),
                ('Offered_Price', models.IntegerField()),
                ('Offer', models.IntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('post', 'Post')], default='post', max_length=10)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Tsheets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steel', models.CharField(choices=[('flat', 'FLAT'), ('angle', 'ANGLE'), ('channel', 'CHANNEL')], max_length=10)),
                ('Item_Name', models.CharField(max_length=1000)),
                ('Item_Image', models.FileField(blank=True, null=True, upload_to='tsheets/')),
                ('size', models.CharField(max_length=100)),
                ('thickness', models.CharField(max_length=100)),
                ('angle_size', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('Offered_Price', models.IntegerField()),
                ('Offer', models.IntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('post', 'Post')], default='post', max_length=10)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]