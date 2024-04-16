from django.shortcuts import render
import openpyxl
from utils import EduDatabase


def StudentAdder(request):
    if request.method == "POST":
        if file := request.FILES.get("datafile"):
            workbook = openpyxl.open(file, data_only=True)
            sheet = workbook.active
            data = [list(row) for row in sheet.iter_rows(values_only=True)]
            basehandler = EduDatabase("edumatrics")
            basehandler.create_connection("navin82005", "navin82005")
            # basehandler.remove_all_students(data)
            basehandler.insert_new_students(data)
        return render(request, "studentform.html")

    return render(request, "studentform.html")
