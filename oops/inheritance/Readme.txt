Python throws an MRO error because class z inherits from both x and y, while y already inherits from x, creating an inconsistent inheritance hierarchy that violates C3 linearization.

MRO is the order in which Python searches base classes when executing a method.

