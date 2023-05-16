from django.shortcuts import render,redirect

from .models import list

from .form import TodoForm
# Create your views here.
def todo_home_view(request):
    obj = list.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
            
    context = {
        "object": obj,
        "form": form
    }
    return render(request, 'List.html', context)

def update_task_view(request, pk):
    obj = list.objects.get(id=pk)
    form = TodoForm(instance=obj)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, 'Update_task.html', context)


def delete_task_view(request, pk):
    obj = list.objects.get(id=pk)
    # form = TodoForm(instance=obj)
    if request.method == 'POST':
            obj.delete()
            return redirect("/")
    context = {
        # "form": form,
        "object":obj
    }
    return render(request, 'Delete_task.html', context)