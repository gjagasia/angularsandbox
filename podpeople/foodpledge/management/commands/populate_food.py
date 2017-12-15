from django.core.management.base import BaseCommand
import random
from foodpledge.models import Food

class Command(BaseCommand):
    help = 'Make some sandwiches'

    def handle(self, *args, **options):
        Food.objects.get_or_create(food_type='sandwich', food_name='Bacon Sandwich', food_picture='http://assets.kraftfoods.com/recipe_images/opendeploy/108091_MXM_K2526V18EC_OR1_OH_640x428.jpg', rating=random.randint(0,100))
        Food.objects.get_or_create(food_type='sandwich', food_name='Bacon, Egg and Cheese', food_picture='http://food.fnr.sndimg.com/content/dam/images/food/fullset/2013/2/14/0/FNK_Maple-Bacon-Grilled-Cheese_s4x3.jpg.rend.hgtvcom.616.462.suffix/1382542424660.jpeg', rating=random.randint(0,100))
        Food.objects.get_or_create(food_type='sandwich', food_name='Bagel Toast', food_picture='https://thomasbreads.com/files/images/recipe/pinterest/Rich_Pin_Frnch_Toast_0.jpg', rating=random.randint(0,100))
        Food.objects.get_or_create(food_type='sandwich', food_name='Baked Bean', food_picture='https://newengland.com/wp-content/uploads/2015/04/new-england-baked-bean-sandwich-720x439.jpg', rating=random.randint(0,100))
        Food.objects.get_or_create(food_type='sandwich', food_name='Banh mi', food_picture='http://cdn-image.myrecipes.com/sites/default/files/styles/4_3_horizontal_-_1200x900/public/image/recipes/ck/08/09/bahn-mi-ck-1835268-x.jpg?itok=Ht0X3KHs', rating=random.randint(0,100))
        # Food.objects.get_or_create(food_type='sandwich', name='Barbeque')
        # Food.objects.get_or_create(food_type='sandwich', name='Chicken Salad')
        # Food.objects.get_or_create(food_type='sandwich', name='Chili Burger')
        # Food.objects.get_or_create(food_type='sandwich', name='Chipped Beef')
        # Food.objects.get_or_create(food_type='sandwich', name='Dagwood')
        # Food.objects.get_or_create(food_type='sandwich', name='Denver')
        # Food.objects.get_or_create(food_type='sandwich', name='Jucy Lucy')
        # Food.objects.get_or_create(food_type='sandwich', name='Katsu')

        Food.objects.get_or_create(food_type='pie', food_name='Bakewell Tart', food_picture='https://ichef.bbci.co.uk/food/ic/food_16x9_448/recipes/marys_bakewell_tart_12584_16x9.jpg', rating=random.randint(0,100))
        Food.objects.get_or_create(food_type='pie', food_name='Black Bun', food_picture='http://cdnwp.audiencemedia.com/wp-content/uploads/2014/10/322212-1-eng-GB_scottish-black-bun-470x540.jpg', rating=random.randint(0,100))
        Food.objects.get_or_create(food_type='pie', food_name='Boysenberry', food_picture='http://www.simplyrecipes.com/wp-content/uploads/2008/06/boysenberry-pie-a.jpg', rating=random.randint(0,100))
        Food.objects.get_or_create(food_type='pie', food_name='Cookie Cake Pie', food_picture='http://www.seriouseats.com/recipes/assets_c/2011/10/20111005-173863-cookie-cake-pie-primary-thumb-625xauto-194166.jpg', rating=random.randint(0,100))
        Food.objects.get_or_create(food_type='pie', food_name='Coulibiac', food_picture='https://www.bbcgoodfood.com/sites/default/files/user-collections/my-colelction-image/2015/12/recipe-image-legacy-id--424506_11.jpg', rating=random.randint(0,100))
        # Food.objects.get_or_create(food_type='pie', name='Kuchen')
        # Food.objects.get_or_create(food_type='pie', name='Manchester Tart')
        # Food.objects.get_or_create(food_type='pie', name='Meat and Potato Pie')
        # Food.objects.get_or_create(food_type='pie', name='Pasty')
        # Food.objects.get_or_create(food_type='pie', name='Pecan Pie')
        # Food.objects.get_or_create(food_type='pie', name='Soparnik')
        # Food.objects.get_or_create(food_type='pie', name='Vlaai')
