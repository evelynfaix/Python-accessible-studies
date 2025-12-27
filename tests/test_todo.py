import os
import json
import tempfile
import unittest
from starter_code import todo_cli

class TestTodoCLI(unittest.TestCase):
    def test_add_save_load(self):
        tasks = []
        tasks = todo_cli.add_task(tasks, 'task one')
        self.assertEqual(len(tasks), 1)
        fd, path = tempfile.mkstemp(suffix='.json')
        os.close(fd)
        try:
            todo_cli.save_tasks(tasks, filename=path)
            loaded = todo_cli.load_tasks(filename=path)
            self.assertEqual(loaded[0]['title'], 'task one')
        finally:
            os.remove(path)

    def test_complete_task(self):
        tasks = []
        tasks = todo_cli.add_task(tasks, 'task two')
        ok = todo_cli.complete_task(tasks, 0)
        self.assertTrue(ok)
        self.assertTrue(tasks[0]['done'])

if __name__ == '__main__':
    unittest.main()
