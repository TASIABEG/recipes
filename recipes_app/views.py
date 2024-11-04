from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Category, Recipe
from .serializers import CategorySerializer, RecipeSerializer
from django.shortcuts import render, redirect
from .forms import RecipeForm

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    @action(detail=True, methods=['get'])
    def detail(self, request, pk=None):
        recipe = self.get_object()
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

class RecipeByCategoryView(APIView):
    def get(self, request, category_id):
        recipes = Recipe.objects.filter(category_id=category_id)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу или страницу списка рецептов
    else:
        form = RecipeForm()
    return render(request, 'create_recipe.html', {'form': form})
