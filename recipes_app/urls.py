from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, RecipeViewSet, create_recipe, RecipeByCategoryView

# Создаем роутер и регистрируем наши viewsets
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'recipes', RecipeViewSet)

# Определяем пути
urlpatterns = [
    path('', include(router.urls)),
    path('create-recipe/', create_recipe, name='create_recipe'),  # путь для создания рецепта
    path('categories/<int:category_id>/recipes/', RecipeByCategoryView.as_view(), name='category_recipes'),  # рецепты по категориям
    path('recipes/<int:pk>/', RecipeViewSet.as_view({'get': 'retrieve'}), name='recipe_detail'),  # детальная информация о рецепте
]
