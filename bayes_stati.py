import sys
# example 1:
'''
a=0.001 # youbing
b=0.999 # jiankang
a_p = 0.95
a_n = 0.05 # x
b_p = 0.02
b_n = 0.98 # X

p_a_p = a*a_p
p_b_p = b*b_p
print(p_a_p,p_b_p)
print(p_a_p/(p_a_p+p_b_p))
print(p_b_p/(p_a_p+p_b_p))
'''
# example 2:
a=0.7 # liugan
b=0.3 # putong
a_p = 0.8
a_n = 0.2 # x
b_p = 0.1
b_n = 0.9 # X
# if observation result is positive:
p_a_p = a*a_p
p_b_p = b*b_p
print(p_a_p,p_b_p)
print(p_a_p/(p_a_p+p_b_p))
print(p_b_p/(p_a_p+p_b_p))
# if observation result is negative:
p_a_n = a*a_n
p_b_n = b*b_n
print(p_a_n,p_b_n)
print(p_a_n/(p_a_n+p_b_n))
print(p_b_n/(p_a_n+p_b_n))