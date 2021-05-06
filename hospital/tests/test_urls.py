from django.test import SimpleTestCase
from django.urls import reverse, resolve
from hospital.views import home_view,bookapp_view,calladoc_view,feedback_view


class TestUrls(SimpleTestCase):

    def test_urls_is_resolved(self):
        url = reverse('')
        self.assertEquals(resolve(url).func,home_view)
    
    def test_urls_is_resolved_bookapp(self):
        url = reverse('bookapp.html')
        self.assertEquals(resolve(url).func,bookapp_view)
    
    def test_urls_is_resolved_calladoc(self):
        url = reverse('calladoc.html')
        self.assertEquals(resolve(url).func,calladoc_view)
    
    def test_urls_is_resolved_feedback(self):
        url = reverse('feedback.html')
        self.assertEquals(resolve(url).func,feedback_view)