import random
from datetime import datetime

from colorama import Fore, Style, init

init()


USERS = {
    "user1": {
        "registration_date": datetime(2022, 1, 15), 
        "last_purchase": datetime(2023, 10, 5),
        "last_login": datetime(2023, 10, 7),
        "total_spent": 45000,
        "offer_usage": 12,
        "redemption_rate": 0.85,
        "purchase_history": ["игры", "подписки", "электронные книги"],
        "cart": ["ключ к игре CyberSphere 2077"],
        "views": ["онлайн-кинотеатр", "музыка"],

    },
    "user2": {
        "registration_date": datetime(2023, 5, 20),
        "last_purchase": datetime(2023, 9, 28),
        "last_login": datetime(2023, 10, 1),
        "total_spent": 8000,
        "offer_usage": 3,
        
        "redemption_rate": 0.65,
        "purchase_history": ["подписки на музыку"],
        "cart": ["подписка Spotify"],
        "views": ["подписки на музыку"],
    },
    "user3": {
        "registration_date": datetime(2021, 11, 1),
        "last_purchase": datetime(2023, 9, 15),
        "last_login": datetime(2023, 10, 3),
        "total_spent": 120000,
        "offer_usage": 25,
        "redemption_rate": 0.92,
        "purchase_history": ["игры", "игры", "подписки"],
        "cart": ["игровая подписка Xbox Game Pass"],
        "views": ["игры", "игры"],
    },
    "user4": {
        "registration_date": datetime(2023, 8, 10),
        "last_purchase": datetime(2023, 9, 5),
        "last_login": datetime(2023, 9, 20),
        "total_spent": 2500,
        "offer_usage": 1,
        "redemption_rate": 0.4,
        "purchase_history": ["электронные книги"],
        "cart": [],
        "views": ["электронные книги", "электронные книги"],
    },
    "user5": {
        "registration_date": datetime(2022, 6, 30),
        "last_purchase": datetime(2023, 8, 12),
        "last_login": datetime(2023, 9, 28),
        "total_spent": 32000,
        "offer_usage": 8,
        "redemption_rate": 0.75,
        "purchase_history": ["онлайн-кинотеатры", "подписки на музыку"],
        "cart": ["подписка Okko"],
        "views": ["онлайн-кинотеатры"],
    },
}

PRODUCTS = {
    "ключ к игре CyberSphere 2077": {
        "category": "игры",
        "base_price": 1500,
        "competitors": {"Steam": 1480, "G2A": 1450},
        "new_releases": 5,
    },
    "подписка Spotify": {
        "category": "подписки на музыку",
        "base_price": 599,
        "competitors": {"Apple Music": 649, "Ozon": 599},
        "new_releases": 2,
    },
    "подписка Okko": {
        "category": "онлайн-кинотеатры",
        "base_price": 499,
        "competitors": {"PREMIER": 549, "Иви": 499},
        "new_releases": 3,
    },
    "игровая подписка Xbox Game Pass": {
        "category": "игры",
        "base_price": 1999,
        "competitors": {"PS Plus": 2200, "Nintendo Switch Online": 1800},
        "new_releases": 10,
    },
    "электронная книга 'Цифровая магия'": {
        "category": "электронные книги",
        "base_price": 499,
        "competitors": {"LitRes": 450, "Storytel": 499},
        "new_releases": 1,
    },
}

TRENDS = {
    "игры": {"CyberSphere 2077": 0.7, "новый DLC для популярной игры": 0.9},
    "онлайн-кинотеатры": {"новый сериал 'Тенденции'": 0.9, "новый фильм Marvel": 0.8},
    "подписки на музыку": {"новый альбом BTS": 0.6, "альбом Taylor Swift": 0.85},
    "электронные книги": {
        "книга 'Цифровая магия'": 0.4,
        "новый хит 'AI Revolution'": 0.7,
    },
}


class WildPrice:
    def __init__(self):
        self.users = USERS
        self.products = PRODUCTS
        self.trends = TRENDS

    def calculate_kd(self, user_id, verbose=False):
        """Рассчитывает коэффициент доверия с подробным выводом"""



        user = self.users[user_id]
     
        days_since_last = (datetime.now() - user["last_purchase"]).days

   
        base_kd = (user["total_spent"] / 1000) * user["redemption_rate"] * 0.1
        time_factor = max(0, 30 - days_since_last) * 0.02
        offer_factor = user["offer_usage"] * 0.05
        kd = base_kd + time_factor + offer_factor
        kd = min(1.0, max(0.1, kd))

        if verbose:
            log = f"\n{Style.BRIGHT}{Fore.GREEN}=== Расчет Kd для {user_id} ==={Style.RESET_ALL}\n"
            log += f"{Fore.BLUE}Базовый коэффициент: {base_kd:.2f}{Style.RESET_ALL} (от суммы покупок {user['total_spent']} руб и выкупа {user['redemption_rate'] * 100}%)\n"
            log += f"{Fore.BLUE}Фактор времени последней покупки: {time_factor:.2f}{Style.RESET_ALL} (последняя покупка {days_since_last} дней назад)\n"
            log += f"{Fore.BLUE}Фактор использования предложений: {offer_factor:.2f}{Style.RESET_ALL} ({user['offer_usage']} использований предложений)\n"
            log += f"{Fore.CYAN}Итоговый Kd: {kd:.2f}{Style.RESET_ALL}\n"
            return round(kd, 2), log
        return round(kd, 2)

    def detect_salary_day(self, user_id, verbose=False):
        """Предсказывает день зарплаты с логами"""
  
        salary_days = [5, 20]  
        day = random.choice(salary_days)

        if verbose:
            log = f"\n{Style.BRIGHT}{Fore.GREEN}=== Анализ дня зарплаты для {user_id} ==={Style.RESET_ALL}\n"
            log += f"{Fore.MAGENTA}На основе шаблонов поведения предположили, что зарплата выплачивается {day} числа{Style.RESET_ALL}\n"
            return day, log
        return day

    def analyze_interests(self, user_id, verbose=False):
        """Анализирует интересы пользователя с детализацией"""
        user = self.users[user_id]
        interest_score = {}

        for item in user["purchase_history"]:
            interest_score[item] = interest_score.get(item, 0) + 0.4

        for item in user["views"]:
            interest_score[item] = interest_score.get(item, 0) + 0.3

        for item in user["cart"]:
            interest_score[item] = interest_score.get(item, 0) + 0.5

        if verbose:
            log = f"\n{Style.BRIGHT}{Fore.GREEN}=== Анализ интересов для {user_id} ==={Style.RESET_ALL}\n"
            for category, score in interest_score.items():
                log += f"{Fore.YELLOW}{category}:{Style.RESET_ALL} {score:.2f} баллов (учитывались: {user['purchase_history'].count(category)} покупок, {user['views'].count(category)} просмотров, {user['cart'].count(category)} в корзине)\n"
            return {k: round(v, 2) for k, v in interest_score.items()}, log
        return {k: round(v, 2) for k, v in interest_score.items()}

    def calculate_kk(self, product_name, verbose=False):
        """Рассчитывает коэффициент конкуренции с логами"""
        product = self.products[product_name]
        base_price = product["base_price"]
        competitors = product["competitors"]

        avg_competitor = sum(competitors.values()) / len(competitors)
        new_releases_factor = 1 - product["new_releases"] / 10
        kk = (base_price / avg_competitor) * new_releases_factor

        if verbose:
            log = f"\n{Style.BRIGHT}{Fore.GREEN}=== Расчет KK для {product_name} ==={Style.RESET_ALL}\n"
            log += f"{Fore.BLUE}Средняя цена конкурентов: {avg_competitor:.2f} руб{Style.RESET_ALL}\n"
            log += f"{Fore.BLUE}Количество новых аналогов: {product['new_releases']} → фактор {new_releases_factor:.2f}{Style.RESET_ALL}\n"
            log += f"{Fore.CYAN}Итоговой коэффициент конкуренции KK: {kk:.2f}{Style.RESET_ALL}\n"
            return round(kk, 2), log
        return round(kk, 2)

    def calculate_ks(self, product_name, verbose=False):
        """Рассчитывает коэффициент спроса с детализацией"""
        product = self.products[product_name]
        category = product["category"]

        if category in self.trends:
            max_trend = max(self.trends[category].values())
            if verbose:
                log = f"\n{Style.BRIGHT}{Fore.GREEN}=== Расчет KS для {product_name} ==={Style.RESET_ALL}\n"
                log += f"{Fore.BLUE}Категория: {category}{Style.RESET_ALL}\n"
                log += f"{Fore.CYAN}Максимальный тренд в категории: {max_trend:.2f}{Style.RESET_ALL}\n"
                return max_trend, log
            return max_trend
        if verbose:
            return (
                0.5,
                f"{Fore.RED}Нет данных о трендах для этой категории{Style.RESET_ALL}",
            )
        return 0.5

    def dynamic_pricing(self, user_id, product_name, verbose=False):
        """Динамическое ценообразование с пошаговым выводом"""
        kd = self.calculate_kd(user_id)
        product = self.products[product_name]
        category = product["category"]
        interest = self.analyze_interests(user_id).get(category, 0)

        base_price = product["base_price"]
        final_price = base_price

        if interest > 0.6:
            price_factor = 1.15
            final_price *= price_factor
        elif interest < 0.3:
            price_factor = 0.85
            final_price *= price_factor
        else:
            price_factor = 1.0

        if kd > 0.7:
            kd_factor = 1.05
            final_price *= kd_factor
        else:
            kd_factor = 1.0

        if verbose:
            log = f"\n{Style.BRIGHT}{Fore.GREEN}=== Динамическое ценообразование для {product_name} ==={Style.RESET_ALL}\n"
            log += f"{Fore.BLUE}Базовая цена: {base_price} руб{Style.RESET_ALL}\n"
            log += f"{Fore.BLUE}Интерес пользователя к категории '{category}': {interest:.2f}{Style.RESET_ALL}\n"

            if interest > 0.6:
                log += f"{Fore.MAGENTA}Высокий интерес → повышение цены на {price_factor * 100 - 100:.1f}%{Style.RESET_ALL}\n"
            elif interest < 0.3:
                log += f"{Fore.MAGENTA}Низкий интерес → скидка {-(1 - price_factor) * 100:.1f}%{Style.RESET_ALL}\n"
            else:
                log += f"{Fore.MAGENTA}Средний интерес → цена без изменений{Style.RESET_ALL}\n"

            if kd > 0.7:
                log += f"{Fore.MAGENTA}Высокий Kd ({kd}) → дополнительное повышение цены на {kd_factor * 100 - 100:.1f}%{Style.RESET_ALL}\n"
            else:
                log += f"{Fore.MAGENTA}Kd ({kd}) ниже порога → без дополнительных изменений{Style.RESET_ALL}\n"

            log += f"{Fore.CYAN}Итоговая цена: {round(final_price, 2)} руб{Style.RESET_ALL}\n"
            return round(final_price, 2), log
        return round(final_price, 2)

    def recommend_products(self, user_id, verbose=False):
        """Рекомендует товары на основе корзины с логами"""
        user = self.users[user_id]
        recommendations = []

        if any("PS" in item for item in user["cart"]):
            recommendations.append("игры для PS5")

        if any("подписка" in item for item in user["cart"]):
            recommendations.append("подарочные карты")

        if verbose:
            log = f"\n{Style.BRIGHT}{Fore.GREEN}=== Рекомендации для {user_id} ==={Style.RESET_ALL}\n"
            if recommendations:
                log += f"{Fore.BLUE}На основе содержимого корзины:{Style.RESET_ALL}\n"
                for rec in recommendations:
                    log += f"{Fore.YELLOW}- {rec}{Style.RESET_ALL}\n"
            else:
                log += (
                    f"{Fore.RED}Не найдено персональных рекомендаций{Style.RESET_ALL}\n"
                )
            return recommendations, log
        return recommendations


def main():
    wp = WildPrice()

    print(f"{Style.BRIGHT}{Fore.CYAN}=== WildPrice Demo ==={Style.RESET_ALL}")
    print(f"\n{Style.BRIGHT}{Fore.YELLOW}Доступные пользователи:{Style.RESET_ALL}")
    for user in wp.users:
        print(f"{Fore.GREEN}- {user}{Style.RESET_ALL}")

    user_id = input(
        f"\n{Style.BRIGHT}{Fore.CYAN}Введите ID пользователя: {Style.RESET_ALL}"
    )

    if user_id not in wp.users:
        print(f"{Fore.RED}Пользователь не найден!{Style.RESET_ALL}")
        return

    verbose_input = input(
        f"{Style.BRIGHT}{Fore.CYAN}Включить подробный вывод логов? (да/нет): {Style.RESET_ALL}"
    ).lower()
    verbose = verbose_input == "да"

    print(f"\n{Style.BRIGHT}{Fore.MAGENTA}=== Анализ пользователя ==={Style.RESET_ALL}")
    kd, kd_log = wp.calculate_kd(user_id, verbose)
    print(f"{Fore.BLUE}Коэффициент доверия Kd: {kd}{Style.RESET_ALL}")
    if verbose:
        print(kd_log)

    salary_day, salary_log = wp.detect_salary_day(user_id, verbose)
    print(
        f"{Fore.BLUE}Предполагаемый день зарплаты: {salary_day} число{Style.RESET_ALL}"
    )
    if verbose:
        print(salary_log)

    interest, interest_log = wp.analyze_interests(user_id, verbose)
    print(f"\n{Fore.BLUE}Интересы пользователя:{Style.RESET_ALL}")
    if verbose:
        print(interest_log)
    else:
        for category, score in interest.items():
            print(f"{Fore.YELLOW}- {category}: {score}{Style.RESET_ALL}")

    print(f"\n{Style.BRIGHT}{Fore.MAGENTA}=== Анализ товаров ==={Style.RESET_ALL}")
    print(f"{Style.BRIGHT}{Fore.YELLOW}Доступные товары:{Style.RESET_ALL}")
    for product in wp.products:
        print(f"{Fore.GREEN}- {product}{Style.RESET_ALL}")

    product_name = input(
        f"\n{Style.BRIGHT}{Fore.CYAN}Введите название товара для анализа: {Style.RESET_ALL}"
    )

    if product_name not in wp.products:
        print(f"{Fore.RED}Товар не найден!{Style.RESET_ALL}")
        return

    kk, kk_log = wp.calculate_kk(product_name, verbose)
    print(f"\n{Fore.BLUE}Коэффициент конкуренции KK: {kk}{Style.RESET_ALL}")
    if verbose:
        print(kk_log)

    ks, ks_log = wp.calculate_ks(product_name, verbose)
    print(f"{Fore.BLUE}Коэффициент спроса KS: {ks}{Style.RESET_ALL}")
    if verbose:
        print(ks_log)

    price, price_log = wp.dynamic_pricing(user_id, product_name, verbose)
    print(
        f"{Fore.CYAN}Рекомендуемая цена для пользователя: {price} руб.{Style.RESET_ALL}"
    )
    if verbose:
        print(price_log)

    recommendations, rec_log = wp.recommend_products(user_id, verbose)
    if verbose:
        print(rec_log)
    else:
        print(
            f"\n{Style.BRIGHT}{Fore.YELLOW}Персональные рекомендации:{Style.RESET_ALL}"
        )
        if recommendations:
            for rec in recommendations:
                print(f"{Fore.GREEN}- {rec}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Нет рекомендаций{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
