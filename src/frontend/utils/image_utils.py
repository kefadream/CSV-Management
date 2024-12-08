import tkinter as tk

# Définition des chemins des images
IMAGE_PATHS = {
    "browse": "data/images/browse.png",
    "save": "data/images/save.png",
    "select": "data/images/select.png",
    "process": "data/images/process.png",
    "delete": "data/images/delete.png",
    "filter": "data/images/filter.png",
    "edit": "data/images/edit.png",
    "check_duplicates": "data/images/check_duplicates.png",
    "sort": "data/images/sort.png",
    "rename": "data/images/rename.png",
    "remove_duplicates": "data/images/remove_duplicates.png"
}


class ImageLoader:
    def __init__(self, image_paths):
        self.image_paths = image_paths
        self.images = {}

    def load_images(self):
        for key, path in self.image_paths.items():
            self.images[key] = tk.PhotoImage(file=path)

    def get_image(self, key):
        return self.images.get(key)


# Fonction pour charger les images
def load_all_images():
    image_loader = ImageLoader(IMAGE_PATHS)
    image_loader.load_images()
    return image_loader
