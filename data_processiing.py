import pandas as pd

class Book_Crossing_Dataset_Processor:
    def __init__(self, bx_users, bx_books, bx_book_ratings):
        self.bx_users = bx_users
        self.bx_books = bx_books
        self.bx_ratings = bx_book_ratings
    
    def read_csv(self, filename):
        df = pd.read_csv(filename, sep = ';', encoding='latin-1')
        return df
    
    def process_bx_users(self):
        df = self.read_csv(self.bx_users)
        
        # Fill 'Age' with median value
        median = df['Age'].median()
        df['Age'] = df['Age'].fillna(median)
        
        # Split 'Location' into 'City', 'State' and 'Country'
        # df[['City', 'State', 'Country']] = df['Location'].str.split(', ', expand=True)
        # del df['Location']
        # print (df['City'].unique()

        return df


if __name__ == '__main__':
    BX_USERS = 'book-crossing-dataset/BX-Users.csv'
    BX_BOOKS = 'book-crossing-dataset/BX-BOOKS.csv'
    BX_BOOK_RATINGS = 'book-crossing-dataset/BX-BOOK_RATINGS.csv'

    object = Book_Crossing_Dataset_Processor(BX_USERS, BX_BOOKS, BX_BOOK_RATINGS)
    df = object.process_bx_users()
    print(df.head(-10))