class Category:
    """
    Creates category
    """

    def __init__(self, category_id, name, description, image):
        """
        Init method of category

        :param category_id:
        :param name:
        :param description:
        :param image:
        """
        self.category_id = category_id
        self.name = name
        self.description = description
        self.image = image
        self.children = {}

    def add_child(self, category_id, name, description, image):
        """
        Adds child to parent

        :param category_id:
        :param name:
        :param description:
        :param image:
        :return:
        """
        n = Category(category_id, name, description, image)
        self.children[category_id] = n
        return n

    def edit_child(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image

    def __str__(self):
        return (f"Node is {self.category_id}, "
                f"name: {self.name}, description: {self.description}, image: {self.image}")
