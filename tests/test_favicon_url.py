import unittest
import asyncio
from pyfavicon import Favicon
from yarl import URL

CASES = [
    ('<link rel="icon" href="/icon.png">', 'https://gitlab.com/icon.png'),
    ('<link rel="icon" href="://gitlab.com/icon.png">',
     'https://gitlab.com/icon.png'),
    ('<link rel="shortcut icon" type="image/png" href="/uploads/-/system/appearance/favicon/1/GnomeLogoVertical.svg.png">',
    'https://gitlab.com/uploads/-/system/appearance/favicon/1/GnomeLogoVertical.svg.png')
]


class TestFaviconUrl(unittest.TestCase):
    def setUp(self):
        self.favicon = Favicon()

    def test_favicon_url(self):
        async def run_tests():
            favicon = Favicon()
            for html_content, expected_result in CASES:
                icons = await favicon.from_html(html_content,
                                                website_url=URL("https://gitlab.com"))
                self.assertEqual(str(icons[0].link), expected_result)
        asyncio.run(run_tests())


if __name__ == "__main__":
    unittest.main()
