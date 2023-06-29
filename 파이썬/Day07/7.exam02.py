
# mutable (변경 가능한)
# - 리스트, 딕셔너리 타입은 변경 가능 
# ex) def func(a):
#       a[0] = "HELLO"
#
#   a = ["hello", "hi"]
#   print(a)    => ["hello", "hi"]
#   func(a)
#   print(a)    => ["HELLO", "hi"]
#
#
# immutable (변경 불가능한)
# - 튜플, 기본 데이터 타입은 변경 불가능
# ex) def func(a):
#       a = "HELLO"
#       print("func: ", a)
#
#   a = "hello"
#   func(a)     => "HELLO"
#   print(a)    => "hello"