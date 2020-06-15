from django.shortcuts import render
from django.views import View
from recipes.models import Recipe
from django.http import JsonResponse, HttpResponse
import json


class GetPatchRecipes(View):
    def get(self, request, pk):
        recipe = Recipe.objects.get(id=pk)
        recipe_dict = {
            'title': recipe.title,
            'description': recipe.description,
            'ingredients': recipe.ingredients,
            'favourite': recipe.favourite,
            'created': recipe.created,
            'updated': recipe.updated
        }
        return JsonResponse(recipe_dict)

    def patch(self, request, pk):
        if len(Recipe.objects.filter(id=pk)) == 1:
            recipe = Recipe.objects.get(id=pk)
            data = json.loads(request.body)
            if data['title'] != recipe.title:
                recipe.title = data['title']
            if data['description'] != recipe.description:
                recipe.description = data['description']
            if data['ingredients'] != recipe.ingredients:
                recipe.ingredients = data['ingredients']
            if data['favourite'] != recipe.favourite:
                recipe.favourite = data['favourite']
            recipe.save()
            return HttpResponse(recipe, status=200)
            """JsonResponse(recipe, safe=False)"""


class ListPostRecipes(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        recipes_dict_list = []
        for recipe in recipes:
            recipe_dict = {
                'title': recipe.title,
                'description': recipe.description,
                'ingredients': recipe.ingredients,
                'favourite': recipe.favourite,
                'created': recipe.created,
                'updated': recipe.updated
            }
            recipes_dict_list.append(recipe_dict)
        return JsonResponse(recipes_dict_list, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        new_recipe = Recipe(**data)
        new_recipe.save()
        recipe_dict = {
            'title': new_recipe.title,
            'description': new_recipe.description,
            'ingredients': new_recipe.ingredients,
            'favourite': new_recipe.favourite
        }
        return HttpResponse(content=json.dumps(recipe_dict), status=201)


class DeleteRecipes(View):
    def delete(self, request, pk):
        recipe = Recipe.objects.(id=pk)
        recipe.delete()
        return HttpResponse(status=200)
    