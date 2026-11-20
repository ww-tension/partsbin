# === Stage 60: Add saved views for frequently used filters ===
# Project: PartsBin
class SavedView:
    def __init__(self, name, filters):
        self.name = name
        self.filters = filters

    def to_dict(self):
        return {"name": self.name, "filters": self.filters}

    @staticmethod
    def from_dict(data):
        return SavedView(data["name"], data["filters"])


class SavedViewManager:
    def __init__(self):
        self.views = []

    def save_view(self, name, filters):
        for view in self.views:
            if view.name == name:
                view.filters = filters
                return
        self.views.append(SavedView(name, filters))

    def delete_view(self, name):
        self.views = [v for v in self.views if v.name != name]

    def list_views(self):
        return self.views

    def apply_view(self, parts, name):
        for view in self.views:
            if view.name == name:
                result = parts
                for key, value in view.filters.items():
                    result = [p for p in result if getattr(p, key) == value]
                return result
        return None


def load_saved_views(storage_key):
    try:
        data = get_storage(storage_key)
        return [SavedView.from_dict(item) for item in data]
    except (KeyError, TypeError):
        return []


def save_saved_views(manager, storage_key):
    data = [view.to_dict() for view in manager.views]
    set_storage(storage_key, data)


def prompt_for_view_name(manager):
    names = [v.name for v in manager.list_views()]
    choice = input("Enter a new view name or 'list' to see saved views: ")
    if choice.lower() == "list":
        if names:
            for name in names:
                print(name)
        else:
            print("No saved views yet.")
        return None
    return choice


def save_current_filter_as_view(manager, parts, current_filters):
    name = prompt_for_view_name(manager)
    if name:
        manager.save_view(name, current_filters)
        print(f"Saved view '{name}'.")
