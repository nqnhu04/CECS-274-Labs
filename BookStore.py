import algorithms
import Book
import SortableBook
import ArrayQueue
import ArrayList
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
import AdjacencyList
import time
import DLList
import MaxStack



class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''
    def __init__(self) :
        self.bookCatalog = DLList.DLList()
        self.shoppingCart = MaxStack.MaxStack()
        self.indexKey = ChainedHashTable.ChainedHashTable()
        self.indexSortedTitle = BinarySearchTree.BinarySearchTree()
        self.bookSortedCatalog = ArrayList.ArrayList()
        self.similaGraph = AdjacencyList.AdjacencyList(0)
        

    def loadCatalog(self, fileName : str) :
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        with open(fileName,encoding='utf8') as f:
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                b = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(b)
                self.indexKey.add(key, self.bookCatalog.size()-1)
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

        self.similaGraph = AdjacencyList.AdjacencyList(self.bookCatalog.size())
        for i in range(self.bookCatalog.size()):
            l = self.bookCatalog[i].similar.split()
            for k in range(1,len(l)):
                j = self.indexKey.find(l[k])  
                if j is not None:
                    self.similaGraph.add_edge(i,j)
        
        return self.bookCatalog.size()
    def addBookByIndex(self, i : int) :
        '''
        addBookByIndex: Inserts into the shopping cart the book with index i
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.push(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def addBookByKey(self, s : str) :
        '''
        addBookByIndex: Inserts into the shopping cart the book with key s
        input: 
            s: key string    
        '''
        if s == "":
            print("Invalid key. Try again.")
        else:
            i = self.indexKey.find(s)
            if i!=None:
                self.shoppingCart.push(self.bookCatalog.get(i))
                print(f"Added to shopping cart {self.bookCatalog.get(i)}")

    def addBookByPrefix(self, s : str) :
        '''
        addBookByPrefix: Inserts into the shopping cart the book with prefix s
        input: 
            s: Prefix    
        '''
        # Validating the index. Otherwise it  crashes
        if s == "":
            print("Invalid prefix. Try again.")
        else:
            i = self.indexSortedTitle.find(s)
            if i!=None:
                self.shoppingCart.push(self.bookCatalog.get(i))
                print(f"Added to shopping cart {self.bookCatalog.get(i)}")


    def pathLength(self, s1: str, s2: str) :
        i = self.indexKey.find(s1)
        j = self.indexKey.find(s2)
        distance = self.similaGraph.distance(i, j)
        print(f"{s1} and {s2} are at distance {distance}")
        return distance

    def searchBookByInfix(self, infix : str) -> int:
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string 
        returns: 
            the number of books that contains infix in its title   
        '''
        heap = BinaryHeap.BinaryHeap()
        numberOfBooks = 0
        for book in self.bookCatalog:
            if infix in book.title:
                numberOfBooks+=1
                heap.add(book)
        while heap:
            book = heap.remove()
            index = self.indexKey.find(book.key)
            l = self.similaGraph.out_edges(index)
            print(f"{book}")
            for i in range(len(l)):
                print(f"\t\tSimilar: {self.bookCatalog.get(l[i]).title}")
        return numberOfBooks

    def sortUsingMergeSort(self) :
        algorithms.merge_sort(self.bookSortedCatalog)

    def sortUsingQuickSort(self) :
        algorithms.quick_sort(self.bookSortedCatalog)

    def searchBookUsingBinarySearch(self, prefix : str) :
        s = SortableBook.SortableBook(0, prefix, "", 0, None)
        j = algorithms.binary_search(self.bookSortedCatalog, self.bookSortedCatalog.size(), s)
        print(self.bookSortedCatalog[j])

    def removeFromShoppingCart(self) :
        '''
        removeFromShoppingCart: remove one book from the shopping cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.pop()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")
            return u
'''
b = BookStore()
b.loadCatalog("booktest.txt")
b.searchBookByInfix("The Art of Machine Piecing")
b.searchBookByInfix("The Best of Howard Jones")
print(b.pathLength("0807842591", "1557509646"))
print(b.pathLength("B00005M2DR", "B00005M2DZ"))
'''