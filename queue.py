import unittest


class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
                
    
    def __init__(self):
        self.in_stack  = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:

            # Move items from in_stack to out_stack, reversing order
            while len(self.in_stack) > 0:
                newest_in_stack_item = self.in_stack.pop()
                self.out_stack.append(newest_in_stack_item)

            # If out_stack is still empty, raise an error
            if len(self.out_stack) == 0:
                raise IndexError("Can't dequeue from empty queue!")

        return self.out_stack.pop()      
                
                








# Tests

class Test(unittest.TestCase):

    def test_queue_usage(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)