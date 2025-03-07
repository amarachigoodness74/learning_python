from datetime import datetime

def main():
  year = input("What year were you born? ")
  age = int(datetime.today().year) - int(year)
  print(f'You are {age} years old now')

if __name__ == "__main__":
  main()