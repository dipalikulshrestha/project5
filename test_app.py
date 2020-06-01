import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy
from database.models import setup_db, Actors, Movies
from app import create_app


class CapstoneTestCase(unittest.TestCase):
    """This class represents the capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client()
        self.db_path = os.environ['DATABASE_URL']
        self.token = os.environ['TOKEN_TEST']
        setup_db(self.app, self.db_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_actor = {
            "name": "Pooja",
            "age": 21,
            "gender": "Female"
        }

        self.new_movie = {
            "title": "In Fabric",
            "releasedate": "28-09-2019"
        }

        self.update_actor = {
            "age": 28
        }

        self.update_movie = {
            "title": "DDLJ"
        }

        # Valid Token passed from environment
        self.authorization = {
            "Authorization": self.token
        }

        # Invalid Token
        self.authorization_exp = {
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9IdDMzYVgzQkRxWUphR1Z4czREaiJ9.eyJpc3MiOiJodHRwczovL2RpcGFsaWsuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlY2ZjZjNmNGZjNmI0MGQwMzlkZDJhYiIsImF1ZCI6IkNhcEFQSSIsImlhdCI6MTU5MDk4Mjc0NywiZXhwIjoxNTkwOTg5OTQ3LCJhenAiOiJjczdaYkVRNkJvRlRENDNwTUpSTlFKUUViWXpxVFpQZSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOltdfQ.SSgR2_Hw_D-WiHdFjRYpWRgB_mPUNhVcetZY2_pJhXE_PHwR10p3ZSpH0_cR6jfBt6Rvojwe7Ca0nX5385PvvyxWoTbjfDn4oO5pykJCE74R8IJM-N9gSNv4rlaUPS9GmB2X0NBqPGUUbvlG4lbzwb8U0IBtCb-fsvBeHAp-BPJL6IGBgyXr8wyrVrpZHuk7zbOsVnCHRjlnmPFHOtIvS7-QLYM-WBksPlsKwZ15VhvnOaDgxXptGKOOHx-z0H6JKA7N1SZ2bxzCfOgbC8R41VlkVLLMspOG_hO0YjxXQJ-JGjOAxFNYsADrYDOnsjQaBdQunRDYOrPgOGRROalsVg"
        }

    def tearDown(self):
        """Executed after each test"""
        pass

    def test_a_get_api_request(self):

        res = self.client.get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['Message']))

    def test_b_create_actors(self):

        res = self.client.post(
            '/actors', json=self.new_actor,
            headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_c_create_movies(self):

        res = self.client.post(
            '/movies', json=self.new_movie,
            headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_d_get_actors(self):

        res = self.client.get('/actors', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_e_get_movies(self):

        res = self.client.get('/movies', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_f_get_actors_by_id(self):

        res = self.client.get('/actors/1', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_g_get_movies_by_id(self):

        res = self.client.get('/movies/1', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_h_update_actors(self):

        res = self.client.patch('/actors/1',
                                json=self.update_actor,
                                headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_i_update_movies(self):

        res = self.client.patch('/movies/1',
                                json=self.update_movie,
                                headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_j_404_get_actors_by_id(self):

        res = self.client.get('/actors/100', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_k_404_get_movies_by_id(self):

        res = self.client.get('/movies/100', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_l_404_delete_actors_not_exist(self):

        res = self.client.delete('/actors/;;;', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_m_404_delete_movies_not_exist(self):

        res = self.client.delete('/movies/;;;', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_n_404_update_actors(self):

        res = self.client.patch('/actors/100',
                                json=self.update_actor,
                                headers=self.authorization,)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_o_404_update_movies(self):

        res = self.client.patch('/movies/100',
                                json=self.update_movie,
                                headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_p_delete_actors(self):

        res = self.client.delete('/actors/1', headers=self.authorization, )
        data = json.loads(res.data)

        actors = Actors.query.filter(Actors.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actors, None)

    def test_q_delete_movies(self):

        res = self.client.delete('/movies/1', headers=self.authorization, )
        data = json.loads(res.data)

        movies = Movies.query.filter(Movies.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movies, None)

    def test_r_401_auth_missing(self):

        res = self.client.get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')

    def test_s_403_unauthorized(self):

        res = self.client.get('/actors', headers=self.authorization_exp, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')


if __name__ == "__main__":
    unittest.main()
