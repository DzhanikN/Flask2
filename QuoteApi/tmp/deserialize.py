from author import Author
from schema import AuthorSchema
json_data = """
{
"name": "Ivan",
"email": "ivan@mail.ru"
}
"""
schema = AuthorSchema()
result = schema.load(json_data)
print(result)