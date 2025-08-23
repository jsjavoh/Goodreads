from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class RegisterTeatCase(TestCase):

    def setUp(self):
        User.objects.create_user(
            username='js',
            first_name='Javohir',
            last_name='Sattorov',
            email='jsjavoh@gmail.com',
            password='Asd12345'
        )

    def test_register(self):
        response = self.client.post(
            reverse('user:register'),
            data={
                'username':'adi',
                'first_name':'adham',
                'last_name':'dadamirzayev',
                'email':'adi@gmail.com',
                'password':'Adi12345',
                'password_confirm':'Adi12345'
            }
        )
        user_count = User.objects.count()
        user = User.objects.get(username='adi')
        self.assertEqual(user_count, 2)
        self.assertEqual(user.first_name, 'adham')
        self.assertEqual(user.last_name, 'dadamirzayev')
        self.assertEqual(user.email, 'adi@gmail.com')
        self.assertTrue(user.check_password('Adi12345'))

    def test_requied(self):
        response = self.client.post(
            reverse('user:register'),
            data={
                'fist_name':'xumoy',
                'last_name':'nasriyev',
            }
        )

        user_cout = User.objects.count()
        self.assertEqual(user_cout, 1)
        self.assertFormError(response.context['form'],'username','This field is required.')
        self.assertFormError(response.context['form'], 'password', 'This field is required.')
        self.assertFormError(response.context['form'],'password_confirm','This field is required.')

    def test_password_confirm(self):
        response = self.client.post(
            reverse('user:register'),
            data={
                'username':'adi',
                'first_name':'adham',
                'last_name':'dadamirzayev',
                'email':'adi@gmail.com',
                'password':'Adi12345',
                'password_confirm':'Adi123456'
            }
        )
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
        self.assertFormError(response.context['form'],'password_confirm','Parol maydonlariga bir xil qiymat kiritilishi shart!')
