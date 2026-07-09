from classes.status import Status
from unittest import TestCase, main


class TestStatus(TestCase):

    def setUp(self):
        self.obj = Status()

    def test_add_status(self):
        val_test = ["Niveau1", "Niveau2", "Niveau3"]

        for status in val_test:
            self.obj.add_status(status)

        result = self.obj.get_status()

        noms = []
        for status in result:
            noms.append(status[1])

        self.assertIn(val_test[0], noms)
        print('Bravo Jeremie')

    def test_edit_status(self):
        val_test = "Niveau1"
        val_test2 = "Niveau4"

        ident = self.obj.get_status_id(val_test)

        self.obj.edit_status(ident, val_test2)

        result = self.obj.get_status()

        noms = []
        for status in result:
            noms.append(status[1])

        self.assertIn(val_test2, noms)
        self.assertNotIn(val_test, noms)
        print("Jeremie you are the best and i love you")



    def test_remove_status(self):
        val_test = ["Niveau4", "Niveau2", "Niveau3"]

        idents = []
        for status in val_test:
            idents.append(self.obj.get_status_id(status))

        for ident in idents:
            self.obj.remove_status(ident)

        print("Jeremie you are the king of python")


    if __name__ == "__main__":
        main()