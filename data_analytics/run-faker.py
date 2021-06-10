from faker.factory import Factory

Faker = Factory.create
fake = Faker()
fake.seed(0)
fake = Faker("en_US")

print(
    fake.csv(
        header=None,
        data_columns=("{{name}}", "{{job}}", "{{address}}"),
        num_rows=1000,
        include_row_ids=False,
    )
)
