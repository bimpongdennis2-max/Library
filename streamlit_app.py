print('Welcome to the Library')
library_dictionary = {}
while True :
    print(f"1.Add book,\n2.Borrow book,\n3.Display All books,\n4.Exit")
    g= input('Enter your choice: ')
       
    
    def add_book(book_title, number_of_copies) : 
       library_dictionary [book_title] = number_of_copies
       return library_dictionary
        

    if g == '1' : 
       book_title  = input ("Book title :")
       number_of_copies = int(input ("Number of copies :"))
       X = add_book(book_title , number_of_copies)

       while True : 
          Z = input('Do you want to input another book : ')
          if Z == 'Yes' : 
              book_title1 = input ("Book title :")
              if book_title1 == book_title or book_title1 in library_dictionary : 
                 new_number_of_copies = int(input('new_number_of_copies:'))
                 library_dictionary[book_title1] = (new_number_of_copies + number_of_copies )
           
              else : 
                 number_of_copies1 =int(input("Number of copies:"))
                 y = add_book(book_title1, number_of_copies1)
           
          if Z == 'No' :
              print(f"Thank you\nGoodbye.")
              print(library_dictionary)             
              break
        
        
    if g == '2' : 
       d = input('What book do you want to borrow: ')      
       if d in library_dictionary : 
          print(f"Book borrowed successfully")
          for d in library_dictionary:
             library_dictionary[d] -= 1
             print(library_dictionary)
       elif d in library_dictionary == 0 :
             print('Book not available')
                  
       elif d != library_dictionary: 
             print('Book not found')
             
    
    if g == '3' :
        for l in library_dictionary:
            print(l)
        if library_dictionary == {}: 
            print('There are currently no books in the library ')       
    if g == '4' : 
        print('Goodbye.\nThank you for using the Library system')   
        break
        
                                    
            
                 
                 
 