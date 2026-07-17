class Overloadingdemo:
    def show_details(self,*args):
        if len(args)==1:
            print(f"Car brand: {args[0]}")
        elif len(args)==2:
            print(f"Car brand: {args[0]}, Model: {args[1]}")
        else:
            print("Invalid number of arguments")

def Overloading_demo():
    demo=Overloadingdemo()
    demo.show_details("Toyota")
    demo.show_details("Honda", "Civic")