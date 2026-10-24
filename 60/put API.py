@api_view(["PUT"])
def student_update(request, pk):
    student=get_object_or_404(student,id=pk)
    Serializer=studentSerializer(student,data=request.data)
    if Serializer.is_valid():
        student.save()
        return Response(Serializer.data,status=201)
    else:
        return Response(Serializer.errors,status=400)

