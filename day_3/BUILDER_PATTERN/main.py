from director import Director
from concrete_builder import ConcreteBuilder

director = Director()
builder = ConcreteBuilder()

director.builder = builder

print("\nobiekt minimalny")
director.build_minimal_version()
builder.product.list_parts()

print("\nobiekt pełny")
director.build_full_version()
builder.product.list_parts()

print("\nobiekt specjalny (AC)")
builder.produce_part_a()
builder.produce_part_c()
builder.product.list_parts()
#
# obiekt minimalny
# Cześć produktu: PartA1
# obiekt pełny
# Cześć produktu: PartA1, PartB1, PartC1
# obiekt specjalny (AC)
# Cześć produktu: PartA1, PartC1
# Process finished with exit code 0