def calculate_file_size(width, height, color_depth):
    """
    Calculates the file size in bytes.
    Formula: (width * height * color_depth) / 8
    """
    return width * height * color_depth / 8

def calculate_color_depth(file_size, width, height):
    """
    Calculates the color depth in bits per pixel.
    Formula: (file_size * 8) / (width * height)
    """
    if width * height == 0:
        raise ValueError("Width and height cannot be zero.")
    return (file_size * 8) / (width * height)

def calculate_width(file_size, height, color_depth):
    """
    Calculates the image width.
    Formula: width = (file_size * 8) / (height * color_depth)
    """
    if height * color_depth == 0:
        raise ValueError("Height and color depth cannot be zero.")
    return (file_size * 8) / (height * color_depth)

def calculate_height(file_size, width, color_depth):
    """
    Calculates the image height.
    Formula: height = (file_size * 8) / (width * color_depth)
    """
    if width * color_depth == 0:
        raise ValueError("Width and color depth cannot be zero.")
    return (file_size * 8) / (width * color_depth)

def calculate_total_pixels(width, height):
    """
    Calculates the total number of pixels.
    """
    return width * height

def get_float(prompt):
    """
    Prompts user for a floating-point number.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Пожалуйста, введите число.")

def main():
    language = True  # по умолчанию русский язык
    english_mode = False

    while True:
        if not english_mode:
            print("\nВыберите действие:")
            print("1. Расчет размера файла (байты, КБ, МБ) с известной шириной, высотой и цветовым глубоким")
            print("2. Расчет цветовой глубины (бит на пиксель) с известным размером файла, шириной и высотой")
            print("3. Расчет ширины изображения с известным размером файла, высотой и цветовым глубиной")
            print("4. Расчет высоты изображения с известным размером файла, шириной и цветовым глубиной")
            print("5. Расчет общего числа пикселей с известной шириной и высотой")
            print("6. Сменить язык на английский (да/нет)")
        else:
            print("\nSelect an option:")
            print("1. Calculate file size (bytes, KB, MB) with known width, height, and color depth")
            print("2. Calculate color depth (bits per pixel) with known file size, width, and height")
            print("3. Calculate image width with known file size, height, and color depth")
            print("4. Calculate image height with known file size, width, and color depth")
            print("5. Calculate total number of pixels with known width and height")
            print("6. Switch to Russian language (yes/no)")

        choice = input("Enter option number: ").strip()

        if not english_mode:
            if choice == "6":
                switch_language = input("Хотите сменить язык на английский? (да/нет): ")
                if switch_language.lower() == "да":
                    language = False
                    english_mode = True
                elif switch_language.lower() == "нет":
                    pass
                else:
                    print("Некорректный ответ.")
            else:
                if choice in ["1", "2", "3", "4", "5"]:
                    if not language:
                        print("\nВыберите действие:")
                        print("1. Расчет размера файла (байты, КБ, МБ) с известной шириной, высотой и цветовым глубоким")
                        print("2. Расчет цветовой глубины (бит на пиксель) с известным размером файла, шириной и высотой")
                        print("3. Расчет ширины изображения с известным размером файла, высотой и цветовым глубиной")
                        print("4. Расчет высоты изображения с известным размером файла, шириной и цветовым глубиной")
                        print("5. Расчет общего числа пикселей с известной шириной и высотой")

                    if choice == "1":
                        width = get_float("Введите ширину:")
                        height = get_float("Введите высоту:")
                        color_depth = get_float("Введите цветовую глубину:")
                        file_size = calculate_file_size(width, height, color_depth)
                        print(f"Расчет размера файла: {file_size:.2f} байт")
                    elif choice == "2":
                        file_size = get_float("Введите размер файла:")
                        width = get_float("Введите ширину:")
                        height = get_float("Введите высоту:")
                        color_depth = calculate_color_depth(file_size, width, height)
                        print(f"Расчет цветовой глубины: {color_depth:.2f} бит на пиксель")
                    elif choice == "3":
                        file_size = get_float("Введите размер файла:")
                        height = get_float("Введите высоту:")
                        color_depth = get_float("Введите цветовую глубину:")
                        width = calculate_width(file_size, height, color_depth)
                        print(f"Расчет ширины изображения: {width:.2f}")
                    elif choice == "4":
                        file_size = get_float("Введите размер файла:")
                        width = get_float("Введите ширину:")
                        color_depth = get_float("Введите цветовую глубину:")
                        height = calculate_height(file_size, width, color_depth)
                        print(f"Расчет высоты изображения: {height:.2f}")
                    elif choice == "5":
                        width = get_float("Введите ширину:")
                        height = get_float("Введите высоту:")
                        total_pixels = calculate_total_pixels(width, height)
                        print(f"Общее количество пикселей: {total_pixels:.0f}")

        else:
            if choice in ["1", "2", "3", "4", "5"]:
                if choice == "6":
                    switch_language = input("Do you want to switch to Russian language? (yes/no): ")
                    if switch_language.lower() == "yes":
                        language = True
                        english_mode = False
                    elif switch_language.lower() == "no":
                        pass
                    else:
                        print("Invalid answer.")
                else:
                    if choice == "1":
                        width = get_float("Enter width:")
                        height = get_float("Enter height:")
                        color_depth = get_float("Enter color depth:")
                        file_size = calculate_file_size(width, height, color_depth)
                        print(f"File size calculation: {file_size:.2f} bytes")
                    elif choice == "2":
                        file_size = get_float("Enter file size:")
                        width = get_float("Enter width:")
                        height = get_float("Enter height:")
                        color_depth = calculate_color_depth(file_size, width, height)
                        print(f"Color depth calculation: {color_depth:.2f} bits per pixel")
                    elif choice == "3":
                        file_size = get_float("Enter file size:")
                        height = get_float("Enter height:")
                        color_depth = get_float("Enter color depth:")
                        width = calculate_width(file_size, height, color_depth)
                        print(f"Image width calculation: {width:.2f}")
                    elif choice == "4":
                        file_size = get_float("Enter file size:")
                        width = get_float("Enter width:")
                        color_depth = get_float("Enter color depth:")
                        height = calculate_height(file_size, width, color_depth)
                        print(f"Image height calculation: {height:.2f}")
                    elif choice == "5":
                        width = get_float("Enter width:")
                        height = get_float("Enter height:")
                        total_pixels = calculate_total_pixels(width, height)
                        print(f"Total number of pixels: {total_pixels:.0f}")

if __name__ == '__main__':
    main()
