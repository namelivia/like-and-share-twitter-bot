from unittest import TestCase
from like_and_share_twitter_bot.bot import Bot
import mock


class TestBot(TestCase):
    def setUp(self):
        self.subs = mock.Mock()
        self.text_clip = mock.Mock()
        self.video_clip = mock.Mock()
        self.twitter = mock.Mock()
        self.gif = mock.Mock()
        self.bot = Bot(
            self.subs,
            self.text_clip,
            self.video_clip,
            self.twitter,
            self.gif
        )

    def test_runnig(self):
        quote_mock = mock.Mock()
        quote_mock.content = 'some quote'
        video_clip_mock = mock.Mock()
        text_clip_mock = mock.Mock()
        self.subs.get_random.return_value = quote_mock
        self.video_clip.generate_quote_video.return_value = video_clip_mock
        self.text_clip.generate_quote_text.return_value = text_clip_mock
        self.bot.run()
        self.subs.get_random.assert_called_once_with()
        self.video_clip.generate_quote_video.assert_called_once_with(
            quote_mock
        )
        self.text_clip.generate_quote_text.assert_called_once_with(quote_mock)
        self.gif.generate_composite_gif.assert_called_once_with(
            video_clip_mock,
            text_clip_mock
        )
        self.twitter.post_gif.assert_called_once_with(quote_mock.content)
