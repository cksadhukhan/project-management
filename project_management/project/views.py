from rest_framework.response import Response
from rest_framework import status, generics
from task.serializers import TaskSerializer

from task.models import Task
from .models import Project
from .serializers import ProjectSerializer


class Projects(generics.GenericAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get(self, request):
        projects = Project.objects.all()
        total_projects = projects.count()

        serializer = self.serializer_class(projects, many=True)
        
        return Response({
            "status": "success",
            "total": total_projects,
            "data": {
                "projects": serializer.data
            }
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"project": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(generics.GenericAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    task_serializer_class = TaskSerializer

    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except:
            return None
        
    def get_tasks(self, project):
        try:
            return Task.objects.filter(project = project)
        except:
            return None

    def get(self, request, pk):
        project = self.get_project(pk=pk)
        tasks = self.get_tasks(project=project)

        if project == None:
            return Response({"status": "fail", "message": f"Project with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(project)
        task_serializer = self.task_serializer_class(tasks, many=True)
        return Response({"status": "success", "data": {"project": serializer.data, 
                                                       "tasks": task_serializer.data
                                                       }})

    def patch(self, request, pk):
        project = self.get_project(pk)
        if project == None:
            return Response({"status": "fail", "message": f"Project with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"project": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_project(pk)
        if project == None:
            return Response({"status": "fail", "message": f"Project with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)