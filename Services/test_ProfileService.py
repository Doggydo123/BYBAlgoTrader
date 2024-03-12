import unittest
from Models.Profile import Profile
from DB import DBAutomation as DB
import ProfileService
from Models.Profile import Profile
import ProfileService
from unittest.mock import MagicMock


class ProfileServiceTests(unittest.TestCase):

    def setUp(self):
        # Set up test data
        self.test_profile = Profile(name="John", lastname="Doe", email="john.doe@example.com", username="johndoe", address="123 Main St", accountCreationDate="2022-01-01", accountType="Standard")

    def tearDown(self):
        # Clean up test data
        pass

    def test_getProfileById(self):
        # Create a mock database connection
        mock_db_connection = MagicMock()

        # Mock the cursor and its execute method
        mock_cursor = mock_db_connection.cursor.return_value
        mock_cursor.fetchone.return_value = (
            self.test_profile.id, self.test_profile.name, self.test_profile.lastname,
            self.test_profile.email, self.test_profile.username, self.test_profile.address,
            self.test_profile.accountCreationDate, self.test_profile.accountType
        )

        # Patch DB.getDBConection to return the mock connection
        with unittest.mock.patch('DB.DBAutomation.getDBConection', return_value=mock_db_connection):
            # Call the getProfileById function
            result = ProfileService.getProfileById(self.test_profile.id)

        # Check if the returned profile matches the test profile
        self.assertEqual(result.name, self.test_profile.name)
        self.assertEqual(result.lastname, self.test_profile.lastname)
        self.assertEqual(result.email, self.test_profile.email)
        self.assertEqual(result.username, self.test_profile.username)
        self.assertEqual(result.address, self.test_profile.address)
        self.assertEqual(result.accountCreationDate, self.test_profile.accountCreationDate)
        self.assertEqual(result.accountType, self.test_profile.accountType)

    def test_insertProfile(self):
        # Create a mock database connection
        mock_db_connection = MagicMock()

        # Patch DB.getDBConection to return the mock connection
        with unittest.mock.patch('DB.DBAutomation.getDBConection', return_value=mock_db_connection):
            # Call the insertProfile function
            profile_id = ProfileService.insertProfile(self.test_profile)

        # Check if the returned profile ID is not None
        self.assertIsNotNone(profile_id)

        # Check if the execute method was called with the correct arguments
        mock_db_connection.cursor.return_value.execute.assert_called_once()

if __name__ == '__main__':
    unittest.main()
