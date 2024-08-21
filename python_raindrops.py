import pygame  # استيراد مكتبة Pygame لإنشاء الألعاب والمحاكاة
import random  # استيراد مكتبة random لتوليد أرقام عشوائية

# إعداد Pygame
pygame.init()  # تهيئة جميع وحدات Pygame
width, height = 800, 600  # تحديد عرض وارتفاع نافذة العرض
screen = pygame.display.set_mode((width, height))  # إنشاء نافذة العرض باستخدام العرض والارتفاع المحددين
clock = pygame.time.Clock()  # إعداد ساعة للتحكم في معدل الإطارات

# إعداد المطر
class RainDrop:  # تعريف كلاس يمثل قطرات المطر
    def __init__(self):
        # تحديد الموضع الأفقي العشوائي لقطرة المطر
        self.x = random.randint(0, width)
        # تحديد الموضع الرأسي العشوائي لقطرة المطر (خارج الشاشة قليلاً)
        self.y = random.randint(-20, height)
        # تحديد سرعة سقوط قطرة المطر بشكل عشوائي
        self.speed = random.randint(5, 15)
        # تحديد طول قطرة المطر بشكل عشوائي
        self.length = random.randint(5, 15)
    
    def fall(self):
        # جعل قطرة المطر تسقط للأسفل عن طريق زيادة الموضع الرأسي بناءً على السرعة
        self.y += self.speed
        # إعادة تعيين موقع قطرة المطر عند تجاوزها الحافة السفلية للشاشة
        if self.y > height:
            self.y = random.randint(-20, -1)  # إعادة ضبط الموضع الرأسي
            self.x = random.randint(0, width)  # إعادة ضبط الموضع الأفقي
            self.speed = random.randint(5, 15)  # إعادة ضبط السرعة
    
    def draw(self):
        # رسم قطرة المطر على الشاشة كخط مستقيم
        pygame.draw.line(screen, (0, 0, 255), (self.x, self.y), (self.x, self.y + self.length), 1)

# إنشاء قائمة تحتوي على 100 قطرة مطر
raindrops = [RainDrop() for _ in range(100)]

# الحلقة الرئيسية
running = True  # متغير للتحكم في استمرار تشغيل الحلقة
while running:
    screen.fill((0, 0, 0))  # ملء الشاشة باللون الأسود

    for drop in raindrops:  # التكرار على كل قطرة مطر في القائمة
        drop.fall()  # تحديث موضع القطرة بناءً على السقوط
        drop.draw()  # رسم القطرة على الشاشة
    
    pygame.display.flip()  # تحديث الشاشة لعرض التغييرات
    clock.tick(30)  # ضبط معدل الإطارات على 30 إطار في الثانية
    
    for event in pygame.event.get():  # التحقق من أحداث Pygame
        if event.type == pygame.QUIT:  # إذا تم الضغط على زر الخروج
            running = False  # إيقاف الحلقة

pygame.quit()  # إنهاء Pygame بعد إيقاف الحلقة
