from project.social_media import SocialMedia
from unittest import TestCase,main

class TestSocialMedia(TestCase):
    def setUp(self):
        self.aide_bg = SocialMedia('aide_bg','YouTube',100,'family')

    def testinit(self):
        self.assertEqual('aide_bg',self.aide_bg._username)
        self.assertEqual('YouTube',self.aide_bg.platform)
        self.assertEqual(100,self.aide_bg.followers)
        self.assertEqual('family',self.aide_bg._content_type)
        self.assertEqual([],self.aide_bg._posts)

    # def test_followers_seter_raises(self):
    #     with self.assertRaises(ValueError) as ex:
    #         SocialMedia('ivo','YouTube',5-6,'all')
    #     self.assertEqual("Followers cannot be negative.",str(ex.exception))

    def test_validate_and_set_platform(self):
        with self.assertRaises(ValueError) as ex:
            SocialMedia('Emo',"vbox7",50,'action')
        self.assertEqual("Platform should be one of ['Instagram', 'YouTube', 'Twitter']",str(ex.exception))

    def test_create_post(self):
        result = self.aide_bg.create_post('cheep vs expensive')
        self.assertEqual("New family post created by aide_bg on YouTube.",result)

    def test_liked_poste(self):
        self.aide_bg.create_post('cheep vs expensive')
        resullt = self.aide_bg.like_post(0)
        self.assertEqual("Post liked by aide_bg.",resullt)

    def test_max_likes(self):
        self.aide_bg.create_post('cheep vs expensive')
        self.aide_bg.create_post('cheep vs expensive')
        self.aide_bg.create_post('cheep vs expensive')
        self.aide_bg.create_post('cheep vs expensive')
        self.aide_bg.create_post('cheep vs expensive')
        self.aide_bg.create_post('cheep vs expensive')
        self.aide_bg.create_post('cheep vs expensive')
        self.aide_bg.create_post('cheep vs expensive')
        self.aide_bg.create_post('cheep vs expensive')
        self.aide_bg.create_post('cheep vs expensive')
        self.aide_bg.create_post('cheep vs expensive')
        self.aide_bg.like_post(0)
        self.aide_bg.like_post(0)
        self.aide_bg.like_post(0)
        self.aide_bg.like_post(0)
        self.aide_bg.like_post(0)
        self.aide_bg.like_post(0)
        self.aide_bg.like_post(0)
        self.aide_bg.like_post(0)
        self.aide_bg.like_post(0)
        self.aide_bg.like_post(0)
        resullt = self.aide_bg.like_post(0)
        self.assertEqual("Post has reached the maximum number of likes.", resullt)

    def test_invalid_post_index_max_ind(self):
        self.aide_bg.create_post('cheep vs expensive')
        self.aide_bg.like_post(0)

        resullt = self.aide_bg.like_post(2)
        self.assertEqual("Invalid post index.", resullt)

    def test_invalid_post_index_min_ind(self):
        self.aide_bg.create_post('cheep vs expensive')
        self.aide_bg.like_post(0)

        resullt = self.aide_bg.like_post(-2)
        self.assertEqual("Invalid post index.", resullt)

    def test_comend_on_post(self):
        self.aide_bg.create_post('cheep vs expensive')
        self.aide_bg.like_post(0)

        resullt = self.aide_bg.comment_on_post(0,'12345678909')
        self.assertEqual("Comment added by aide_bg on the post.", resullt)

    def test_comend_on_post_less_than_10_charecters(self):
        self.aide_bg.create_post('cheep vs expensive')
        self.aide_bg.like_post(0)

        resullt = self.aide_bg.comment_on_post(0,'123456789')
        self.assertEqual("Comment should be more than 10 characters.", resullt)


if __name__ == '__main__':
    main()