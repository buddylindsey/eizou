from os import listdir
from os.path import isfile, join

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    ListView,
    TemplateView,
)

from .forms import ImageUploadForm
from .models import Image


class ImageListView(ListView):
    model = Image
    template_name = "images/list.html"
    context_object_name = "images"
    paginate_by = 20


class UploadImageView(CreateView):
    model = Image
    form_class = ImageUploadForm
    template_name = "images/upload.html"


class ImageDetailView(DetailView):
    model = Image
    template_name = "images/detail.html"
    context_object_name = "image"


class ImageDeleteView(DeleteView):
    model = Image
    success_url = reverse_lazy("list_images")
