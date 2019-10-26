import math


bukin_function = lambda x, y: 100 * math.sqrt(abs(y - 0.01 * pow(x, 2))) + 0.01 * abs(x + 10)
makkormik_function = lambda x, y: math.sin(x + y) + pow(x - y, 2) - 1.5 * x + 2.5 * y + 1
but_function = lambda x, y: pow(x + 2 * y - 7, 2) + pow(2 * x + y - 5, 2)
rastrigin_function = lambda x, a: a * len(x) + sum([pow(x[i], 2) - a * math.cos(2 * math.pi * x[i])
                                            for i in range(len(x))])
ekli_function = lambda x, y: -20 * math.exp(-0.2 * math.sqrt(0.5 * (pow(x, 2) + pow(y, 2)))) - \
                             math.exp(0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y))) + math.e + 20
sphere_function = lambda x: sum([pow(el, 2) for el in x])
rosenbrock_function = lambda x: sum([100 * pow(x[i+1] - pow(x[i], 2), 2) + pow(x[i] - 1, 2)]
                                    for i in range(len(x) - 1))
bill_function = lambda x, y: pow(1.5 - x + x * y, 2) + pow(2.25 - x + x * pow(y, 2), 2) + pow(2.625 - x + x * pow(y, 3), 2)
goldman_price_function = lambda x, y: (1 + pow(x + y + 1, 2) * (19 - 14 * x + 3 * pow(x, 2) -
                                                                14 * y + 6 * x * y + 3 * pow(y, 2))
                                       ) * (30 + pow(2 *x - 3 * y, 2) * (18 - 32 * x + 12 * pow(x, 2) +
                                                                         48 * y - 36 * x * y + 27 * pow(y, 2)))
matias_function = lambda x, y: 0.26 * (pow(x, 2) + pow(y, 2)) - 0.48 * x * y
levi_function = lambda x, y: pow(math.sin(3 * math.pi * x), 2) + pow(x-1, 2) * (1 + pow(math.sin(3 * math.pi * y), 2)) + pow(y-1, 2) * (1 + pow(math.sin(2 * math.pi * y), 2))
himmelblay_function = lambda x, y: pow(pow(x, 2) + y - 11, 2) + pow(x + pow(y, 2) - 7, 2)
camel_function = lambda x, y: 2*pow(x, 2) - 1.05*pow(x, 4) + pow(x, 6)/6 + x*y + pow(y, 2)
isom_function = lambda x, y: -math.cos(x)*math.cos(y)*math.exp(-(pow(x-math.pi, 2) + pow(y-math.pi, 2)))
cross_in_tray_function = lambda x, y: -0.0001 * pow(abs(math.sin(x) * math.sin(y) * math.exp(abs(100 - math.sqrt(pow(x, 2) + pow(y, 2)) / math.pi))) + 1, 0.1)
egnholder_function = lambda x, y: - (y + 47) * math.sin(math.sqrt(abs(x/2 + y + 47))) - x * math.sin(abs(x - (y + 47)))
holder_function = lambda x, y: -abs(math.sin(x) * math.cos(x) * math.exp(abs(1 - math.sqrt(pow(x, 2) + pow(y, 2)) / math.pi)))
shaffer_function_v2 = lambda x, y: 0.5 + (pow(math.sin(pow(x, 2) - pow(y, 2)), 2) - 0.5) / pow(1 + 0.001 * (pow(x, 2) + pow(y, 2)), 2)
shaffer_function_v4 = lambda x, y: 0.5 + (pow(math.cos(math.sin(abs(pow(x, 2) - pow(y, 2)))), 2) - 0.5) / pow(1 + 0.001 * (pow(x, 2) + pow(y, 2)), 2)
stibinsky_tang_funciton = lambda x, y: sum([pow(x[i], 4) - 16 * pow(x[i], 2) + 5 * x[i] for i in range(len(x))])

functions_limitations = {'bukin': {'function': bukin_function,
                                   'upper': [-5, 3],
                                   'lower': [-15, -3]},
                         'makkormik': {'function': makkormik_function,
                                       'upper': [4, 4],
                                       'lower': [-1.5, -3]},
                         'but': {'function': but_function,
                                 'upper': [10, 10],
                                 'lower': [-10, -10]},
                         'rastrigin': {'function': rastrigin_function,
                                       'upper': [5.12],
                                       'lower': [-5.12]},
                         'ekli': {'function': ekli_function,
                                  'upper': [5, 5],
                                  'lower': [-5, -5]},
                         'sphere': {'function': sphere_function},
                         'rosenbrock': {'function': rosenbrock_function},
                         'bill': {'function': bill_function,
                                  'upper': [4.5, 4.5],
                                  'lower': [-4.5, 4.5]},
                         'goldman_price': {'function': goldman_price_function,
                                           'upper': [2, 2],
                                           'lower': [-2, -2]},
                         'matias': {'function': matias_function,
                                           'upper': [10, 10],
                                           'lower': [-10, -10]},
                         'levi': {'function': levi_function,
                                    'upper': [10, 10],
                                    'lower': [-10, -10]},
                         'himmelblay': {'function': himmelblay_function,
                                    'upper': [5, 5],
                                    'lower': [-5, -5]},
                         'camel': {'function': camel_function,
                                    'upper': [5, 5],
                                    'lower': [-5, -5]},
                         'isom': {'function': isom_function,
                                    'upper': [100, 100],
                                    'lower': [-100, -100]},
                         'cross_in_tray': {'function': cross_in_tray_function,
                                    'upper': [10, 10],
                                    'lower': [-10, -10]},
                         'egnholder': {'function': egnholder_function,
                                    'upper': [512, 512],
                                    'lower': [-512, -512]},
                         'holder': {'function': holder_function,
                                    'upper': [10, 10],
                                    'lower': [-10, -10]},
                         'shaffer_v2': {'function': shaffer_function_v2,
                                    'upper': [100, 100],
                                    'lower': [-100, -100]},
                         'shaffer_v4': {'function': shaffer_function_v4,
                                    'upper': [100, 100],
                                    'lower': [-100, -100]},
                         'stibinsky_tanng': {'function': stibinsky_tang_funciton,
                                    'upper': [5],
                                    'lower': [-5]},
                         }
