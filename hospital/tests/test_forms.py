from django.test import SimpleTestCase
from hospital.forms import YourHealthEditForm


class FormTest(SimpleTestCase):

    def test_yourhealtheditform_valid(self):
        yhform = YourHealthEditForm(data={
            'height': 181,
            'weight': 71,
            'diseases': "test disease",
            'medicines': "test meds",
            'ts': "test ts"
        })
        self.assertTrue(yhform.is_valid())
    
    def test_yourhealtheditform_invalid(self):
        yhform = YourHealthEditForm(data={
            'height': 181,
            'weight': 71,
            'disease': 8989,
            'medicines': "test meds",
            'ts': "test ts"
        })

        self.assertFalse(yhform.is_valid())
        self.assertEquals(len(yhform.errors),1)