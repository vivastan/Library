from tkinter import *
from tkinter.messagebox import *
from datetime import *
from random import *

today = date.today()
todayday = str(today)[-2:]
todaymonth = str(today)[5:7]
todayyear = str(today)[:4]

deadline = timedelta(weeks = 3)
returnDate = today + deadline
returnDay = str(returnDate)[-2:]
returnMonth = str(returnDate)[5:7]
returnYear = str(returnDate)[:4]

cardExpires = timedelta(weeks = 4*52)
expiryDate = today + cardExpires
expiryMonth = str(expiryDate)[5:7] + '.'
expiryYear = str(expiryDate)[:4]

books = dict()
file = open('knjige_v3.txt', 'r')
L = file.read().split('\n')
for e in L:
    j = e.split('-')
    books[j[0]] = j[1]


class App(Frame):

    def __init__(self, tt):
        self.win = tt
        super().__init__(self.win)
        self.pack()
        self.Main()
        return

    def Main(self):
        self.win.title('Library - Main menu')
        self.b1 = Button(self, text = 'Borrow book', command = self.Borrow)
        self.b1.pack(fill = X)
        self.b2 = Button(self, text = 'Get membership', command = self.Membership)
        self.b2.pack(fill = X)
        self.b3 = Button(self, text = 'General information', command = self.Information)
        self.b3.pack(fill = X)
        self.b4 = Button(self, text = 'Search', command = self.Search)
        self.b4.pack(fill = X)
        return

    def Borrow(self):
        self.win.withdraw()
        try:
            self.top.destroy()
        except AttributeError:
            pass
        self.top = Toplevel()
        self.top.title('Borrow')
        self.b10 = Button(self.top, text = 'Back', command = self.Back)
        self.b10.pack()
        self.l16 = Label(self.top)
        self.l16.pack()
        self.l10 = Label(self.top, text = 'Recommendations...')
        self.l10.pack()
        a = 0
        for i in books:
            a += 1
            author = books[i].split(';')[0]
            if not a%5:
                self.b11 = Button(self.top, text = author+': '+str(i), command = self.Confirm)
                self.b11.pack()
        self.l15 = Label(self.top)
        self.l15.pack()
        self.l12 = Label(self.top, text = 'Cannot find the book you are looking for? Click on Search')
        self.l12.pack()
        self.b13 = Button(self.top, text = 'Search', command = self.Search)
        self.b13.pack()
        self.confirm = 0
        return

    def Confirm(self):
        result = askyesno('', 'Would you like to borrow this book?')
        if result:
            self.confirm += 1
            if self.confirm < 2:
                self.l11 = Label(self.top, text = 'Enter your ID card number')
                self.l11.pack()
                self.e11 = Entry(self.top)
                self.e11.pack()
                self.l12 = Label(self.top, text = 'Enter your ID card password')
                self.l12.pack()
                self.e12 = Entry(self.top)
                self.e12.pack()
                self.b12 = Button(self.top, text = 'Borrow', command = self.FinallyBorrow)
                self.b12.pack()
                self.b14 = Button(self.top, text = 'Quit', command = self.Borrow)
                self.b14.pack()
        return

    def FinallyBorrow(self):
        try:
            if len(self.e11.get()) == 0 or len(self.e12.get()) == 0:
                raise SyntaxError
            for b in self.e11.get():
                if ord(b) < 48 or ord(b) > 57:
                    raise TypeError
                elif len(self.e11.get()) != 6:
                    raise NameError
            for c in self.e12.get():
                if ord(c) < 48 or ord(c) > 57:
                    raise ValueError
                elif len(self.e12.get()) != 4:
                    raise AttributeError
        except SyntaxError:
            showerror('There has been an error.', 'Enter required data!')
        except TypeError:
            showerror('There has been an error.', 'ID card number can contain only numbers.')
        except NameError:
            showerror('There has been an error.', 'ID card number consists of 6 characters')
        except ValueError:
            showerror('There has been an error.', 'ID card password can contain only numbers.')
        except AttributeError:
            showerror('There has been an error.', 'ID card password consists of 4 characters')
        else:
            showinfo('', 'Book is borrowed until ' + returnDay + '.' + returnMonth + '.' + returnYear + '.')
            self.top.destroy()
            self.win.deiconify()
        return

    def Back(self):
        self.top.destroy()
        self.win.deiconify()
        return

    def Membership(self):
        self.win.withdraw()
        self.top = Toplevel()
        self.top.title('Get a membership')
        self.l21 = Label(self.top, text = 'First name:')
        self.l21.pack()
        self.e21 = Entry(self.top)
        self.e21.pack()
        self.l22 = Label(self.top, text = 'Last name:')
        self.l22.pack()
        self.e22 = Entry(self.top)
        self.e22.pack()
        self.l23 = Label(self.top, text = 'Date of birth:')
        self.l23.pack()
        self.e23 = Entry(self.top)
        self.e23.pack()
        self.b21 = Button(self.top,  text = 'Enter', command = self.Info)
        self.b21.pack()
        self.b22 = Button(self.top, text = 'Quit', command = self.Back)
        self.b22.pack()
        return

    def Info(self):
        try:
            for g in self.e21.get():
                if ord(g) < 65 or 90 < ord(g) < 97 or ord(g) > 122:
                    raise TypeError
            for h in self.e22.get():
                if ord(h) < 65 or 90 < ord(h) < 97 or ord(h) > 122:
                    raise TypeError
            dateOfBirth = self.e23.get()
            if dateOfBirth[2] != '.' or dateOfBirth[5] != '.':
                raise ValueError
            elif int(dateOfBirth[6:]) == returnYear:
                if int(dateOfBirth[2:4]) == int(str(today[5:7])):
                    if int(dateOfBirth[:1]) >= int(str(today[-2:])):
                       raise NameError
                elif int(dateOfBirth[2:4]) > int(str(today[5:7])):
                    raise NameError
            elif int(dateOfBirth[6:]) > int(str(today)[:4]):
                raise NameError
            else:
                a = int(dateOfBirth[:2])
                b = int(dateOfBirth[3:5])
                c = int(dateOfBirth[6:])
                if c > int(todayyear):
                    raise NameError
                elif b > 12:
                    raise NameError
                elif b == 2:
                    if a > 29:
                        raise NameError
                    elif a == 29:
                        if c%4 != 0:
                            raise NameError
                elif b in [1, 3, 5, 7, 8, 10, 12]:
                    if a > 31:
                        raise NameError
                elif b in [2, 4, 6, 9, 11]:
                    if a > 30:
                        raise NameError              
                if c == int(todayyear):
                    if b > int(todaymonth):
                        raise NameError
                    else:
                        if a > int(todayday):
                            raise NameError
        except TypeError:
            showerror('There has been an error.', 'Please enter correct first and last name (you can use only the English alphabet).')
        except ValueError:
            showerror('There has been an error.', 'Date of birth must be entered in format dd.mm.yyyy (01.01.2020)!')
        except NameError:
            showerror('There has been an error.', 'Enter valid date of birth!')
        except IndexError:
            showerror('There has been an error.', 'All fields have to be filled!')
        else:
            brisk = ''
            for n in range(6):
                brisk += str(randint(0,9))
            sifraisk = ''
            for m in range(4):
                sifraisk += str(randint(0,9))
            showinfo('You successfully got the membership, ' + self.e21.get().capitalize() + '!', 'Your ID card number: ' + brisk + '\nYour ID card password: ' + sifraisk + '\nYou use this information when borrowing books.\nYour ID card expires on ' + expiryMonth + expiryYear +'.')
            self.top.destroy()
            self.win.deiconify()
        return

    def Information(self):
        showinfo('', 'working hours: Mon-Fri   08-20\ndeadline for borrowing books: three weeks from the day they were borrowed;\nif you borrow a book today, the return deadline is ' + returnDay + returnMonth + returnYear)
        return

    def Search(self):
        self.win.withdraw()
        try:
            self.top.destroy()
        except AttributeError:
            pass
        self.top = Toplevel()
        self.top.title('Search')
        self.rbv = IntVar()
        self.r1 = Radiobutton(self.top, text = 'Search by title', variable = self.rbv, value = 1)
        self.r1.pack()
        self.r2 = Radiobutton(self.top, text = 'Search by author\'s last name', variable = self.rbv, value = 2)
        self.r2.pack()
        self.r3 = Radiobutton(self.top, text = 'Search by genre', variable = self.rbv, value = 3)
        self.r3.pack()
        self.b41 = Button(self.top, text = 'Next', command = self.Next)
        self.b41.pack()
        self.dalje = 0
        self.b46 = Button(self.top, text = 'Quit', command = self.Back)
        self.b46.pack()
        return

    def Next(self):
        try:
            if self.rbv.get() == 0:
                raise TypeError
            else:
                self.dalje += 1
                if self.dalje > 1:
                    raise NameError
        except TypeError:
            showerror('There has been an error.', 'Choose a field')
        except NameError:
            if self.rbv.get() == 1:
                self.l41.config(text = 'Enter first letter of title:')
            elif self.rbv.get() == 2:
                self.l41.config(text = 'Enter first letter of author\'s last name:')
            else:
                self.top.destroy()
                self.top = Toplevel()
                self.b52 = Button(self.top, text = 'Back to Main menu', command = self.Back)
                self.b52.pack()
                self.b51 = Button(self.top, text = 'Back to search', command = self.Search)
                self.b51.pack()
                self.rbv1 = IntVar()
                self.r4 = Radiobutton(self.top, text = 'fantasy', variable = self.rbv1, value = 1)
                self.r4.pack()
                self.r5 = Radiobutton(self.top, text = 'crime', variable = self.rbv1, value = 2)
                self.r5.pack()
                self.r6 = Radiobutton(self.top, text = 'school', variable = self.rbv1, value = 3)
                self.r6.pack()
                self.r7 = Radiobutton(self.top, text = 'romance', variable = self.rbv1, value = 4)
                self.r7.pack()
                self.b42 = Button(self.top, text = 'Find', command = self.Find)
                self.b42.pack()

        else:
            self.l41 = Label(self.top)
            self.l41.pack()
            if self.rbv.get() == 3:
                self.top.destroy()
                self.top = Toplevel()
                self.b52 = Button(self.top, text = 'Back to Main menu', command = self.Back)
                self.b52.pack()
                self.b51 = Button(self.top, text = 'Back to search', command = self.Search)
                self.b51.pack()
                self.rbv1 = IntVar()
                self.r4 = Radiobutton(self.top, text = 'fantasy', variable = self.rbv1, value = 1)
                self.r4.pack()
                self.r5 = Radiobutton(self.top, text = 'crime', variable = self.rbv1, value = 2)
                self.r5.pack()
                self.r6 = Radiobutton(self.top, text = 'school', variable = self.rbv1, value = 3)
                self.r6.pack()
                self.r7 = Radiobutton(self.top, text = 'romance', variable = self.rbv1, value = 4)
                self.r7.pack()
            else:
                if self.rbv.get() == 1:
                    self.l41.config(text = 'Enter first letter of title:')
                else:
                    self.l41.config(text = 'Enter first letter of author\'s last name:')
                self.e41 = Entry(self.top)
                self.e41.pack()
            self.b42 = Button(self.top, text = 'Find', command = self.Find)
            self.b42.pack()
        return

    def Find(self):
        if self.rbv.get() == 1:
            letter = self.e41.get()
            try:
                if len(letter) != 1:
                    raise TypeError
                elif ord(letter) < 65 or 90 < ord(letter) < 97 or ord(letter) > 122:
                    raise ValueError
            except TypeError:
                showerror('There has been an error.', 'You can only enter one letter.')
            except ValueError:
                showerror('There has been an error.', 'You can only enter letters.')
            else:
                self.top.destroy()
                self.top = Toplevel()
                self.top.title('books by title')
                self.b47 = Button(self.top, text = 'Back to Main menu', command = self.Back)
                self.b47.pack()
                self.b49 = Button(self.top, text = 'Back to Search', command = self.Search)
                self.b49.pack()
                self.l43 = Label(self.top)
                self.l43.pack()
                y = 0
                self.confirm = 0
                for k in books:
                    if k[0].upper() == letter.upper():
                        y += 1
                        author = books[k].split(';')[0]
                        self.b42 = Button(self.top, text = author+': '+str(k), command = self.Confirm)
                        self.b42.pack()
                if y == 0:
                    showinfo('', 'In the library database there does not exist a book starting with letter '+letter)
        elif self.rbv.get() == 2:
            letter = self.e41.get()
            try:
                if len(letter) != 1:
                    raise TypeError
                elif ord(letter) < 65 or 90 < ord(letter) < 97 or ord(letter) > 122:
                    raise ValueError
            except TypeError:
                showerror('There has been an error.', 'You can only enter one letter.')
            except ValueError:
                showerror('There has been an error.', 'You can only enter letters of the English alphabet.')
            else:
                self.top.destroy()
                self.top = Toplevel()
                self.top.title('books by author\'s last name')
                self.b48 = Button(self.top, text = 'Back to Main menu', command = self.Back)
                self.b48.pack()
                self.b50 = Button(self.top, text = 'Back to Search', command = self.Search)
                self.b50.pack()
                self.l44 = Label(self.top)
                self.l44.pack()
                z = 0
                self.confirm = 0
                for k in books:
                    prezime = books[k].split()
                    if prezime[1][0].upper() == letter.upper() or prezime[-1][0].upper() == letter.upper():
                        z += 1
                        author = books[k].split(';')[0]
                        self.b43 = Button(self.top, text = author+': '+str(k), command = self.Confirm)
                        self.b43.pack()
                if z == 0:
                    showinfo('', 'In the library database there does not exist a book whose author\'s last name starts with letter '+letter)
        else:
            try:
                if self.rbv1.get() == 0:
                    raise TypeError
            except TypeError:
                showerror('There has been an error.', 'You have to choose one field')
            else:
                self.top.destroy()
                self.top = Toplevel()
                self.top.title('books by genre')
                self.b45 = Button(self.top, text = 'Back to Main menu', command = self.Back)
                self.b45.pack()
                self.b50 = Button(self.top, text = 'Back to Search', command = self.Search)
                self.b50.pack()
                self.l42 = Label(self.top)
                self.l42.pack()
                self.confirm = 0
                for k in books:
                    genre = books[k].split(';')[-1].split(',')
                    author = books[k].split(';')[0]
                    if ('f' in genre and self.rbv1.get() == 1) or ('k' in genre and self.rbv1.get() == 2) or ('l' in genre and self.rbv1.get() == 3) or ('r' in genre and self.rbv1.get() == 4):
                        self.b44 = Button(self.top, text = author+': '+str(k), command = self.Confirm)
                        self.b44.pack()
        return
    
t = Tk()
app = App(t)
t.mainloop()
