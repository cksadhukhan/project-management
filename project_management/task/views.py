from rest_framework.response import Response
from rest_framework import status, generics
from .models import Task
from .serializers import TaskSerializer


class Tasks(generics.GenericAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get(self, request):
        tasks = Task.objects.all()
        total_tasks = tasks.count()

        serializer = self.serializer_class(tasks, many=True)
        
        return Response({
            "status": "success",
            "total": total_tasks,
            "data": {
                "tasks": serializer.data
            }
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"tasks": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_task(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        project = self.get_task(pk=pk)
        if project == None:
            return Response({"status": "fail", "message": f"Task with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(project)
        return Response({"status": "success", "data": {"task": serializer.data}})

    def patch(self, request, pk):
        task = self.get_task(pk)
        if task == None:
            return Response({"status": "fail", "message": f"Task with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"task": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_task(pk)
        if task == None:
            return Response({"status": "fail", "message": f"Task with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)