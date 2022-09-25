from django.test import TestCase
import pytest

# Create your tests here.

from . import category_tree as ct
from . import category_node as cn


class TestCategoryTree:

    def creation_of_tree(self) -> ct.CategoryTree:
        """
        Method for creating category tree:

        :return tree:
        """
        t = ct.CategoryTree()
        n1 = t.add_root("1", "name1", "description1", "image1")
        n11 = n1.add_child("11", "name11", "description11", "image11")
        n111 = n11.add_child("111", "name111", "description111", "image111")
        n12 = n1.add_child("12", "name12", "description12", "image12")
        n13 = t.add_child(n1, "13", "name13", "description13", "image13")

        n2 = t.add_root("2", "name2", "description2", "image2")
        n2.add_child("21", "name21", "description21", "image21")
        n22 = t.add_child(n2, "22", "name22", "description22", "image22")

        n3 = t.add_root("3", "name3", "description3", "image3")
        n3.add_child("31", "name31", "description31", "image31")
        n32 = t.add_child(n3, "32", "name32", "description32", "image32")
        n33 = t.add_child(n3, "33", "name33", "description33", "image33")

        return t

    def print_created_tree(self, t):
        """
        Method for printing the tree

        :param:
        :return:
        """
        print()
        print("children of root: 1")
        t.print_children(t.roots['1'])

        print("children of root: 2")
        t.print_children(t.roots['2'])

        print("children of root: 3")
        t.print_children(t.roots['3'])

    def test_editing_of_category(self):
        """
        Test method for editing the category

        :param:
        :return:
        """
        t = self.creation_of_tree()
        category_id = "13"
        root_id = '1'
        nn1 = t.get_child(t.roots[root_id], category_id)
        nn1.edit_child('name14', 'description14', 'image14')
        t.set_child(t.roots[root_id], category_id, nn1)
        self.print_created_tree(t)
        assert t.roots[root_id].children[category_id].category_id == category_id
        assert t.roots[root_id].children[category_id].name == 'name14'
        assert t.roots[root_id].children[category_id].description == 'description14'
        assert t.roots[root_id].children[category_id].image == 'image14'


    def test_moving_category(self):
        """
        Test method for moving the category
        :return:
        """
        t = self.creation_of_tree()
        moving_category_id = '21'
        from_root_id = '2'
        to_root_id = '3'
        t.move_child(moving_category_id, from_root_id, to_root_id)
        self.print_created_tree(t)
        assert t.roots[to_root_id].children[moving_category_id].category_id == moving_category_id
        assert t.roots[to_root_id].children[moving_category_id].name == 'name21'
        assert t.roots[to_root_id].children[moving_category_id].description == 'description21'
        assert t.roots[to_root_id].children[moving_category_id].image == 'image21'
        assert len(t.roots[from_root_id].children) == 1  # only '21

    def test_deleting_category(self):
        """
        Test method for deleting a category from its parent
        :return:
        """
        t = self.creation_of_tree()
        removing_category_id = '32'
        from_root_id = '3'
        t.delete_child(removing_category_id, from_root_id)
        self.print_created_tree(t)
        assert len(t.roots[from_root_id].children) == 2  # element is deleted

    def test_return_sub_children(self):
        """
        Testing returning children of a parent

        :param:
        :return:
        """
        t = self.creation_of_tree()
        root_id = '2'
        category_id = '21'
        sub_children = t.get_children(root_id)
        assert sub_children[category_id].category_id == category_id
        assert sub_children[category_id].name == 'name21'
        assert sub_children[category_id].description == 'description21'
        assert sub_children[category_id].image == 'image21'
        assert len(sub_children) == 2  # '21' and '22'


