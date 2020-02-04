# FIXME (1): Prompt for four weights. Add all weights to a list. Output list.
users_weight = []
for i in range(0,1):
    x = input('Enter weight 1: \n')
    users_weight.append(float(x))
    x = input('Enter weight 2: \n')
    users_weight.append(float(x))
    x = input('Enter weight 3: \n')
    users_weight.append(float(x))
    x = input('Enter weight 4: \n')
    users_weight.append(float(x))
    print('')
    
print('Weights:',users_weight)

# FIXME (2): Output average of weights.
average_weights = sum(users_weight) / float(len(users_weight))
print('Average weight:', average_weights)

# FIXME (3): Output max weight from list.
max_weight = max(users_weight)
print('Max weight: %s\n' % max_weight)

# FIXME (4): Prompt the user for a list index and output that weight in pounds and kilograms.
index_value = (input('Enter a list index (1 - 4): \n'))
if index_value == '1':
    index_value = users_weight[0]
    print('Weight in pounds:', index_value)
    index_value = users_weight[0] * 0.45359237
    rounded_value = round(index_value)
    print('Weight in kilograms: %.1f\n' % rounded_value)
elif index_value == '2':
    index_value = users_weight[1]
    print('Weight in pounds:', index_value)
    index_value = users_weight[1] * 0.45359237
    rounded_value = round(index_value)
    print('Weight in kilograms: %.1f\n' % rounded_value)
elif index_value == '3':
    index_value = users_weight[2]
    print('Weight in pounds:', index_value)
    index_value = users_weight[2] * 0.45359237
    rounded_value = round(index_value)
    print('Weight in kilograms: %.1f\n' % rounded_value)
else:
    index_value = users_weight[3]
    print('Weight in pounds:', index_value)
    index_value = users_weight[3] * 0.45359237
    rounded_value = round(index_value)
    print('Weight in kilograms: %.1f\n' % rounded_value)
    
# FIXME (5): Sort the list and output it.
users_weight.sort()
print('Sorted list:', users_weight)
