
def push(stack, element):
  """
  Add value in to the stack
  """
  stack.append(element)

def pop(stack):
  """
  Remove last value ever pushed
  """
  return print(stack.pop())

def peek(stack):
  return print("peek value: {}".format(stack[-1]))

def is_empty(stack):
  """
  Check and print stack is empty or not
  """
  if len(stack)==0:
    print(True)
  else:
    print(False)


if __name__=='__main__':
  stack_1 = []
  push(stack_1, 1)
  push(stack_1, 2)
  push(stack_1, 3)

  print(stack_1)
  peek(stack_1)

  pop(stack_1)
  pop(stack_1)
  pop(stack_1)
