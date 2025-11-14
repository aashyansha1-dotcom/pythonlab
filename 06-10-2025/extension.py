filename=input("Enter the filename: ");
if "." in filename:
   parts=filename.split(".")
   extension=parts[-1]
   print("The extension of the file is:",extension)
else:
    print("The extension of the file is extension")
