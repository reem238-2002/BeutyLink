import os
import django
import random

# Set up Django environment
import sys
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BeutyLink.settings')
django.setup()

from accounts.models import Salon, Service, Review

def populate():
    # 1. Clear existing data
    print("Cleaning up existing data...")
    Review.objects.all().delete()
    Salon.objects.all().delete()
    Service.objects.all().delete()

    # 2. Create Services
    services_list = [
        ("مكياج سهرة", "palette"),
        ("تسريحة شعر", "scissors"),
        ("تنظيف بشرة", "sparkles"),
        ("بديكير ومنيكير", "hand"),
        ("مكياج عرائس", "heart"),
        ("صبغة شعر", "brush"),
        ("حمام مغربي", "bath"),
        ("مساج", "wind"),
    ]
    
    service_objs = []
    for name, icon in services_list:
        service_objs.append(Service.objects.create(name=name, icon=icon))

    # 3. Create Salons
    locations = [
        "حدة", "شارع الستين", "التحرير", "شارع بغداد", "حي الجزائر", 
        "شارع الزبيري", "الصافية", "الروضة", "بيت بوس", "شارع الدائري"
    ]
    
    names = [
        "صالون رويال كوين", "مركز لومينوس للتجميل", "بيوتي تاتش", "صالون ميس كاترين",
        "جلامور زون", "مركز النخبة للتجميل", "سيلك آند ستون", "صالون ستايلش", 
        "الأميرة الصغيرة", "مركز الياقوت"
    ]

    assets_logos = ["logos/logo_1.png"]
    assets_bgs = ["salons/bg_1.png", "salons/bg_2.png", "salons/bg_3.png"]

    comments = [
        "خدمة رائعة جداً، والتعامل راقي!",
        "أفضل مكان للمكياج في صنعاء الصراحة.",
        "الأسعار مناسبة جداً مقارنة بالجودة.",
        "التزام بالمواعيد ونظافة تامة.",
        "شغلهم احترافي والنتائج مذهلة.",
        "أنصح الجميع بتجربة حمامهم المغربي.",
        "المكان هادئ ومريح جداً.",
        "أفضل مركز لتجهيز العرائس.",
    ]

    print("Creating 10 salons...")
    for i in range(10):
        price_range = random.choice([1, 2, 3])
        rating = round(random.uniform(4.0, 5.0), 1)
        
        salon = Salon.objects.create(
            name=names[i],
            description=f"يقدم {names[i]} أرقى خدمات التجميل والعناية بالبشرة في منطقة {locations[i]}. نحن نلتزم بأعلى معايير الجودة والاحترافية لضمان إطلالة ساحرة لكل عميلة.",
            image=random.choice(assets_bgs),
            logo=assets_logos[0],
            rating=rating,
            location="صنعاء",
            area=locations[i],
            price_range=price_range,
            is_active=True
        )
        
        # Add random services
        random_services = random.sample(service_objs, k=random.randint(3, 5))
        salon.services.set(random_services)
        
        # Add a review
        Review.objects.create(
            salon=salon,
            user_name=random.choice(["سارة", "فاطمة", "ليلى", "أماني", "ريم"]),
            comment=random.choice(comments),
            rating=int(rating)
        )

    print("Population complete!")

if __name__ == "__main__":
    populate()
