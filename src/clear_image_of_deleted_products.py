import os, sys
import logging
from datetime import datetime
import app


class App(app.App):
    def usage(self):
        super().usage() # call parent class usage method

        print("python/python3 clear_image_of_deleted_products.py (csv_file_name) (upload_dir)")
        print("csv_file_name like: /home/xxx/xxxxxx.csv")
        print("upload_dir like: /home/www/xxx.com/upload")
        print("command like: python3 clear_image_of_deleted_products.py ../data/wc-product-export-10-6-2023-1686380411240.csv /home/example.com/upload")

    def process(self):
        if len(sys.argv) < 3:
            sys.exti(-1)
    
        keyword = 'uploads'

        csv_filename, upload_dir = sys.argv[1], sys.argv[2]
        #remove / from upload_dir tail
        if upload_dir.endswith('/'):
            upload_dir = upload_dir[:-1]
        print(upload_dir)

        data = self.readCsvToDict(csv_filename)
        for line in data:
            sku, images = line['SKU'], line['Images']
            for image in images.split(','):
                image = image.strip()
                idx = image.find(keyword)
                image = image[idx+len(keyword)+1:]
                image_filename = os.path.join(upload_dir, image)
                if os.path.exists(image_filename):
                    os.remove(image_filename)
                    
                    # detect same product images
                    dir_name = os.path.dirname(image_filename)
                    file_name = os.path.basename(image_filename)
                    main_name, ext_name = os.path.splitext(file_name)
                    for f in os.listdir(dir_name):
                        if f.startswith(main_name) and f.endswith(ext_name):
                            os.remove(os.path.join(dir_name, f))
                else:
                    print("Cann't find {}".format(image_filename))


if __name__ == "__main__":
    app = App()
    app.run()