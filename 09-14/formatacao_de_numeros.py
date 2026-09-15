x = 2 ** 0.5
y = 5 ** 0.5


# .n n casas depois da decimal
# d (int) ou f (float) formato
print(format(x, ".3f"))
print(x, "+", y, "=", x + y)
print(f"{x:.2f} + {y:.2f} = {x + y:.2f}")