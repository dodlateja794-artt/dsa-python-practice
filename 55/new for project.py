@api_view(["POST"])
def student_create(request):
    serializer=studentserilizer(data=request.data)
    if serializer is_valid:
        serializer.save()
        return response(serializer.data)
    return response(serializer.errors)
