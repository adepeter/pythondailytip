from django.test import TestCase# Create your tests here.from ..models import PythonTipHashTagclass TestHashtag(TestCase):    def setUp(self):        self.hash_tag = PythonTipHashTag.objects.create(name='django')    def test_hash_tag_is_smallcase(self):        self.assertEqual(self.hash_tag.name, 'django')    def test_hash_tag_cannot_contain_uppercase(self):        self.assertNotEqual(self.hash_tag.name, 'django'.swapcase())