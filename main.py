from band import Band
from venue import Venue
from concert import Concert


def main():
    while True:
        print("\n--- Concert Management System ---")
        print("1. Add a Band")
        print("2. Add a Venue")
        print("3. Create a Concert")
        print("4. View Concerts at a Venue")
        print("5. View Bands that performed at a Venue")
        print("6. View all Concerts for a Band")
        print("7. Check if Concert is Hometown Show")
        print("8. Get Concert Introductions for a Band")
        print("9. Get Band with Most Performances")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == "1":
            # Add a Band
            band_name = input("Enter Band Name: ")
            hometown = input("Enter Hometown: ")
            Band.create(band_name, hometown)
            print(f"Band '{band_name}' from '{hometown}' has been added.")

        elif choice == "2":
            # Add a Venue
            venue_title = input("Enter Venue Title: ")
            city = input("Enter City: ")
            Venue.create(venue_title, city)
            print(f"Venue '{venue_title}' in '{city}' has been added.")

        elif choice == "3":
            # Create a Concert
            band_id = int(input("Enter Band ID: "))
            venue_id = int(input("Enter Venue ID: "))
            date = input("Enter Concert Date (YYYY-MM-DD): ")

            concert = Concert.create(band_id, venue_id, date)
            print(f"Concert created for Band ID '{band_id}' at Venue ID '{venue_id}' on {date}.")

        elif choice == "4":
            # View Concerts at a Venue
            venue_id = int(input("Enter Venue ID: "))
            venue = Venue(venue_id, "", "")
            concerts = venue.concerts()
            if concerts:
                print(f"Concerts at Venue ID {venue_id}:")
                for concert in concerts:
                    print(f"Concert ID: {concert[0]}, Band ID: {concert[1]}, Date: {concert[3]}")
            else:
                print(f"No concerts found at Venue ID {venue_id}.")

        elif choice == "5":
            # View Bands that performed at a Venue
            venue_id = int(input("Enter Venue ID: "))
            venue = Venue(venue_id, "", "")
            bands = venue.bands()
            if bands:
                print(f"Bands that performed at Venue ID {venue_id}:")
                for band in bands:
                    print(f"Band ID: {band[0]}, Name: {band[1]}, Hometown: {band[2]}")
            else:
                print(f"No bands found for Venue ID {venue_id}.")

        elif choice == "6":
            # View all Concerts for a Band
            band_id = int(input("Enter Band ID: "))
            band = Band(band_id, "", "")
            concerts = band.concerts()
            if concerts:
                print(f"Concerts for Band ID {band_id}:")
                for concert in concerts:
                    print(f"Concert ID: {concert[0]}, Venue ID: {concert[2]}, Date: {concert[3]}")
            else:
                print(f"No concerts found for Band ID {band_id}.")

        elif choice == "7":
            # Check if Concert is Hometown Show
            concert_id = int(input("Enter Concert ID: "))
            band_id = int(input("Enter Band ID: "))
            venue_id = int(input("Enter Venue ID: "))
            concert = Concert(concert_id, band_id, venue_id, "")
            if concert.hometown_show():
                print(f"The concert is a hometown show for Band ID {band_id}.")
            else:
                print(f"The concert is NOT a hometown show for Band ID {band_id}.")

        elif choice == "8":
            # Get Concert Introductions for a Band
            band_id = int(input("Enter Band ID: "))
            band = Band(band_id, "", "")
            introductions = band.all_introductions()
            if introductions:
                print("Introductions:")
                for intro in introductions:
                    print(intro)
            else:
                print(f"No concerts found for Band ID {band_id}.")

        elif choice == "9":
            # Get Band with Most Performances
            band = Band.most_performances()
            print(f"Band with most performances: {band[1]} from {band[2]}")

        elif choice == "10":
            # Exit
            print("Exiting the Concert Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()