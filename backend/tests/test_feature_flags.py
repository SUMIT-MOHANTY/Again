import os
import json
import unittest
from backend.app import create_app
from backend.app.feature_flags.middleware import is_feature_enabled
from backend.app.feature_flags.store import FEATURE_FLAGS

class TestFeatureFlags(unittest.TestCase):
    def setUp(self):
        # Ensure a clean env var and store for each test
        os.environ.pop('FEATURE_FLAGS_JSON', None)
        FEATURE_FLAGS.clear()
        self.app = create_app()
        self.client = self.app.test_client()

    def test_load_from_env(self):
        os.environ['FEATURE_FLAGS_JSON'] = json.dumps({
            'env_flag': {'enabled': True, 'description': 'from env'}
        })
        # Reload flags after setting env var
        from backend.app.feature_flags.store import load_feature_flags
        load_feature_flags()
        self.assertIn('env_flag', FEATURE_FLAGS)
        self.assertTrue(is_feature_enabled('env_flag'))

    def test_api_toggle_create(self):
        resp = self.client.post('/api/flags/new_flag', json={'enabled': True, 'description': 'test'}, headers={'X-Admin': '1'})
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertTrue(data['enabled'])
        self.assertTrue(is_feature_enabled('new_flag'))

    def test_api_toggle_update(self):
        # Create first
        self.client.post('/api/flags/toggle_flag', json={'enabled': True}, headers={'X-Admin': '1'})
        # Update to False
        resp = self.client.post('/api/flags/toggle_flag', json={'enabled': False, 'description': 'off'}, headers={'X-Admin': '1'})
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(is_feature_enabled('toggle_flag'))

    def test_admin_protection(self):
        resp = self.client.get('/api/flags')
        self.assertEqual(resp.status_code, 403)

if __name__ == '__main__':
    unittest.main()
