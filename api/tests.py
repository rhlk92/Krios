from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

class TodoTest(APITestCase):

    def create_todo(self):
        data = {'description':'remember the milk'}
        return self.client.post('/api/tasks/', data)

    def test_todo_list(self):
        response = self.create_todo()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get('/api/tasks/')
        expected_data = {'id':1, 'description':'remember the milk','completed':False}

        self.assertEqual(len(response.data), 1)
        entry = response.data[0]
        self.assertEqual(entry, expected_data)

    def test_todo_detail(self):
        self.create_todo()

        data = {'description':'remember the milk','completed':True}
        response = self.client.put('/api/tasks/1', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/api/tasks/1')
        expected_data = {'id':1, 'description':'remember the milk','completed':True}
        self.assertEqual(response.data, expected_data)

        response = self.client.delete('/api/tasks/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
