from math import ceil
class PhotoAlbum:
    PAGE_SIZE = 4
    def __init__(self,pages:int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls,photos_count: int) ->'PhotoAlbum':

        return cls(ceil(photos_count/cls.PAGE_SIZE))

    def add_photo(self,label: str):
        for i,page in enumerate(self.photos):
            if len(page) < self.PAGE_SIZE:
                page.append(label)
                return f"{label} photo added successfully on page {i+1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        d = '-'*11 +'\n'
        res = d
        for i in self.photos:
            res+= ' '.join('[]' for _ in i)+'\n'
            res+=d
        return res

#Test code
album = PhotoAlbum(2)

print(album.add_photo("baby"))

print(album.add_photo("first grade"))

print(album.add_photo("eight grade"))

print(album.add_photo("party with friends"))

print(album.photos)

print(album.add_photo("prom"))

print(album.add_photo("wedding"))

print(album.display())