import tkinter as tk

# Définition des chemins des images
IMAGE_PATHS = {
    "browse": "src/ui/images/browse.png",
    "save": "src/ui/images/save.png",
    "select": "src/ui/images/select.png",
    "process": "src/ui/images/process.png",
    "delete": "src/ui/images/delete.png",
    "filter": "src/ui/images/filter.png",
    "edit": "src/ui/images/edit.png",
    "check_duplicates": "src/ui/images/check_duplicates.png",
    "sort": "src/ui/images/sort.png",
    "rename": "src/ui/images/rename.png"
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
