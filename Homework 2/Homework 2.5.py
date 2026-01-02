events = []


def calendar():
    """Creates an event calendar with the ability to add, delete and view events"""

    def add_event(date: str, description: str) -> None:
        """Adds an event to the event list."""
        global events
        events.append({"date": date, "description": description})

    def remove_event(description: str) -> bool:
        """Deletes an event from the event list."""
        for index, event in enumerate(events):
            if event["description"] == description:
                events.pop(index)
                return True
        return False

    def view_events() -> None:
        """Displays a list of all scheduled events"""
        if events:
            print("Майбутні події:")
            for e in events:
                print(f"- {e}")
        else:
            print("Немає запланованих подій.")

    return add_event, remove_event, view_events


add_event, remove_event, view_events = calendar()
add_event("01.01.2026", "Новий рік")
add_event("02.01.2026", "Урок 4")
view_events()
remove_event("Урок 4")
view_events()
