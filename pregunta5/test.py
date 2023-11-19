import unittest
from main import Type, TypeManager, mcm, is_command_valid


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.type_manager = TypeManager()

    def test_init(self):
        self.assertTrue(self.type_manager.types == {})

    def test_mcm(self):
        self.assertTrue(mcm([1]) == 1)
        self.assertTrue(mcm([0]) == 0)
        self.assertTrue(mcm([2, 3, 5]) == 30)
        self.assertIsNone(mcm([]))

    def test_is_command_valid(self):
        self.assertTrue(is_command_valid(['SALIR']))
        self.assertTrue(is_command_valid(['ATOMICO', 'nombre', '1', '1']))
        self.assertFalse(is_command_valid(['ATOMICO']))
        self.assertTrue(is_command_valid(['STRUCT', 'nombre', 'a', 'b']))
        self.assertFalse(is_command_valid(['STRUCT']))
        self.assertTrue(is_command_valid(['UNION', 'nombre', 'a', 'b']))
        self.assertFalse(is_command_valid(['UNION']))
        self.assertTrue(is_command_valid(['DESCRIBIR', 'nombre']))
        self.assertFalse(is_command_valid(['DESCRIBIR']))

    def test_type_manager_atomic(self):
        self.type_manager.atomic('int', 4, 4)
        self.assertEqual(self.type_manager.types['int'].name, 'int')
        self.assertEqual(self.type_manager.types['int'].aln, 4)
        self.assertEqual(self.type_manager.types['int'].rep, [4, 4, 4])

        self.assertIsNone(self.type_manager.atomic('int', 5, 5))
        self.assertEqual(self.type_manager.types['int'].name, 'int')
        self.assertEqual(self.type_manager.types['int'].aln, 4)
        self.assertEqual(self.type_manager.types['int'].rep, [4, 4, 4])

    def test_type_manager_struct(self):
        self.type_manager.atomic('bool', 2, 1)
        self.type_manager.atomic('char', 2, 2)
        self.type_manager.atomic('int', 4, 4)
        self.type_manager.atomic('double', 8, 8)

        self.assertIsNone(self.type_manager.struct('s', ['a', 'b', 'c']))
        self.assertEqual(len(self.type_manager.types), 4)

        self.type_manager.struct('s', ['int', 'char', 'int', 'double', 'bool'])
        self.assertEqual(self.type_manager.types['s'].name, 's')
        self.assertEqual(self.type_manager.types['s'].aln, 8)
        self.assertEqual(self.type_manager.types['s'].rep, [25, 19, 19])

        self.assertIsNone(self.type_manager.struct('s', ['int', 'double', 'bool']))
        self.assertEqual(self.type_manager.types['s'].name, 's')
        self.assertEqual(self.type_manager.types['s'].aln, 8)
        self.assertEqual(self.type_manager.types['s'].rep, [25, 19, 19])

    def test_type_manager_union(self):
        self.type_manager.atomic('foo', 2, 8)
        self.type_manager.atomic('bar', 3, 6)
        self.type_manager.atomic('baz', 4, 2)

        self.assertIsNone(self.type_manager.union('u', ['a', 'b', 'c']))
        self.assertEqual(len(self.type_manager.types),  3)

        self.type_manager.union('u', ['foo', 'bar', 'baz'])
        self.assertEqual(self.type_manager.types['u'].name, 'u')
        self.assertEqual(self.type_manager.types['u'].aln, 12)
        self.assertEqual(self.type_manager.types['u'].rep, [8, 8, 8])

        self.assertIsNone(self.type_manager.union('u', ['foo', 'foo', 'foo']))
        self.assertEqual(self.type_manager.types['u'].name, 'u')
        self.assertEqual(self.type_manager.types['u'].aln, 12)
        self.assertEqual(self.type_manager.types['u'].rep, [8, 8, 8])
