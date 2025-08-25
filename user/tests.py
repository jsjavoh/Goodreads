from django.contrib.auth.middleware import get_user
from django.template.context_processors import request
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


class LoginTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(
            username='js',
            first_name='Javohir',
            last_name='Sattorov',
            email='jsjavoh@gmail.com',
            password='Asd12345'
        )

    def test_logout(self):
        self.client.login(username='js', password='Asd12345')

        response = self.client.get(reverse('user:logout'))

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)


    def test_login(self):
        response = self.client.post(
            reverse('user:login'),
            data={
                'username':'js',
                'password':'Asd12345'
            }
        )

        self.assertRedirects(response, reverse('home'))
        self.assertEqual(response.status_code, 302)

    def test_login_wrong(self):
        response = self.client.post(
            reverse('user:login'),
            data={
                'username': 'js',
                'password': 'xatoparol'
            }
        )
        self.assertFormError(response.context['form'], None, 'Validate username or password')
        self.assertEqual(response.status_code, 200)


class ProfileTestCase(TestCase):

    def test_no_requried(self):
        response = self.client.get(reverse('user:profile'))

        self.assertEqual(response.url, reverse('user:login')+"?next=/users/profile/")
        self.assertEqual(response.status_code, 302)

    def test_profile_detail(self):

        user = User.objects.create_user(
            username='js',
            first_name='Javohir',
            last_name='Sattorov',
            email='jsjavoh@gmail.com',
            password='Asd12345'
        )

        self.client.login(username='js', password='Asd12345')

        response = self.client.get(reverse('user:profile'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, user.username)
        self.assertContains(response, user.first_name)
        self.assertContains(response, user.last_name)
        self.assertContains(response, user.email)

    def test_profile_edit(self):

        user = User.objects.create_user(
            username='js',
            first_name='Javohir',
            last_name='Sattorov',
            email='jsjavoh@gmail.com',
            password='Asd12345'
        )

        self.client.login(username='js', password='Asd12345')

        response = self.client.post(
            reverse('user:profile-edit'),
            data={
            'username':'jsf',
            'first_name':'Javohir',
            'last_name':'Sattorov',
            'email':'jsjavoh@gmail.com'
        })

        user.refresh_from_db()
        self.assertEqual(response.url, reverse('user:profile'))
        self.assertEqual(user.username, 'jsf')
        self.assertEqual(response.status_code, 302)

    def test_profile_edit_username(self):
        user = User.objects.create_user(
            username='js',
            first_name='Javohir',
            last_name='Sattorov',
            email='jsjavoh@gmail.com',
            password='Asd12345'
        )
        user2 = User.objects.create_user(
            username='jsf',
            first_name='Javohir',
            last_name='Sattorov',
            email='jsjavoh@gmail.com',
            password='Asd12345'
        )
        self.client.login(username='js', password='Asd12345')

        response = self.client.post(
            reverse('user:profile-edit'),
            data={
                'username': 'jsf',
                'first_name': 'Javohir',
                'last_name': 'Sattorov',
                'email': 'jsjavoh@gmail.com'
            })

        self.assertFormError(response.context['form'],'username','Bu username allaqachon db\'da mavjud')