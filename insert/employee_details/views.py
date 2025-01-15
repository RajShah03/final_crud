from django.shortcuts import render, redirect
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["employee_db"]
collection = db["employees"]

# Insert View
def insert_employee(request):
    if request.method == "POST":
        data = {
            "id": request.POST["id"],
            "name": request.POST["name"],
            "age": int(request.POST["age"]),
            "salary": float(request.POST["salary"])
        }
        collection.insert_one(data)
        return redirect("/")
    return render(request, "insert.html")

