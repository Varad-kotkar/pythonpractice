book = {
    "title": "Python",
    "price": 500,
    "author": "Guido"
}
removed_price=book.pop("price")
# print(book)
# print(removed_price)
book.pop("titl","not found")
print(book.pop("titl","not found"))