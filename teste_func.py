def test_func():
  assert func(2,4,3) == 3

def test_negativo():
  assert func(-1,-1,-1) == -1

def test_decimal():
  assert func(1.1,2.1,3.1) == 2.1
  
def test_zero():
  assert(0,0,0) == 0
      
