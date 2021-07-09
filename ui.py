import requests
import tkinter as tk
import webbrowser
from py_edamam import PyEdamam
from io import BytesIO
from PIL import Image, ImageTk
from playsound import playsound
from utils import get_json, parse_json, convert_string_to_list

BUTTON_CLICK_SOUND = "../clicks.m4a"
WINDOW_TITLE = "Recipe App"
RECIPE_IMAGE_WIDTH = 350
RECIPE_IMAGE_HEIGHT = 300


class RecipeApp(object):
    dish_name_label = 'Dish Name:'
    missing_ingredient_label = 'Missing Ingredients: '
    name = ''
    image = ''
    all_good = False

    def __init__(self, recipe_app_key):
        self.recipe_app_key = recipe_app_key
        # self.name = name
        # self.image = image
        # self.missing_ingredients = missing_ingredients
        self.window = tk.Tk()

        # Auto resize geometry
        self.window.geometry("")
        self.window.configure(bg="#9ddfd3")
        self.window.title(WINDOW_TITLE)

        self.search_label = tk.Label(self.window, text="Search Recipe", bg="#ea86b6")
        self.search_label.grid(column=0, row=0, padx=5)

        self.search_entry = tk.Entry(master=self.window, width=40)
        self.search_entry.grid(column=1, row=0, padx=5, pady=10)

        self.search_button = tk.Button(self.window, text="search", highlightbackground="#ea86b6",
                                       command=self.__run_search_query)
        self.search_button.grid(column=2, row=0, padx=5)

    def __run_search_query(self):

        # playsound(BUTTON_CLICK_SOUND)
        query = self.search_entry.get()
        self.get_query(query)
        #recipe = self.__get_recipe(query)

        # Recipe
        if self.all_good is True:
            recipe_image = self.image
            # recipe_url = recipe.url
            # print("From run_search_query\n" + recipe)
            # print("From run_search_query\n" + recipe.ingredient_names)

        else:
            # Recipe not found
            self.all_good = False
            print("IN THE UI IMAGE IS NULL")
            recipe_image = "https://www.mageworx.com/blog/wp-content/uploads/2012/06/Page-Not-Found-13.jpg"

        self.__show_image(recipe_image)
        self.__get_ingredients(self.missing_ingredients)

        def __open_link():
            pass
            # playsound(BUTTON_CLICK_SOUND)
            # webbrowser.open(recipe_url)

        self.recipe_button = tk.Button(self.window, text="recipe link", highlightbackground="#ea86b6",
                                       command=__open_link)
        self.recipe_button.grid(column=1, row=7, pady=10)

    # def __get_recipe(self, query):
    #     query_result = edamam_object.search_recipe(query)
    #
    #     # Get first recipe in list
    #     for recipe in query_result:
    #         print(recipe)
    #         return recipe

    def __show_image(self, image_url):
        response = requests.get(image_url)

        img = Image.open(BytesIO(response.content))
        img = img.resize((RECIPE_IMAGE_WIDTH, RECIPE_IMAGE_HEIGHT))
        image = ImageTk.PhotoImage(img)

        holder = tk.Label(self.window, image=image)
        holder.photo = image
        holder.grid(column=1, row=6, pady=10)

    def __get_ingredients(self, missing_ingredients):
        ingredients = tk.Text(master=self.window, height=15, width=50, bg="#ffdada")
        ingredients.grid(column=1, row=4, pady=10)
        ingredients.delete("1.0", tk.END)

        if missing_ingredients is None:
            ingredients.insert(tk.END, "No Recipe found for search criteria")
            return

        ingredients.insert(tk.END, "\n"+self.dish_name_label+" " + self.name + "\n\n")
        ingredients.insert(tk.END, self.missing_ingredient_label, "\n")
        for ingredient in missing_ingredients:
            ingredients.insert(tk.END, "\n- " + ingredient)

    def run_app(self):
        self.window.mainloop()
        return

    def get_query(self, query):
        response = get_json(query)
        print(response)
        recipe_list = parse_json(response)
        if response:
            self.all_good = True
            for item in recipe_list:

                self.name = item.name
                self.image = item.image
                self.missing_ingredients = item.missing_ingredients
