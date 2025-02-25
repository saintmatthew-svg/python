import unittest
import toDoList

class TestToDoList(unittest.TestCase):

    def test_that_show_menu_exist(self):
        toDoList.show_menu()
        
    def test_that_show_menu_print_menu(self):
        result = toDoList.show_menu()
        output = """
            1. Add a task
            2. View all tasks
            3. Mark a task as complete
            4. Delete a task
            5. Exit
    """  
        self.assertEqual(result,output)
        
    def test_that_add_task_exist(self):
        toDoList.add_task()
             
    def test_that_add_task_collect_task_input(self):
        result = toDoList.add_task()
        expected = "'food' added to the list."
        self.assertEqual(result, expected)  

    def test_that_view_task_exist(self):
        toDoList.view_tasks()    
        
    def test_that_view_task_shows_task(self):
        result = toDoList.view_tasks()
        expected = "TASK: [ ]food"
        self.assertEqual(result, expected)       

    def test_that_mark_task_exist(self):
        toDoList.mark_task_as_completed()   
    
    def test_that_mark_task_marks(self):
        result = toDoList.mark_task_as_completed()
        expected = " TASK: [X]food"
        expect =  "TASK: [ ]food"
        self.assertEqual(result, expected, expect)       

    
if __name__ == '__main__':
    unittest.main()