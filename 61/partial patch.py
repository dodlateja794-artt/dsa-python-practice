@api_view(["PATCH"])
def student_partial_update(request, pk):
    student=get_object_404(Student,id=pk)
    serilizer=Studentserializer(student,data=request.data,partial=True)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data,status=200)
    else:
        return Response(serilizer.errors,status=400)