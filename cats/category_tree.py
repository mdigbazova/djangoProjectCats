from . import category_node as cn


class CategoryTree:
    """
    Category tree
    """

    def __init__(self):
        """
        Init of Category Tree
        """
        self.roots = {}

    def add_root(self, category_id, name, description, image, similar_to=None):
        """
        Adds roots into the tree

        :param category_id:
        :param name:
        :param description:
        :param image:
        :param similar_to:
        :return:
        """
        node = cn.Category(category_id, name, description, image)
        self.roots[category_id] = node
        return node

    def add_child(self, parent, category_id, name, description, image):
        """
        Adds child into a parent

        :param parent:
        :param category_id:
        :param name:
        :param description:
        :param image:
        :return:
        """
        return parent.add_child(category_id, name, description, image)

    def get_child(self, parent, category_id) -> cn.Category:
        """
        Returns a child

        :param parent:
        :param category_id:
        :return:
        """
        return parent.children[category_id]

    def set_child(self, parent, category_id, modified_child):
        """
        Sets a child in a position

        :param parent:
        :param category_id:
        :param modified_child:
        :return:
        """
        parent.children[category_id] = modified_child

    def print_children(self, parent):
        """
        Prints all the children in a parent

        :param parent:
        :return:
        """
        for key, value in parent.children.items():
            print(value)
            if value.children:
                for key1, value1 in value.children.items():
                    print(value1)

    def move_child(self, category_id, from_category_id, to_category_id):
        """
        Moving a category from a category to another category
        :param category_id:
        :param from_category_id:
        :param to_category_id:
        :return:
        """
        moving_child = self.roots[from_category_id].children.pop(category_id)
        self.roots[to_category_id].children[category_id] = moving_child

    def delete_child(self, category_id, from_category_id):
        """
        Deletes a category from a parent category
        :param category_id:
        :param from_category_id:
        :return:
        """
        self.roots[from_category_id].children.pop(category_id)

    def get_children(self, parent_id):
        """
        Gets all the children in a parent
        :param parent_id:
        :return:
        """
        return_sub_children = {}
        for key, value in self.roots[parent_id].children.items():
            return_sub_children[key] = value
        return return_sub_children
