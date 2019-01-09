import torch

first_counter = torch.Tensor([0])
second_counter = torch.Tensor([10])
some_value = torch.Tensor(15)
# print("some_value:", some_value)
print("first_counter:", first_counter)
print("second_counter:", second_counter, "\n")

while(first_counter < second_counter)[0]:
    first_counter += 2
    second_counter += 1
    # print("some_value:", some_value)
    print("first_counter:", first_counter)
    print("second_counter:", second_counter, "\n")


# # tensorflow version
# import tensorflow as tf
#
# first_counter = tf.constant(0)
# second_counter = tf.constant(10)
# some_value = tf.Variable(15)
#
# # condition should handle all args:
# def cond(first_counter, second_counter, *args):
#     return first_counter < second_counter
#
# def body(first_counter, second_counter, some_value):
#     first_counter = tf.add(first_counter, 2)
#     second_counter = tf.add(second_counter, 1)
#     return first_counter, second_counter, some_value
#
#
# c1, c2, val = tf.while_loop(cond, body, [first_counter, second_counter, some_value])
# with tf.Session() as sess:
#     sess.run(tf.global_variable_initializer())
#     counter_1_res, counter_2_res = sess.run([c1, c2])







