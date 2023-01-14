import xml.etree.ElementTree as ET

tree = ET.parse("compiler.xml")
root = tree.getroot()

for book in root.findall('book'):
    bookID = book.get('id')
    authorName = book.find('author').text
    title = book.find('title').text
    genre = book.find('genre').text
    price = book.find('price').text
    publishDate = book.find('publish_date').text
    description = book.find('description').text

    print("**********Book Data**********")
    print("Book ID: " + bookID)
    print("Author: " + authorName)
    print("Book Title: " + title)
    print("Genre: " + genre)
    print("Price: " + price)
    print("Dare of Publish: " + publishDate)
    print("Book Description: " + description)
    print("**********Thank you!**********\n")