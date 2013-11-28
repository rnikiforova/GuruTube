from django.test import TestCase
from videos.models import Tag
from django.db.utils import DataError, IntegrityError

class TagTestCase(TestCase):
    def test_create_tag_content_is_hair(self):
        '''Asserts that a tag with content "hair" is correctly stored in the database'''
        CONTENT_TEXT = "hair"
        tag = Tag(content=CONTENT_TEXT)
        tag.save()
        database_tag = Tag.objects.get(content=CONTENT_TEXT)
        self.assertEqual(database_tag.content, CONTENT_TEXT)

    def test_create_three_tags(self):
        '''Asserts that three tags have been correctly stored in the database'''
        first_tag = Tag(content = "beauty")
        first_tag.save()
        second_tag = Tag(content = "make up")
        second_tag.save()
        third_tag = Tag(content = "nail polish")
        third_tag.save()
        tags_count = Tag.objects.all().count()
        self.assertEqual(tags_count, 3)
        
    def test_tag_content_longer_than_max_length(self):
        '''Asserts that the insert fails when max_length of content is exceeded'''
        tag = Tag(content = "Very long content")
        self.assertRaises(DataError, tag.save)
        
    def test_content_cannot_be_none(self):
        '''Asserts that the insert fails when content is None'''
        tag = Tag(content=None)
        self.assertRaises(IntegrityError, tag.save)
        
    def test_content_can_be_empty_string(self):
        '''Asserts that the content can be an empty string'''
        tag = Tag(content=str())
        tag.save()
        database_tag = Tag.objects.get(content=str())
        self.assertEqual(database_tag.content, str())
        
    def test_content_update_in_database(self):
        '''Asserts that the content can be updated in the database'''
        INITIAL_CONTENT = "make up"
        UPDATED_CONTENT = "beauty"
        tag = Tag(content=INITIAL_CONTENT)
        tag.save()
        database_tag = Tag.objects.get(content=INITIAL_CONTENT)
        database_tag.content = UPDATED_CONTENT
        database_tag.save()
        initial_content_tags_count = Tag.objects.filter(content__exact=INITIAL_CONTENT).count()
        self.assertEqual(initial_content_tags_count, 0)