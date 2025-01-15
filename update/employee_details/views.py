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

# Update View
def update_employee(request, id):
    employee = collection.find_one({"id": id})
    if request.method == "POST":
        updated_data = {
            "name": request.POST["name"],
            "age": int(request.POST["age"]),
            "salary": float(request.POST["salary"])
        }
        collection.update_one({"id": id}, {"$set": updated_data})
        return redirect("/")
    return render(request, "update.html", {"employee": employee})

# Delete View
def delete_employee(request, id):
    employee = collection.find_one({"id": id})
    if request.method == "POST":
        collection.delete_one({"id": id})
        return redirect("/")
    return render(request, "delete.html", {"employee": employee})
