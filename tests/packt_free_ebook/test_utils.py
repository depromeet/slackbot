import unittest
from unittest import mock
from src.cron.packt_free_ebook.utils import get_today_free_ebook_title


def _mock_scraper(raise_exception=False):
    mock_book_title = mock.Mock()

    if raise_exception:
        mock_book_title.side_effect = FileNotFoundError
    else:
        mock_book_title.return_value = 'TEST TITLE'

    return mock_book_title


class FreeBookScraperTest(unittest.TestCase):
    @unittest.skip('Test not fully implemented')
    @mock.patch('src.cron.packt_free_ebook.utils.get_today_free_ebook_title')
    def test_successful_scraping(self, mock_scraper):
        mock_book_title = _mock_scraper()
        mock_scraper.return_value = mock_book_title

        result = get_today_free_ebook_title()
        self.assertEqual(result, 'TEST TITLE')

    @unittest.skip('Test not fully implemented')
    @mock.patch('src.cron.packt_free_ebook.utils.get_today_free_ebook_title')
    def test_failed_scraping(self, mock_scraper):
        pass


if __name__ == '__main__':
    unittest.main()
