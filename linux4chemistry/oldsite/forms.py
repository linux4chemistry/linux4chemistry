from django import forms

LICENSE_NAMES = [
    'Open Source',
    'Freeware',
    'Free for academics',
    'Shareware',
    'Commercial'
    ]

CATEGORIES = [
    ('MD', 'Molecular Dynamics'),
    ('Viewer', '3D Viewer'),
    ('QM', 'Quantum Mechanics'),
    ('Rxn', 'Reactions'),
    ('Draw', '2D Draw'),
    ('Xtal', 'Crystallography'),
    ('NMR', 'NMR'),
    ('Cheminf', 'Cheminformatics'),
    ('MM', 'Molecular Mechanics'),
    ('Dock', 'Docking'),
    ('Thermo', 'Thermodynamics'),
    ('MS', 'Mass Spectrometry'),
    ('Electrochemistry', 'Electrochemistry'),
    ('Education', 'Education'),
    ]

CATEGORIES.sort()

CATEGORY_CHOICES = ( 
    [('all', 'All categories'),] +
    CATEGORIES +
    [('other', 'Other categories'),]
    )

CATEGORIES = dict(CATEGORIES)

class Linux4ChemistryForm(forms.Form):
    
    open_source = forms.BooleanField()
    freeware = forms.BooleanField()
    free_for_academics = forms.BooleanField()
    shareware = forms.BooleanField()
    commercial = forms.BooleanField()

    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

